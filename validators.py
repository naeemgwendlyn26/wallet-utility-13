import re
from typing import Optional

def validate_ethereum_address(address: str) -> bool:
    """
    Checks if the provided string is a valid hexadecimal Ethereum address.

    Args:
        address: The hex string to validate.

    Returns:
        bool: True if format is valid, False otherwise.
    """
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return bool(re.match(pattern, address))

def validate_amount(amount: str) -> bool:
    """
    Validates that the amount string is a positive numeric decimal.

    Args:
        amount: The string representation of the crypto amount.

    Returns:
        bool: True if valid numeric amount, False otherwise.
    """
    try:
        val = float(amount)
        return val > 0
    except (ValueError, TypeError):
        return False

def format_currency_key(asset_symbol: Optional[str]) -> str:
    """
    Standardizes asset symbols for internal lookup.

    Args:
        asset_symbol: The ticker symbol or alias.

    Returns:
        str: Uppercase sanitized ticker or default 'UNKNOWN'.
    """
    if not asset_symbol:
        return "UNKNOWN"
    return str(asset_symbol).strip().upper()