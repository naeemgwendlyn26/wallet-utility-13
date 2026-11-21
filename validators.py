import re

# Regex for standard EVM-compatible addresses
ADDRESS_PATTERN = re.compile(r'^0x[a-fA-F0-9]{40}$')

def validate_address(address: str) -> bool:
    """Checks if a string is a valid hexadecimal crypto address."""
    if not isinstance(address, str):
        return False
    return bool(ADDRESS_PATTERN.match(address))

def validate_amount(amount: float) -> bool:
    """Ensures transaction amount is positive and not NaN."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def sanitize_input(data: str) -> str:
    """Strips whitespace and converts to lowercase for consistency."""
    return data.strip().lower() if isinstance(data, str) else ""