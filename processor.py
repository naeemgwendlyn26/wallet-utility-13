import time
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """Executes a network-dependent function with exponential backoff."""
    last_exception = None
    
    for attempt in range(retries):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            last_exception = e
            wait_time = delay * (2 ** attempt)
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
            time.sleep(wait_time)
        except Exception as e:
            logger.error(f"Unrecoverable error during network operation: {e}")
            raise e
            
    logger.error(f"Max retries reached. Final exception: {last_exception}")
    raise last_exception

def process_transaction(tx_data: dict, network_call: Callable) -> dict:
    """
    Wraps network calls for crypto transactions with retry logic.
    """
    try:
        result = retry_network_operation(lambda: network_call(tx_data))
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
