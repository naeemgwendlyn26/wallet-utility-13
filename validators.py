import re
from functools import lru_cache

# Cached regex patterns for performance optimization
# Prevents recompilation of patterns during repeated validation calls
@lru_cache(maxsize=16)
def _get_address_pattern(network: str) -> re.Pattern:
    patterns = {
        "bitcoin": r"^(1|3|bc1)[a-zA-Z0-9]{25,59}$",
        "ethereum": r"^0x[a-fA-F0-9]{40}$"
    }
    return re.compile(patterns.get(network, r".*"))

def is_valid_address(address: str, network: str) -> bool:
    """
    Validates crypto wallet addresses using cached compiled regex.
    Reduces overhead in high-throughput transaction processing.
    """
    if not address or not isinstance(address, str):
        return False
    
    pattern = _get_address_pattern(network)
    return bool(pattern.match(address))

def validate_batch(addresses: list[str], network: str) -> list[bool]:
    """
    Processes address lists in bulk to minimize function call depth.
    """
    pattern = _get_address_pattern(network)
    return [bool(pattern.match(addr)) for addr in addresses if isinstance(addr, str)]