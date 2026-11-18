import time
import functools
import logging
from typing import Callable, Any

# Configure logger for network operations
logger = logging.getLogger('wallet-utility-13')

class NetworkRetryError(Exception):
    """Custom exception for persistent network failure."""
    pass

def with_retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator to add retry logic for volatile network calls.
    Retries up to max_attempts with an exponential backoff.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError, IOError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed for {func.__name__}: {e}")
                    if attempt < max_attempts:
                        time.sleep(current_delay)
                        current_delay *= 2
            
            logger.error(f"Final attempt failed for {func.__name__} after {max_attempts} tries")
            raise NetworkRetryError(f"Failed after {max_attempts} attempts: {last_exception}") from last_exception
        return wrapper
    return decorator