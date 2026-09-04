import decimal
from typing import Union

def format_crypto(amount: Union[int, float, str], precision: int = 8) -> str:
    """Converts raw crypto amounts to string with fixed decimal precision."""
    quantizer = decimal.Decimal('1.' + '0' * precision)
    value = decimal.Decimal(str(amount))
    return str(value.quantize(quantizer, rounding=decimal.ROUND_HALF_UP))

def validate_address(address: str, prefix: str = '0x') -> bool:
    """Basic hex address validation for EVM-based assets."""
    if not address.startswith(prefix):
        return False
    return len(address) == 42 and all(c in '0123456789abcdefABCDEF' for c in address[2:])

def wei_to_ether(wei: int) -> float:
    """Converts smallest unit to base asset."""
    return float(wei) / 10**18

def ether_to_wei(ether: float) -> int:
    """Converts base asset to smallest unit."""
    return int(decimal.Decimal(str(ether)) * 10**18)

def sanitize_tx_hash(tx_hash: str) -> str:
    """Normalizes transaction hash formatting."""
    return tx_hash.lower().strip()