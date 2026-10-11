import decimal
from typing import Union

def format_crypto_amount(amount: Union[str, float, int], precision: int = 8) -> decimal.Decimal:
    """Normalize crypto amounts to fixed precision decimal objects."""
    # Use context to prevent overflow or precision errors
    ctx = decimal.Context(prec=28, rounding=decimal.ROUND_HALF_UP)
    decimal.setcontext(ctx)
    
    try:
        val = decimal.Decimal(str(amount))
        return val.quantize(decimal.Decimal(10) ** -precision)
    except (decimal.InvalidOperation, ValueError):
        return decimal.Decimal('0.00000000')

def validate_address_format(address: str, chain_prefix: str = '0x') -> bool:
    """Basic validation for crypto wallet address strings."""
    if not address or len(address) < 26:
        return False
    
    # Check prefix requirement for EVM-style addresses
    if chain_prefix and not address.startswith(chain_prefix):
        return False
        
    # Verify hexadecimal characters only
    check_val = address[len(chain_prefix):] if chain_prefix else address
    return all(c in '0123456789abcdefABCDEF' for c in check_val)

def to_wei(amount: float) -> int:
    """Convert standard unit to smallest blockchain denomination."""
    return int(decimal.Decimal(str(amount)) * (10 ** 18))