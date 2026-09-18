import decimal
from typing import Union, Optional

def format_crypto_amount(amount: Union[int, float, str], decimals: int = 8) -> str:
    """Normalizes crypto amounts to string with fixed precision."""
    try:
        d_amount = decimal.Decimal(str(amount))
        return format(d_amount, f'.{decimals}f').rstrip('0').rstrip('.')
    except (decimal.InvalidOperation, ValueError):
        return "0"

def validate_address(address: str, chain_prefix: str = "0x") -> bool:
    """Checks basic crypto address formatting."""
    if not isinstance(address, str):
        return False
    return address.startswith(chain_prefix) and len(address) == 42

def wei_to_ether(wei: Union[int, str]) -> float:
    """Converts smallest unit to standard unit."""
    return float(decimal.Decimal(str(wei)) / decimal.Decimal("1000000000000000000"))

def calculate_fee(amount: float, fee_rate: float) -> float:
    """Calculates network transaction fee based on rate."""
    return round(amount * fee_rate, 10)