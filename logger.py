import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(
    name: str = "wallet_utility",
    log_file: str = "logs/wallet.log",
    level: int = logging.INFO
) -> logging.Logger:
    """Configures and returns a logger instance with rotating file handler."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console output handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Create log directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    # File rotation: max 5MB per log file, keeping up to 3 backups
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Pre-configured logger instance for crypto wallet operations
wallet_logger = setup_logger()
