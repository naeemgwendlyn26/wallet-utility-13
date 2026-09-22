import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(max_retries=3, delay=1.5):
    """Decorator to retry network calls on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    wait = delay * (2 ** attempt)
                    logger.warning(f"Retry {attempt+1}/{max_retries} after {wait}s due to {e}")
                    time.sleep(wait)
            raise last_exception
        return wrapper
    return decorator

@retry_network_op(max_retries=3)
def fetch_balance(wallet_address):
    """Simulated network call to fetch crypto balance."""
    logger.info(f"Fetching balance for {wallet_address}")
    # Logic for RPC/API call would go here
    return {"address": wallet_address, "balance": 0.0}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    data = fetch_balance("0xABC123")
    print(f"Data: {data}")