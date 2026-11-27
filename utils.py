import functools
from typing import Callable, Any, Dict

# Cache for compute-intensive cryptographic address derivations
_ADDRESS_CACHE: Dict[str, str] = {}

def memoize_address_derivation(func: Callable) -> Callable:
    """
    Decorator to cache wallet address derivation results.
    Prevents redundant expensive hashing operations.
    """
    @functools.wraps(func)
    def wrapper(pubkey: str, *args: Any, **kwargs: Any) -> str:
        if pubkey not in _ADDRESS_CACHE:
            _ADDRESS_CACHE[pubkey] = func(pubkey, *args, **kwargs)
        return _ADDRESS_CACHE[pubkey]
    return wrapper

@memoize_address_derivation
def derive_wallet_address(pubkey: str) -> str:
    """
    Simulates a CPU-heavy cryptographic hashing operation.
    """
    # Simulated complex derivation logic
    import hashlib
    return hashlib.sha256(pubkey.encode()).hexdigest()

def clear_cache() -> None:
    """
    Clears memory cache to prevent stale data bloat.
    """
    _ADDRESS_CACHE.clear()

if __name__ == "__main__":
    # Example usage for wallet-utility-13
    addr = derive_wallet_address("pubkey_example_0x123")
    print(f"Generated: {addr}")