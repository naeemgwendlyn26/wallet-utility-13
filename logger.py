import logging
import sys
import os

def setup_logger(name: str) -> logging.Logger:
    """Configures a standardized logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    try:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        if not logger.handlers:
            logger.addHandler(handler)
    except Exception as e:
        # Fallback to stderr if standard stream initialization fails
        print(f"Critical failure initializing logger: {e}", file=sys.stderr)
        
    return logger

def log_error(logger: logging.Logger, error: Exception, context: str = "operation") -> None:
    """Centralized error reporting for edge cases."""
    if not isinstance(error, Exception):
        logger.error(f"Invalid error type provided: {type(error)}")
        return

    error_type = type(error).__name__
    msg = f"Error during {context} [{error_type}]: {str(error)}"
    
    if error_type in ['ConnectionError', 'TimeoutError']:
        logger.warning(msg)
    elif error_type in ['ValueError', 'TypeError']:
        logger.error(f"Logic error detected: {msg}")
    else:
        logger.critical(f"Unhandled system exception: {msg}", exc_info=True)