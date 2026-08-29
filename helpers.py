"""Helper functions for common crypto wallet operations.
Practical utilities for address handling and amount conversion.
"""

import re

def format_balance(balance: int, decimals: int = 18) -> str:
    """Format integer balance to human readable string."""
    if balance < 0:
        return "0"
    formatted = balance / (10 ** decimals)
    return f"{formatted:.8f}".rstrip("0").rstrip(".")

def is_valid_address(address: str) -> bool:
    """Check if address is valid hex format."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))

def to_smallest_unit(amount: float, decimals: int = 18) -> int:
    """Convert decimal amount to smallest unit like wei."""
    return int(amount * (10 ** decimals))

def from_smallest_unit(amount: int, decimals: int = 18) -> float:
    """Convert from smallest unit to decimal amount."""
    return amount / (10 ** decimals)

def shorten_address(address: str, chars: int = 4) -> str:
    """Return shortened address for display purposes."""
    if not is_valid_address(address):
        return address
    return f"{address[:2 + chars]}...{address[-chars:]}"

def calculate_fee(gas_used: int, gas_price: int) -> int:
    """Calculate transaction fee in smallest units."""
    return gas_used * gas_price

def validate_amount(amount: float) -> bool:
    """Check if amount is positive and finite."""
    return amount > 0 and amount == amount  # not nan
