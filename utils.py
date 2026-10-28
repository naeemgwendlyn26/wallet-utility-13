import functools
import logging
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    retry_exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """Decorator to retry network operations with exponential backoff."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retry_exceptions as exc:
                    if attempt == max_retries:
                        logger.error(
                            f"Failed {func.__name__} after {max_retries} attempts: {exc}"
                        )
                        raise exc

                    logger.warning(
                        f"Attempt {attempt}/{max_retries} for {func.__name__} failed: {exc}. "
                        f"Retrying in {delay:.2f}s..."
                    )
                    time.sleep(delay)
                    delay *= backoff_factor

        return wrapper

    return decorator


def fetch_rpc_data_with_retry(
    fetch_fn: Callable[[], Any], retries: int = 3
) -> Any:
    """Utility wrapper to execute an RPC call with retry support."""
    @retry_network_op(max_retries=retries)
    def _execute():
        return fetch_fn()

    return _execute()
