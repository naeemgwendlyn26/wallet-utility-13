import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logger(
    name: str = "wallet_utility",
    log_dir: str = "logs",
    log_file: str = "wallet.log",
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 5,
    level: int = logging.INFO,
) -> logging.Logger:
    """Configures and returns a logger instance with rotating file and console output."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if logger.handlers:
        return logger

    # Ensure output log directory exists
    os.makedirs(log_dir, exist_ok=True)
    full_log_path = os.path.join(log_dir, log_file)

    # Shared log formatting for wallet transactions and operations
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Rotating file handler to manage disk space for heavy logging
    file_handler = RotatingFileHandler(
        full_log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Standard output stream handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


def get_wallet_logger(module_name: Optional[str] = None) -> logging.Logger:
    """Retrieves a logger or child logger configured for wallet sub-modules."""
    base_logger = setup_logger()
    if module_name:
        return base_logger.getChild(module_name)
    return base_logger
