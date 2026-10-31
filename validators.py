import time
import functools
import logging

# Logger instance for wallet-utility-13
logger = logging.getLogger('wallet-utility-13')

def retry_network_op(retries=3, delay=2, backoff=2):
    """Decorator for retrying unstable network operations."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt {attempt + 1} failed for {func.__name__}")
                        raise e
                    
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {current_delay}s: {e}")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=1)
def validate_node_connection(node_url: str) -> bool:
    """Placeholder for actual network health checks."""
    # Simulate network connectivity check
    if not node_url.startswith("https://"):
        raise ConnectionError("Invalid node protocol")
    return True