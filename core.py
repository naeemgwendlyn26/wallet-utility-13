import hashlib
from functools import lru_cache
from typing import Dict, List


@lru_cache(maxsize=4096)
def sha256_double(data_bytes: bytes) -> bytes:
    """Compute double SHA-256 hash with caching for repeated inputs."""
    return hashlib.sha256(hashlib.sha256(data_bytes).digest()).digest()


@lru_cache(maxsize=2048)
def derive_address_checksum(address_raw: str) -> str:
    """Fast EIP-55 style checksum address calculation with memoization."""
    address_clean = address_raw.lower().replace("0x", "")
    hash_hex = hashlib.sha256(address_clean.encode("utf-8")).hexdigest()

    checksummed = []
    for i, char in enumerate(address_clean):
        if char.isdigit():
            checksummed.append(char)
        elif int(hash_hex[i], 16) >= 8:
            checksummed.append(char.upper())
        else:
            checksummed.append(char.lower())
    return "0x" + "".join(checksummed)


class TransactionBatchProcessor:
    """High-performance batch processing engine for crypto transaction payload validation."""

    def __init__(self, cache_size: int = 1000):
        self._cache_size = cache_size
        self._precomputed_hashes: Dict[str, bytes] = {}

    def batch_hash_transactions(self, raw_tx_list: List[bytes]) -> List[bytes]:
        """Process a list of raw transaction bytes, leveraging cached double-SHA256 results."""
        results = []
        for raw_tx in raw_tx_list:
            tx_hash = sha256_double(raw_tx)
            results.append(tx_hash)
        return results

    def validate_and_format_addresses(self, addresses: List[str]) -> List[str]:
        """Validate and apply checksum formatting across a batch of wallet addresses."""
        formatted = []
        for addr in addresses:
            if not addr or len(addr) < 40:
                continue
            formatted.append(derive_address_checksum(addr))
        return formatted

    def clear_caches(self) -> None:
        """Purge precomputation caches to free memory."""
        sha256_double.cache_clear()
        derive_address_checksum.cache_clear()
