"""Logger module for wallet-utility with rotation."""

import logging
import logging.handlers

from pathlib import Path

def get_logger(name: str = "wallet_utility", level: int = logging.INFO) -> logging.Logger:
    """Return configured logger using rotating file handler."""
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger
    logger.setLevel(level)
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"{name}.log"
    file_handler = logging.handlers.RotatingFileHandler(
        filename=str(log_file),
        maxBytes=10 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_formatter = logging.Formatter(fmt="%(levelname)s: %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    return logger