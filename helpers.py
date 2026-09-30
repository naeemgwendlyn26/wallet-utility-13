import decimal
from typing import Union

def format_crypto_amount(amount: Union[str, float, int], decimals: int = 8) -> str:
    """Format crypto balance to a string with fixed precision."""
    try:
        d_amount = decimal.Decimal(str(amount))
        quantizer = decimal.Decimal('1.' + '0' * decimals)
        formatted = d_amount.quantize(quantizer, rounding=decimal.ROUND_DOWN)
        return format(formatted, f'f')
    except (decimal.InvalidOperation, ValueError):
        return "0.00000000"

def calculate_tx_fee(amount: float, rate: float, min_fee: float = 0.0001) -> float:
    """Calculate transaction fee based on percentage rate and floor."""
    fee = amount * rate
    return max(fee, min_fee)

def validate_address_format(address: str, chain: str) -> bool:
    """Simple validator for address lengths per blockchain protocol."""
    patterns = {
        "BTC": (26, 35),
        "ETH": (42, 42)
    }
    if chain not in patterns:
        return True
    
    min_len, max_len = patterns[chain]
    return min_len <= len(address) <= max_len

def to_wei(amount: float) -> int:
    """Convert ETH denomination to Wei."""
    return int(decimal.Decimal(str(amount)) * decimal.Decimal(10**18))