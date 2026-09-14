import logging
from logging.handlers import RotatingFileHandler
import os

LOG_FILE = "wallet-utility-13.log"
MAX_BYTES = 5 * 1024 * 1024
BACKUP_COUNT = 3

def get_logger(name: str) -> logging.Logger:
    """Configures a rotating file logger for wallet operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Create rotating file handler to prevent disk exhaustion
        file_handler = RotatingFileHandler(
            LOG_FILE, 
            maxBytes=MAX_BYTES, 
            backupCount=BACKUP_COUNT
        )
        
        # Standard formatting for audit and debugging
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        
        # Console output for immediate development feedback
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger