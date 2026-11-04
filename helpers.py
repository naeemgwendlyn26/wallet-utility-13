import logging
from typing import Optional, Any

logger = logging.getLogger(__name__)

class WalletError(Exception):
    """Base exception for wallet-utility-13 operations."""
    pass

def validate_address(address: str) -> bool:
    """Basic length and character validation for addresses."""
    if not isinstance(address, str):
        return False
    return 26 <= len(address) <= 42 and address.isalnum()

def safe_execute(func: callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Wrapper to catch execution errors during crypto processing."""
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, ConnectionError) as e:
        logger.error(f"Execution failed in {func.__name__}: {str(e)}")
        return None
    except Exception as e:
        logger.critical(f"Unexpected system failure: {str(e)}")
        raise WalletError("Critical failure in wallet-utility-13") from e

def format_amount(amount: Any) -> float:
    """Conversion with safe fallback for invalid inputs."""
    try:
        val = float(amount)
        if val < 0:
            raise ValueError("Negative balance detected")
        return val
    except (ValueError, TypeError):
        logger.warning(f"Invalid amount input: {amount}")
        return 0.0