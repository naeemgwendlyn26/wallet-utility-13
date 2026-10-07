import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_op(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator to retry network-bound operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            last_exception = None
            
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            
            logger.error("Max retries exceeded for network operation.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_op(retries=3)
def fetch_blockchain_data(endpoint: str):
    """Example network call for wallet utility."""
    # Placeholder for actual network request logic
    return {"status": "ok", "data": "block_hash_0x123"}