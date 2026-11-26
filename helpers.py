import logging
from typing import Optional, Dict, Any

def format_address(address: str) -> str:
    """Truncates long crypto addresses for UI display."""
    if len(address) <= 12:
        return address
    return f"{address[:6]}...{address[-4:]}"

def validate_transaction_amount(amount: float) -> bool:
    """Ensures transaction amounts are non-negative."""
    return amount >= 0

def get_logger(name: str) -> logging.Logger:
    """Standardized logger configuration for wallet modules."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

def sanitize_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Removes null values from transaction dictionaries."""
    return {k: v for k, v in payload.items() if v is not None}