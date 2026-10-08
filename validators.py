import re
from typing import Any

class ValidationError(Exception):
    """Custom exception for crypto input validation failures."""
    pass

def validate_address(address: Any) -> str:
    """Validates blockchain address format (hex string)."""
    if not isinstance(address, str):
        raise ValidationError("Address must be a string")
    
    # Basic hex check for crypto addresses
    if not re.fullmatch(r'0x[a-fA-F0-9]{40}', address):
        raise ValidationError("Invalid blockchain address format")
    return address

def validate_amount(amount: Any) -> float:
    """Validates transaction amount as positive float."""
    try:
        val = float(amount)
        if val <= 0:
            raise ValidationError("Amount must be positive")
        return val
    except (ValueError, TypeError):
        raise ValidationError("Amount must be a numeric value")

def validate_payload(data: dict) -> bool:
    """Ensures mandatory fields exist and are valid."""
    required = {'address', 'amount'}
    if not all(k in data for k in required):
        raise ValidationError("Missing required transaction fields")
    
    validate_address(data['address'])
    validate_amount(data['amount'])
    return True