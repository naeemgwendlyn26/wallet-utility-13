import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger("wallet_utility.helpers")

def retry_with_backoff(
    retries: int = 3,
    backoff_in_seconds: float = 1.0,
    max_exponent: int = 5,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator to retry a network-related function call with exponential backoff and jitter.
    Commonly used in blockchain interactions for handling transient RPC or API failures.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= retries:
                        logger.error(f"Failed {func.__name__} after {retries} attempts: {e}")
                        raise e
                    
                    # Exponential backoff formula with full jitter
                    sleep_time = (backoff_in_seconds * (2 ** min(attempt, max_exponent)))
                    jitter = random.uniform(0, 1.0)
                    total_sleep = sleep_time + jitter
                    
                    logger.warning(
                        f"Retrying {func.__name__} due to: {e}. "
                        f"Attempt {attempt}/{retries}. Retrying in {total_sleep:.2f}s..."
                    )
                    time.sleep(total_sleep)
        return wrapper
    return decorator