import re
from decimal import Decimal
from typing import Union, Dict, Any, Optional

WEI_PER_ETH = Decimal("1000000000000000000")
SATOSHI_PER_BTC = Decimal("100000000")


def wei_to_eth(wei_amount: Union[int, str, Decimal]) -> Decimal:
    """Convert an amount in Wei to Ether.

    Args:
        wei_amount: The balance in Wei as integer, string, or Decimal.

    Returns:
        The equivalent amount in Ether as Decimal.
    """
    amount = Decimal(str(wei_amount))
    return amount / WEI_PER_ETH


def eth_to_wei(eth_amount: Union[float, str, Decimal]) -> int:
    """Convert an amount in Ether to Wei.

    Args:
        eth_amount: The balance in Ether as float, string, or Decimal.

    Returns:
        The equivalent amount in Wei as an integer.
    """
    amount = Decimal(str(eth_amount))
    return int(amount * WEI_PER_ETH)


def format_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Truncate a crypto address for user interface display.

    Args:
        address: The full wallet address string.
        prefix_len: Number of characters to keep at the start.
        suffix_len: Number of characters to keep at the end.

    Returns:
        Shortened address with ellipsis in the middle, or original if short.
    """
    if not address:
        return ""
    min_len = prefix_len + suffix_len + 3
    if len(address) <= min_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def validate_hex_address(address: str, expected_length: int = 42) -> bool:
    """Check if a string is a valid hex crypto address.

    Args:
        address: The wallet address to validate.
        expected_length: Expected total length including '0x' prefix.

    Returns:
        True if the address is valid hex with matching length.
    """
    if not isinstance(address, str):
        return False
    pattern = f"^0x[a-fA-F0-9]{{{expected_length - 2}}}$"
    return bool(re.match(pattern, address))
