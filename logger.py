import logging
import sys
from logging.handlers import RotatingFileHandler

def get_logger(name: str) -> logging.Logger:
    """Configures and returns a logger instance for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Console output
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Rotating file output for audit trails
        file_handler = RotatingFileHandler(
            'wallet_utility.log', 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

# Standard logger for the project
logger = get_logger('wallet-utility-13')