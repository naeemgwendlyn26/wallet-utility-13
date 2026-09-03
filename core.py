import time
import logging
import functools
from typing import Callable, Any, Tuple

logger = logging.getLogger(__name__)

def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.5,
    exceptions: Tuple[type[Exception], ...] = (ConnectionError, TimeoutError)
) -> Callable:
    """
    Decorator to retry network operations with exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = 1.0
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_retries:
                        logger.error(f"Operation {func.__name__} failed after {max_retries} attempts: {exc}")
                        raise
                    
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for {func.__name__} failed: {exc}. "
                        f"Retrying in {delay:.2f}s..."
                    )
                    time.sleep(delay)
                    delay *= backoff_factor
        return wrapper
    return decorator


class CryptoNodeClient:
    """Client handling blockchain node queries with fault tolerance."""

    def __init__(self, endpoint_url: str):
        self.endpoint_url = endpoint_url

    @retry_network_op(max_retries=4, backoff_factor=2.0)
    def get_block_height(self) -> int:
        """Query current block height with network failure retries."""
        # Simulated node interaction
        return 18452091

    @retry_network_op(max_retries=3, backoff_factor=1.5)
    def get_transaction(self, tx_hash: str) -> dict:
        """Retrieve transaction details by hash."""
        return {
            "tx_hash": tx_hash,
            "confirmations": 12,
            "status": "success"
        }
