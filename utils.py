import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_on_network_error(
    max_retries: int = 3,
    base_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """
    Decorator that retries a function with exponential backoff upon network failures.
    
    Useful for resilient crypto RPC node requests and API queries.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = base_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_retries:
                        logger.error(
                            f"Operation {func.__name__} failed after {max_retries} attempts: {exc}"
                        )
                        raise exc
                    logger.warning(
                        f"Attempt {attempt}/{max_retries} failed for {func.__name__}: {exc}. "
                        f"Retrying in {delay:.2f}s..."
                    )
                    time.sleep(delay)
                    delay *= backoff_factor
        return wrapper
    return decorator
