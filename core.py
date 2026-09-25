import time
import functools
import requests
from typing import Callable, Any

def retry_network_call(max_retries: int = 3, delay: float = 2.0) -> Callable:
    """Decorator to retry network requests on failure."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    last_exception = e
                    time.sleep(delay * (attempt + 1))
            raise last_exception
        return wrapper
    return decorator

@retry_network_call(max_retries=3, delay=1.0)
def fetch_wallet_balance(api_url: str, address: str) -> dict:
    """Fetch wallet balance with built-in retry logic."""
    response = requests.get(f"{api_url}/balance/{address}", timeout=10)
    response.raise_for_status()
    return response.json()