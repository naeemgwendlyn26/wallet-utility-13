import time
import functools
import logging

# Configure logger for wallet-utility-13
logger = logging.getLogger('wallet_utility')

def retry_network_operation(max_retries=3, delay=2):
    """
    Decorator to retry network functions on failure with exponential backoff.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == max_retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
            return None
        return wrapper
    return decorator