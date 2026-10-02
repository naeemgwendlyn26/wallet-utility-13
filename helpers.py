import re
from typing import Optional

def validate_address(address: str) -> bool:
    """Validate cryptocurrency wallet address format."""
    # Pattern for standard hex-based addresses
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return bool(re.match(pattern, address))

def validate_amount(amount: float) -> bool:
    """Ensure transaction amount is positive and non-zero."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def sanitize_input(data: str) -> Optional[str]:
    """Remove whitespace and validate basic input bounds."""
    if not data or not isinstance(data, str):
        return None
    
    cleaned = data.strip()
    if len(cleaned) < 10:
        return None
        
    return cleaned

def process_transaction(address: str, amount: float) -> bool:
    """Core validation logic for the main processing loop."""
    sanitized = sanitize_input(address)
    if not sanitized or not validate_address(sanitized):
        return False
        
    if not validate_amount(amount):
        return False
        
    return True