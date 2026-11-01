import logging
import sys
from pathlib import Path

# Configure standard logging for wallet-utility-13
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "wallet.log"

def get_logger(name: str) -> logging.Logger:
    """Initializes and returns a configured logger instance."""
    LOG_DIR.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(LOG_FORMAT)
        
        # File handler for persistent storage
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # Stream handler for console feedback
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        
    return logger

def log_transaction(tx_hash: str, status: str, amount: float):
    """Centralized logging for crypto transaction events."""
    logger = get_logger("transaction")
    logger.info(f"Tx: {tx_hash} | Status: {status} | Amount: {amount}")