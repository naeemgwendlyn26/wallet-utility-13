import functools
import time
from typing import Any, Callable, Dict

# Cache dictionary for wallet balance lookups to improve latency
_balance_cache: Dict[str, tuple] = {}
CACHE_TTL = 30

def cached_balance_lookup(func: Callable) -> Callable:
    """Decorator for rate-limited balance lookups."""
    @functools.wraps(func)
    def wrapper(address: str, *args, **kwargs) -> Any:
        now = time.time()
        if address in _balance_cache:
            val, timestamp = _balance_cache[address]
            if now - timestamp < CACHE_TTL:
                return val
        
        result = func(address, *args, **kwargs)
        _balance_cache[address] = (result, now)
        return result
    return wrapper

class WalletHandler:
    """Performance-focused wallet data processor."""

    def __init__(self, provider: Any):
        self.provider = provider

    @cached_balance_lookup
    def get_wallet_balance(self, address: str) -> float:
        """Fetches and caches balance from blockchain node."""
        balance = self.provider.fetch_balance(address)
        return float(balance)

    def batch_process_balances(self, addresses: list) -> Dict[str, float]:
        """Efficient mapping of multiple wallet addresses."""
        return {addr: self.get_wallet_balance(addr) for addr in addresses}