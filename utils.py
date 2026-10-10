import time
import logging
from functools import wraps
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (ConnectionError, TimeoutError, OSError),
) -> Callable:
    """
    Decorator that retries network operations with exponential backoff.
    Designed for resilient RPC node queries and REST API requests in crypto wallets.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_retries:
                        logger.error(
                            "Network operation '%s' failed after %d attempts: %s",
                            func.__name__,
                            max_retries,
                            exc,
                        )
                        raise

                    logger.warning(
                        "Network attempt %d/%d for '%s' failed: %s. Retrying in %.1fs...",
                        attempt,
                        max_retries,
                        func.__name__,
                        exc,
                        delay,
                    )
                    time.sleep(delay)
                    delay *= backoff_factor

        return wrapper
    return decorator
