import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_on_network_error(
    max_retries: int = 3,
    base_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """Decorator that retries network operations with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            delay = base_delay

            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    retries += 1
                    if retries > max_retries:
                        logger.error("Max retries (%d) reached for %s: %s", max_retries, func.__name__, err)
                        raise

                    # Add jitter to prevent simultaneous retry requests
                    jitter = random.uniform(0, 0.1 * delay)
                    sleep_time = delay + jitter
                    logger.warning(
                        "Network operation failed (%s). Retrying %d/%d in %.2fs...",
                        err, retries, max_retries, sleep_time
                    )
                    time.sleep(sleep_time)
                    delay *= backoff_factor

        return wrapper
    return decorator

class WalletRPCClient:
    """Core client handling resilient blockchain RPC communications."""

    def __init__(self, endpoint_url: str):
        self.endpoint_url = endpoint_url

    @retry_on_network_error(max_retries=4, base_delay=0.5)
    def query_balance(self, address: str) -> float:
        """Query wallet balance with exponential backoff retry protection."""
        if not address.startswith("0x") or len(address) != 42:
            raise ValueError(f"Invalid wallet address format: {address}")
        
        # Simulated balance query returning formatted value
        return 42.108
