import re
from typing import Optional

SATOSHI_PER_BTC = 100_000_000


def satoshi_to_btc(sats: int) -> float:
    """Convert integer satoshis to Bitcoin float value."""
    if sats < 0:
        raise ValueError("Satoshi amount cannot be negative")
    return sats / SATOSHI_PER_BTC


def btc_to_satoshi(btc: float) -> int:
    """Convert Bitcoin float value to integer satoshis."""
    if btc < 0:
        raise ValueError("BTC amount cannot be negative")
    return round(btc * SATOSHI_PER_BTC)


def format_address_short(address: str, leading: int = 6, trailing: int = 4) -> str:
    """Shorten a public wallet address for visual display."""
    if not address or len(address) <= (leading + trailing):
        return address
    return f"{address[:leading]}...{address[-trailing:]}"


def is_valid_hex_string(val: str, length: Optional[int] = None) -> bool:
    """Check if string is valid hex with optional exact length check."""
    clean_val = val[2:] if val.startswith("0x") else val
    if length and len(clean_val) != length:
        return False
    return bool(re.fullmatch(r"[0-9a-fA-F]+", clean_val))
