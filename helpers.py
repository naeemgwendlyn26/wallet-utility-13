from decimal import Decimal, ROUND_DOWN
from typing import Union


def format_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Truncate a crypto address for display purposes (e.g., 0x1234...abcd)."""
    if not address or len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def wei_to_ether(wei_value: Union[int, str]) -> Decimal:
    """Convert value from Wei to Ether with exact precision."""
    wei = Decimal(str(wei_value))
    return wei / (Decimal("10") ** 18)


def ether_to_wei(ether_value: Union[float, str, Decimal]) -> int:
    """Convert value from Ether to Wei as integer."""
    ether = Decimal(str(ether_value))
    return int(ether * (Decimal("10") ** 18))


def format_crypto_balance(
    amount: Union[int, float, str, Decimal],
    decimals: int = 18,
    display_decimals: int = 4
) -> str:
    """Format token balance with decimals and specified display precision."""
    val = Decimal(str(amount)) / (Decimal("10") ** decimals)
    quantizer = Decimal("10") ** -display_decimals
    formatted = val.quantize(quantizer, rounding=ROUND_DOWN)
    return f"{formatted:f}"


def satoshi_to_btc(sats: int) -> Decimal:
    """Convert Satoshis to Bitcoin."""
    return Decimal(sats) / (Decimal("10") ** 8)
