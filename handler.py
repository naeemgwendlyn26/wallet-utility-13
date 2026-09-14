import functools
from typing import Dict, Any
from collections import deque

# Cache for frequently accessed balance queries
_balance_cache: Dict[str, Any] = {}
_cache_order = deque(maxlen=1000)

@functools.lru_cache(maxsize=128)
def get_wallet_address(pubkey: str) -> str:
    """Derives address from pubkey using memoized computation."""
    # Simulate expensive cryptographic derivation
    return f"addr_{pubkey[-8:]}"

def update_balance_cache(address: str, balance: float) -> None:
    """Updates cache with least recently used eviction strategy."""
    if address not in _balance_cache:
        if len(_cache_order) >= 1000:
            oldest = _cache_order.popleft()
            _balance_cache.pop(oldest, None)
    else:
        _cache_order.remove(address)
    
    _balance_cache[address] = balance
    _cache_order.append(address)

def get_cached_balance(address: str) -> float:
    """Retrieves balance from local memory cache."""
    return _balance_cache.get(address, 0.0)

def clear_cache() -> None:
    """Resets all cached session data."""
    _balance_cache.clear()
    _cache_order.clear()
    get_wallet_address.cache_clear()