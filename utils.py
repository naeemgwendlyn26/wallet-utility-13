import functools
import hashlib
from typing import Dict, Any, Callable

# Cache for compute-heavy address derivations to improve throughput
CACHE_SIZE = 1024

@functools.lru_cache(maxsize=CACHE_SIZE)
def derive_address_checksum(address: str) -> str:
    """Generates EIP-55 style checksum for wallet addresses."""
    address = address.lower().replace('0x', '')
    hash_str = hashlib.keccak_256(address.encode()).hexdigest()
    result = ['0x']
    for i, char in enumerate(address):
        if int(hash_str[i], 16) >= 8:
            result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)

def batch_process_balances(balances: Dict[str, float]) -> Dict[str, str]:
    """
    Batch processing of wallet balances with cached derivation.
    Reduces redundant hex computations during bulk operations.
    """
    return {
        derive_address_checksum(addr): f"{val:.8f}"
        for addr, val in balances.items()
    }

def clear_derivation_cache():
    """Manual memory management for crypto utility cache."""
    derive_address_checksum.cache_clear()