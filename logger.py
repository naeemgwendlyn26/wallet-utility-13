import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='wallet-utility-13', log_file='app.log', level=logging.INFO):
    """Initializes a rotating file logger for crypto operations."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        # Format: timestamp - name - level - message
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Rotation: 5MB per file, keep 3 backups
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Instantiate core application logger
logger = setup_logger()