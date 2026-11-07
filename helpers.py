import re
from typing import Optional, Union


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    """Safely truncate a crypto address for UI display with edge-case handling."""
    if not isinstance(address, str):
        raise TypeError("Address must be a string")
    
    cleaned = address.strip()
    if not cleaned:
        return ""
    
    min_length = leading + trailing + 3
    if len(cleaned) <= min_length:
        return cleaned
    
    return f"{cleaned[:leading]}...{cleaned[-trailing:]}"


def satoshis_to_btc(satoshis: Union[int, float, str, None]) -> float:
    """Convert Satoshis to BTC value, handling invalid types and bounds edge cases."""
    if satoshis is None:
        return 0.0
    
    try:
        val = float(satoshis)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid satoshi value format: {satoshis}")
    
    if val < 0:
        raise ValueError("Satoshi amount cannot be negative")
    
    # Max supply guard: 21 million BTC in satoshis
    if val > 2.1e15:
        raise ValueError("Amount exceeds theoretical maximum Bitcoin supply")
    
    return round(val / 1e8, 8)


def parse_hex_balance(hex_str: Union[str, int]) -> int:
    """Parse RPC hex balance string into wei integer with safety checks."""
    if isinstance(hex_str, int):
        return hex_str if hex_str >= 0 else 0

    if not isinstance(hex_str, str):
        raise TypeError("Hex balance must be a string or integer")

    cleaned = hex_str.strip().lower()
    if not cleaned:
        return 0

    if cleaned.startswith("0x"):
        cleaned = cleaned[2:]

    if not cleaned:
        return 0

    if not re.fullmatch(r"[0-9a-f]+", cleaned):
        raise ValueError(f"Invalid hexadecimal characters in balance: '{hex_str}'")

    return int(cleaned, 16)
