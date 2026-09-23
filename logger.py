import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(name: str = 'wallet-utility-13', log_file: str = 'app.log') -> logging.Logger:
    """Configures a rotating file logger for the wallet utility."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is re-initialized
    if logger.hasHandlers():
        logger.handlers.clear()

    # Ensure logs directory exists
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Rotating file handler: 5MB per file, keep 3 backups
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=3
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Stream handler for console output
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger