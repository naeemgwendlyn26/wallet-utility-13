import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def with_retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            last_exception = None
            
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    if attempt < retries - 1:
                        time.sleep(current_delay)
                        current_delay *= backoff
            
            logger.error(f"Operation failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@with_retry(retries=3)
def fetch_balance(address: str) -> float:
    """Mock network call to retrieve crypto wallet balance."""
    # Implementation would involve requests/httpx here
    return 0.0