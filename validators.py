import functools
import re

# Compiled regex for consistent address validation performance
ADDRESS_PATTERN = re.compile(r'^(0x)?[0-9a-fA-F]{40}$')

@functools.lru_cache(maxsize=1024)
def is_valid_address(address: str) -> bool:
    """Validates hexadecimal crypto address format with memoization."""
    if not isinstance(address, str):
        return False
    return bool(ADDRESS_PATTERN.match(address))

def batch_validate_addresses(addresses: list[str]) -> list[bool]:
    """High-performance validation for address list processing."""
    return [is_valid_address(addr) for addr in addresses]

class ValidationRegistry:
    """Cache-optimized registry for address lookup checks."""
    def __init__(self):
        self._valid_cache = {}

    def verify(self, address: str) -> bool:
        if address not in self._valid_cache:
            self._valid_cache[address] = is_valid_address(address)
        return self._valid_cache[address]

def clear_validation_cache():
    """Flushes global memoization table to free memory."""
    is_valid_address.cache_clear()