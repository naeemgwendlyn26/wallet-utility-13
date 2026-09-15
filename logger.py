import logging
import sys
import os

def setup_logger(name: str = "wallet-utility-13") -> logging.Logger:
    """Configures a robust logger for cryptographic operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    try:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        if not logger.handlers:
            logger.addHandler(handler)
    except Exception as e:
        print(f"Critical: Logger initialization failure: {e}", file=sys.stderr)
        sys.exit(1)

    return logger

def log_error(logger: logging.Logger, err: Exception, context: str = "operation") -> None:
    """Standardized logging format for caught edge-case exceptions."""
    if isinstance(err, (ConnectionError, TimeoutError)):
        logger.error(f"Network-related fault during {context}: {str(err)}")
    elif isinstance(err, ValueError):
        logger.warning(f"Validation failure in {context}: {str(err)}")
    else:
        logger.critical(f"Unhandled system exception in {context}: {type(err).__name__} - {str(err)}")

# Instance for global module usage
wallet_logger = setup_logger()