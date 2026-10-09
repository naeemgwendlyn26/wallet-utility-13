import logging
import sys
from typing import Optional

def get_wallet_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Initialize and return a configured logger for wallet operations.

    Args:
        name: The name of the logger instance.
        level: The logging severity level.

    Returns:
        A configured logging.Logger instance.
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_transaction(logger: logging.Logger, tx_hash: str, status: str) -> None:
    """
    Log crypto transaction status updates.

    Args:
        logger: The logger instance to use.
        tx_hash: The unique transaction identifier.
        status: The current status of the transaction.
    """
    logger.info(f"Transaction {tx_hash} updated to status: {status}")

def log_error(logger: logging.Logger, error: Exception, context: Optional[str] = None) -> None:
    """
    Log operational errors with optional context.

    Args:
        logger: The logger instance.
        error: The caught exception.
        context: Additional details regarding the failure.
    """
    msg: str = f"Context: {context} | Error: {str(error)}" if context else str(error)
    logger.error(f"Wallet operation failure: {msg}")