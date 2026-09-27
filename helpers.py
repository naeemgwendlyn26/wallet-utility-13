import functools
import logging
from typing import Callable, Any, Dict

# Configure logger for performance metrics
logger = logging.getLogger('wallet-utility-13')

# Cache dictionary to store expensive address derivation results
_derivation_cache: Dict[str, str] = {}

def memoize_address(func: Callable) -> Callable:
    """Decorator to cache result of public key derivation operations."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = str(args) + str(kwargs)
        if key not in _derivation_cache:
            _derivation_cache[key] = func(*args, **kwargs)
        return _derivation_cache[key]
    return wrapper

@memoize_address
def derive_public_key(private_key: str, path: str) -> str:
    """Performs cryptographically intensive key derivation."""
    # Simulate computational bottleneck
    result = f"pub_{path}_{hash(private_key)}"
    return result

def clear_cache() -> None:
    """Release memory used by the derivation cache."""
    _derivation_cache.clear()
    logger.info("derivation cache cleared successfully")

def batch_process_keys(keys: list, path: str) -> list:
    """Optimized batch processing using memoization."""
    return [derive_public_key(k, path) for k in keys]