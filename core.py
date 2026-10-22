import hashlib
import functools
from typing import List, Dict, Tuple

class CoreWalletProcessor:
    """Core utility for optimized crypto key derivation and address checking."""

    def __init__(self, network_prefix: bytes = b'\x00'):
        self.network_prefix = network_prefix

    @staticmethod
    @functools.lru_cache(maxsize=4096)
    def derive_address_fast(pubkey_bytes: bytes) -> str:
        """Derive standard wallet address from public key using cached hashing logic."""
        sha_hash = hashlib.sha256(pubkey_bytes).digest()
        ripemd_hash = hashlib.new('ripemd160', sha_hash).digest()
        checksum = hashlib.sha256(hashlib.sha256(ripemd_hash).digest()).digest()[:4]
        full_payload = ripemd_hash + checksum
        return full_payload.hex()

    def batch_process_signatures(
        self, transactions: List[Dict[str, bytes]]
    ) -> List[Tuple[str, bool]]:
        """Batch process transaction public keys with caching to maximize throughput."""
        results = []
        for tx in transactions:
            pubkey = tx.get('pubkey')
            signature = tx.get('signature')
            if not pubkey or not signature:
                results.append(("", False))
                continue

            address = self.derive_address_fast(pubkey)
            is_valid_len = len(signature) in (64, 65)
            results.append((address, is_valid_len))

        return results

    def clear_derivation_cache(self) -> None:
        """Reset memory cache for key derivations."""
        self.derive_address_fast.cache_clear()
