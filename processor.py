import time
import logging
from typing import Callable, Any, Optional

logger = logging.getLogger(__name__)

def with_retry(func: Callable, retries: int = 3, delay: float = 1.0, backoff: float = 2.0) -> Any:
    """Executes a network-bound function with exponential backoff."""
    current_delay = delay
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            if attempt == retries - 1:
                logger.error(f"Final attempt failed: {str(e)}")
                raise
            
            logger.warning(f"Attempt {attempt + 1} failed, retrying in {current_delay}s...")
            time.sleep(current_delay)
            current_delay *= backoff

def fetch_wallet_balance(api_client: Any, wallet_address: str) -> dict:
    """
    Example implementation for fetching balance with retry logic.
    Uses a lambda to wrap the specific network call.
    """
    return with_retry(lambda: api_client.get_balance(wallet_address))

if __name__ == "__main__":
    # Example usage for wallet-utility-13 integration
    logging.basicConfig(level=logging.INFO)
    print("Network operation retry wrapper initialized")