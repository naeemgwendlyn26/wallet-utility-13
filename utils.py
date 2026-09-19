import time
import logging
from functools import wraps
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_on_failure(max_attempts: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}")
                    
                    if attempt < max_attempts:
                        time.sleep(current_delay)
                        current_delay *= 2
            
            logger.error(f"Operation failed after {max_attempts} attempts")
            raise last_exception
            
        return wrapper
    return decorator