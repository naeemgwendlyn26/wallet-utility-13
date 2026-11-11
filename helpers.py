import re
from decimal import Decimal, ROUND_DOWN

SATOSHI_PER_BTC = Decimal("100000000")
WEI_PER_ETH = Decimal("1000000000000000000")


def satoshi_to_btc(satoshi: int) -> Decimal:
    """Convert Satoshi integer amount to Bitcoin Decimal."""
    if not isinstance(satoshi, int) or satoshi < 0:
        raise ValueError("Satoshi amount must be a non-negative integer")
    return (Decimal(satoshi) / SATOSHI_PER_BTC).quantize(
        Decimal("0.00000001"), rounding=ROUND_DOWN
    )


def btc_to_satoshi(btc_amount: str | float | Decimal) -> int:
    """Convert Bitcoin amount to Satoshi integer."""
    decimal_amount = Decimal(str(btc_amount))
    if decimal_amount < 0:
        raise ValueError("Bitcoin amount cannot be negative")
    return int(decimal_amount * SATOSHI_PER_BTC)


def wei_to_eth(wei: int) -> Decimal:
    """Convert Wei integer amount to Ether Decimal."""
    if not isinstance(wei, int) or wei < 0:
        raise ValueError("Wei amount must be a non-negative integer")
    return (Decimal(wei) / WEI_PER_ETH).quantize(
        Decimal("0.000000000000000001"), rounding=ROUND_DOWN
    )


def truncate_address(address: str, leading_chars: int = 6, trailing_chars: int = 4) -> str:
    """Format public crypto address for user display."""
    if not address or len(address) <= (leading_chars + trailing_chars):
        return address
    return f"{address[:leading_chars]}...{address[-trailing_chars:]}"
