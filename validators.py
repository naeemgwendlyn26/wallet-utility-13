import re
from typing import Optional

class ValidationError(Exception):
    """Base exception for address validation failures."""
    pass

def validate_crypto_address(address: str, currency: str = "BTC") -> bool:
    """
    Validates cryptocurrency address formats with edge case handling.
    """
    if not isinstance(address, str):
        raise ValidationError("Address must be a string")
    
    if not address or len(address) < 26 or len(address) > 42:
        raise ValidationError("Invalid address length")

    # Currency specific regex patterns
    patterns = {
        "BTC": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$",
        "ETH": r"^0x[a-fA-F0-9]{40}$"
    }

    pattern = patterns.get(currency.upper())
    if not pattern:
        raise ValidationError(f"Unsupported currency: {currency}")

    try:
        if not re.match(pattern, address):
            raise ValidationError(f"Malformed {currency} address format")
    except re.error as e:
        raise ValidationError(f"Regex engine error: {str(e)}")

    return True

def sanitize_input(data: Optional[str]) -> str:
    """
    Safely cleans input strings to prevent injection.
    """
    if data is None:
        return ""
    
    # Remove non-alphanumeric chars except basic punctuation
    sanitized = re.sub(r'[^a-zA-Z0-9]', '', data)
    return sanitized.strip()