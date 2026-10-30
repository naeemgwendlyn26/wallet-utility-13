import logging
import sys

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures a standard console logger for wallet operations."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Prevent duplicate handlers if setup is called multiple times
    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

def log_transaction(logger: logging.Logger, tx_hash: str, status: str) -> None:
    """Standardizes logging for blockchain transaction lifecycle events."""
    logger.info(f"Transaction [{tx_hash}] status update: {status}")

def log_error(logger: logging.Logger, message: str, exc: Exception = None) -> None:
    """Formats error messages with optional exception details."""
    error_msg = f"Error: {message}"
    if exc:
        error_msg += f" | Details: {str(exc)}"
    logger.error(error_msg)