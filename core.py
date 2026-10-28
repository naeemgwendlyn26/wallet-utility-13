import hashlib
from functools import lru_cache
from typing import Dict, List, Tuple


class FastCryptoCore:
    """Core cryptographic utility with optimized hashing and lookups."""

    def __init__(self, cache_size: int = 2048):
        self.cache_size = cache_size

    @staticmethod
    @lru_cache(maxsize=2048)
    def double_sha256(data: bytes) -> bytes:
        """Compute double SHA-256 hash with memoization for repeated payloads."""
        return hashlib.sha256(hashlib.sha256(data).digest()).digest()

    @staticmethod
    @lru_cache(maxsize=1024)
    def fast_address_validate(address: str) -> bool:
        """Validate address structure using cached pattern checking."""
        if not address or len(address) < 26 or len(address) > 90:
            return False
        valid_prefixes = ("1", "3", "bc1", "0x")
        return address.startswith(valid_prefixes)

    def batch_hash_payloads(self, payloads: List[bytes]) -> Dict[bytes, bytes]:
        """Process batch of payloads utilizing cached double SHA-256."""
        return {data: self.double_sha256(data) for data in payloads}

    def deduplicate_utxos(self, utxos: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Fast UTXO deduplication using set-based hash tracking."""
        seen = set()
        unique_utxos = []
        for utxo in utxos:
            key = (utxo.get("txid"), utxo.get("vout"))
            if key not in seen:
                seen.add(key)
                unique_utxos.append(utxo)
        return unique_utxos
