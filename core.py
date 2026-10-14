import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def retry_network_call(max_retries: int = 3, delay: float = 1.0, exceptions: tuple = (Exception, )) -> Callable:
    """Decorator for retrying unstable network operations."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"Function {func.__name__} failed after {max_retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_call(max_retries=3, delay=2.0)
def fetch_balance(wallet_address: str) -> float:
    """Simulated network call to retrieve crypto balance."""
    # Actual network implementation goes here
    return 0.0

def main():
    try:
        balance = fetch_balance("0xABC123")
        print(f"Wallet balance: {balance}")
    except Exception as e:
        print(f"Critical network failure: {e}")

if __name__ == "__main__":
    main()