import re

def validate_wallet_address(address: str) -> bool:
    """Validates standard hex-based wallet address format."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def validate_transaction_amount(amount: float) -> bool:
    """Ensures transaction amount is positive and within reasonable limits."""
    try:
        val = float(amount)
        return 0 < val < 1_000_000
    except (ValueError, TypeError):
        return False

def sanitize_input(data: dict) -> dict:
    """Cleans dictionary input for safe processing."""
    return {k: str(v).strip() for k, v in data.items() if v is not None}