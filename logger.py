import logging
import sys
from pathlib import Path

def get_logger(name: str, log_file: str = 'wallet.log') -> logging.Logger:
    """Configures a standard logger for wallet operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    file_path = Path(log_file)
    file_handler = logging.FileHandler(file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Global logger instance for the utility
logger = get_logger('wallet-utility-13')

if __name__ == '__main__':
    logger.info('Logger initialized for crypto utility operations')