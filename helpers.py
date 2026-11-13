import functools
import time
from typing import Any, Callable

# Cache dictionary to store function call results
_CACHE = {}

def memoize(func: Callable) -> Callable:
    """Performance decorator for expensive cryptographic calculations."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Memory-efficient generator for large wallet address datasets."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def timed_execution(func: Callable) -> Callable:
    """Profiler wrapper for monitoring core module latency."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        if duration > 0.5:
            print(f"Warning: {func.__name__} took {duration:.4f}s")
        return result
    return wrapper