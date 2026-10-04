import re

# Regex pattern for standard base58 or hex wallet addresses
ADDRESS_PATTERN = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$|^0x[a-fA-F0-9]{40}$')

def validate_wallet_address(address: str) -> bool:
    """Verify address format against supported blockchain schemes."""
    if not isinstance(address, str):
        return False
    return bool(ADDRESS_PATTERN.match(address))

def validate_amount(amount: float) -> bool:
    """Ensure transaction amount is positive and non-zero."""
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def sanitize_input(data: str) -> str:
    """Strip whitespace and normalize input strings."""
    return data.strip() if data else ""