import re
from decimal import Decimal, InvalidOperation
from typing import Union


class WalletValidationError(Exception):
    """Raised when wallet input validation fails."""
    pass


def parse_satoshi_amount(val: Union[str, int, float, Decimal]) -> int:
    """
    Converts a crypto amount to satoshis safely.
    Handles edge cases like scientific notation, negative values, and precision loss.
    """
    try:
        d = Decimal(str(val))
    except (InvalidOperation, TypeError) as err:
        raise WalletValidationError(f"Invalid numeric input format: {val}") from err

    if d.is_nan() or d.is_infinite():
        raise WalletValidationError("Amount cannot be NaN or Infinite")

    if d <= Decimal('0'):
        raise WalletValidationError("Transaction amount must be strictly positive")

    satoshis = d * Decimal('100000000')
    if satoshis != satoshis.quantize(Decimal('1')):
        raise WalletValidationError("Amount exceeds maximum precision (8 decimal places)")

    return int(satoshis)


def validate_hex_address(address: str, expected_length: int = 42) -> str:
    """
    Validates standard hex addresses against edge cases like missing prefixes and bad lengths.
    """
    if not isinstance(address, str):
        raise WalletValidationError("Address must be a string")

    clean_addr = address.strip()
    if not clean_addr:
        raise WalletValidationError("Address string cannot be empty")

    if not clean_addr.startswith("0x"):
        clean_addr = f"0x{clean_addr}"

    if len(clean_addr) != expected_length:
        raise WalletValidationError(
            f"Invalid address length: expected {expected_length}, got {len(clean_addr)}"
        )

    if not re.match(r"^0x[a-fA-F0-9]+$", clean_addr):
        raise WalletValidationError("Address contains non-hexadecimal characters")

    return clean_addr.lower()
