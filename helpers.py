import functools
import logging
import random
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger("wallet_utility.helpers")


def retry_network_call(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """Decorator that retries network operations using exponential backoff with jitter."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_retries:
                        logger.error(
                            f"Network call '{func.__name__}' failed after {max_retries} attempts: {exc}"
                        )
                        raise

                    # Exponential backoff with a small jitter factor
                    jitter = random.uniform(0.8, 1.2)
                    sleep_time = delay * jitter
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for '{func.__name__}' failed ({exc}). "
                        f"Retrying in {sleep_time:.2f}s..."
                    )
                    time.sleep(sleep_time)
                    delay *= backoff_factor

        return wrapper

    return decorator
