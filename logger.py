import logging
import functools
import time
from typing import Callable, Any

# Configure performance-optimized logging for wallet transactions
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('wallet-utility-13')

def performance_monitor(func: Callable) -> Callable:
    """
    Decorator for measuring execution time of critical wallet operations
    Reduces overhead by using local time references and conditional logging
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        duration = end_time - start_time
        if duration > 0.5:
            logger.warning(f'High latency in {func.__name__}: {duration:.4f}s')
        return result
    return wrapper

def log_transaction(tx_id: str, status: str) -> None:
    """
    Optimized logging for frequent blockchain transaction updates
    Uses f-strings for faster string formatting
    """
    logger.info(f'tx_update:{tx_id}:{status}')