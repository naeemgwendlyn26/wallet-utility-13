import hashlib
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from typing import Dict, List, Tuple


class WalletCore:
    """Core cryptographic and wallet processing engine with cached operations."""

    def __init__(self, max_workers: int = 4):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    @staticmethod
    @lru_cache(maxsize=1024)
    def derive_address_fast(public_key_hex: str, network_prefix: bytes = b"\x00") -> str:
        """Derives a crypto address from a public key with LRU caching for performance."""
        pub_bytes = bytes.fromhex(public_key_hex)
        sha = hashlib.sha256(pub_bytes).digest()
        ripemd = hashlib.new("ripemd160", sha).digest()

        payload = network_prefix + ripemd
        checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
        return (payload + checksum).hex()

    def batch_derive_addresses(
        self, public_keys: List[str], network_prefix: bytes = b"\x00"
    ) -> Dict[str, str]:
        """Concurrently derives addresses for a batch of public keys."""
        futures = {
            pk: self.executor.submit(self.derive_address_fast, pk, network_prefix)
            for pk in public_keys
        }
        return {pk: future.result() for pk, future in futures.items()}

    def batch_validate_nonces(self, account_nonces: List[Tuple[str, int, int]]) -> List[bool]:
        """Validates expected vs network nonces in parallel to reduce turnaround latency."""
        def check_nonce(data: Tuple[str, int, int]) -> bool:
            _, expected, current = data
            return current >= expected

        return list(self.executor.map(check_nonce, account_nonces))

    def shutdown(self) -> None:
        """Cleans up internal thread executor resources."""
        self.executor.shutdown(wait=True)
