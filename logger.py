import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = "wallet.log") -> logging.Logger:
    """Initializes a rotating file logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Rotate files at 5MB, keep 3 backups
        handler = RotatingFileHandler(
            log_file, maxBytes=5 * 1024 * 1024, backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Add console output for development visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instance for global application usage
wallet_logger = setup_logger("wallet-utility-13")