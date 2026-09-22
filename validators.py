import time
import logging
from functools import wraps
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_retries: int = 3, delay: float = 1.0):
    """
    decorator for retrying network operations on failure
    exponential backoff applied to sequential attempts
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"attempt {attempt} failed for {func.__name__}: {e}")
                    
                    if attempt < max_retries:
                        time.sleep(current_delay)
                        current_delay *= 2
                    else:
                        break
            
            logger.error(f"operation {func.__name__} failed after {max_retries} attempts")
            raise last_exception
        return wrapper
    return decorator