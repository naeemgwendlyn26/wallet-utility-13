"""Utility functions for crypto wallet data formatting and conversions."""

from decimal import Decimal
import re


def wei_to_eth(wei_amount: int) -> Decimal:
    """Convert Wei integer to Ether Decimal value."""
    return Decimal(wei_amount) / Decimal(10**18)


def eth_to_wei(eth_amount: float | str | Decimal) -> int:
    """Convert Ether value to Wei integer."""
    return int(Decimal(str(eth_amount)) * Decimal(10**18))


def satoshi_to_btc(satoshi: int) -> Decimal:
    """Convert Satoshi integer to Bitcoin Decimal value."""
    return Decimal(satoshi) / Decimal(10**8)


def btc_to_satoshi(btc_amount: float | str | Decimal) -> int:
    """Convert Bitcoin value to Satoshi integer."""
    return int(Decimal(str(btc_amount)) * Decimal(10**8))


def format_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Truncate crypto address for safe UI display (e.g., 0x1234...abcd)."""
    if not address or len(address) <= (prefix_len + suffix_len):
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def is_hex_string(val: str) -> bool:
    """Check if a string is a valid hexadecimal string."""
    clean_val = val[2:] if val.startswith(("0x", "0X")) else val
    return bool(re.fullmatch(r"[0-9a-fA-F]+", clean_val)) if clean_val else False
