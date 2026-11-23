import logging
import functools
import time
from typing import Callable, Any

# Configure structured logging for high-frequency crypto wallet operations
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("wallet-utility-13")

# Cache dictionary for performance optimization of redundant calculations
_execution_cache = {}

def memoize_performance(func: Callable) -> Callable:
    """Decorator to cache function results and reduce overhead in core logic."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key in _execution_cache:
            return _execution_cache[key]
        
        result = func(*args, **kwargs)
        _execution_cache[key] = result
        return result
    return wrapper

def log_execution_time(func: Callable) -> Callable:
    """Decorator for monitoring throughput of critical wallet operations."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        if duration > 0.1:
            logger.warning(f"High latency detected in {func.__name__}: {duration:.4f}s")
        return result
    return wrapper