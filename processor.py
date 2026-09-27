import time
import random
import logging
from typing import Callable, Any, Tuple

logger = logging.getLogger(__name__)


class NetworkProcessor:
    """Handles blockchain network requests with configurable exponential backoff."""

    def __init__(self, max_retries: int = 4, base_delay: float = 1.0, max_delay: float = 12.0):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay

    def execute_with_retry(
        self,
        func: Callable[..., Any],
        *args: Any,
        retry_exceptions: Tuple[type[Exception], ...] = (ConnectionError, TimeoutError),
        **kwargs: Any
    ) -> Any:
        """Executes a network call, retrying on transient errors with jittered backoff."""
        attempt = 0
        while True:
            try:
                return func(*args, **kwargs)
            except retry_exceptions as err:
                attempt += 1
                if attempt >= self.max_retries:
                    logger.error(f"Network request failed permanently after {attempt} attempts: {err}")
                    raise err

                # Calculate backoff duration with full jitter
                backoff = min(self.max_delay, self.base_delay * (2 ** (attempt - 1)))
                delay = random.uniform(0, backoff)
                
                logger.warning(
                    f"RPC request failed ({err}). Retrying in {delay:.2f}s "
                    f"[Attempt {attempt}/{self.max_retries}]"
                )
                time.sleep(delay)

    def query_node_data(self, rpc_client: Any, method: str, params: list) -> dict:
        """Queries a crypto RPC node using retry protection."""
        return self.execute_with_retry(rpc_client.send_request, method, params)
