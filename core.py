import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_retries=3, delay=1.0, backoff=2.0):
    """Decorator for retrying network functions with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == max_retries:
                        logger.error(f"Final attempt {attempt} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_operation(max_retries=3)
def fetch_balance(address: str):
    """Mock network call to fetch wallet balance."""
    # Simulated network instability
    import random
    if random.random() < 0.7:
        raise ConnectionError("node synchronization timeout")
    return "1.05 BTC"