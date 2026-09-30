import re

def validate_address(address: str, chain: str) -> bool:
    """Validate cryptocurrency address format for supported chains."""
    if not isinstance(address, str) or len(address) < 26 or len(address) > 42:
        return False

    patterns = {
        "eth": r"^0x[a-fA-F0-9]{40}$",
        "btc": r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
    }

    pattern = patterns.get(chain.lower())
    if not pattern:
        return False

    return bool(re.match(pattern, address))

def validate_amount(amount: float) -> bool:
    """Ensure transaction amount is positive and within reasonable bounds."""
    try:
        val = float(amount)
        return 0 < val < 1_000_000
    except (ValueError, TypeError):
        return False

def sanitize_input(data: dict) -> dict:
    """Clean dictionary keys and values for processing."""
    return {k: str(v).strip() for k, v in data.items() if v is not None}