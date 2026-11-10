import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_on_failure(max_retries: int = 3, delay: float = 1.0):
    """Decorator to retry network functions on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}: {e}")
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))
            logger.error(f"Function {func.__name__} failed after {max_retries} attempts")
            raise last_exception
        return wrapper
    return decorator