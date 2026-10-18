import logging
import sys
from typing import Optional

def setup_wallet_logger(name: str = 'wallet_utility_13') -> logging.Logger:
    """Configures a structured logger with exception handling."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_critical_error(logger: logging.Logger, error: Exception, context: Optional[str] = None) -> None:
    """Standardized logging for crypto transaction failures."""
    error_type = type(error).__name__
    details = f" | Context: {context}" if context else ""
    
    if isinstance(error, (ValueError, ConnectionError, TimeoutError)):
        logger.error(f"Recoverable error [{error_type}]: {str(error)}{details}")
    else:
        logger.critical(f"Unrecoverable system failure [{error_type}]: {str(error)}{details}", exc_info=True)

def sanitize_log_message(message: str) -> str:
    """Strip sensitive data from logs before persistence."""
    if not message:
        return ""
    # Example: Basic scrubbing of potential private keys or sensitive patterns
    sensitive_patterns = ["private_key", "mnemonic", "secret"]
    for pattern in sensitive_patterns:
        if pattern in message.lower():
            return f"[REDACTED SENSITIVE DATA IN {pattern.upper()}]"
    return message