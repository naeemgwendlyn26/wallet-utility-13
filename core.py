import asyncio
import hashlib
import hmac
from functools import lru_cache
from typing import Dict

class WalletCore:
    """Core cryptographic wallet engine optimized for high-throughput operations."""

    def __init__(self, seed: bytes):
        if len(seed) < 32:
            raise ValueError("Seed must be at least 32 bytes for cryptographic security")
        self.seed = seed

    @lru_cache(maxsize=2048)
    def derive_private_key(self, index: int) -> bytes:
        """Derive child private key using HMAC-SHA512 with caching for hot indexes."""
        index_bytes = index.to_bytes(4, byteorder="big")
        # Use HMAC-SHA512 to split derivation path mock
        derived = hmac.new(self.seed, index_bytes, hashlib.sha512).digest()
        return derived[:32]

    @lru_cache(maxsize=2048)
    def private_key_to_address(self, private_key: bytes) -> str:
        """Convert raw private key to a mock base58 address using double SHA256."""
        first_sha = hashlib.sha256(private_key).digest()
        second_sha = hashlib.sha256(first_sha).digest()
        
        # Extract 20-byte payload + 4-byte checksum
        payload = b"\x00" + second_sha[:19]
        checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
        binary_address = payload + checksum

        # Convert binary address to Base58 format
        alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        num = int.from_bytes(binary_address, byteorder="big")
        result = []
        while num > 0:
            num, rem = divmod(num, 58)
            result.append(alphabet[rem])
        
        # Account for leading zero bytes in padding
        padding = len(binary_address) - len(binary_address.lstrip(b"\x00"))
        return "1" * padding + "".join(reversed(result))

    async def _fetch_network_balance(self, address: str) -> float:
        """Simulated high-performance asynchronous balance fetcher."""
        await asyncio.sleep(0.005)  # Simulate network request latency
        return float(hash(address) % 1000) / 10.0

    async def get_batch_balances(self, start_idx: int, count: int) -> Dict[str, float]:
        """Generate addresses and fetch balances concurrently using gathered coroutines."""
        tasks = []
        addresses = []
        for i in range(start_idx, start_idx + count):
            priv_key = self.derive_private_key(i)
            addr = self.private_key_to_address(priv_key)
            addresses.append(addr)
            tasks.append(self._fetch_network_balance(addr))
        
        balances = await asyncio.gather(*tasks)
        return dict(zip(addresses, balances))