"""Cryptocurrency wallet utility functions for conversions and formatting."""

from typing import Union

WEI_PER_ETHER = 10**18
SATS_PER_BTC = 10**8


def wei_to_ether(wei: int) -> float:
    """Convert Wei (smallest Ethereum unit) to Ether."""
    if not isinstance(wei, int) or wei < 0:
        raise ValueError("Wei value must be a non-negative integer")
    return wei / WEI_PER_ETHER


def ether_to_wei(ether: Union[int, float]) -> int:
    """Convert Ether to Wei."""
    if not isinstance(ether, (int, float)) or ether < 0:
        raise ValueError("Ether value must be a non-negative number")
    return int(ether * WEI_PER_ETHER)


def sats_to_btc(sats: int) -> float:
    """Convert Satoshis to Bitcoin."""
    if not isinstance(sats, int) or sats < 0:
        raise ValueError("Satoshi value must be a non-negative integer")
    return sats / SATS_PER_BTC


def btc_to_sats(btc: Union[int, float]) -> int:
    """Convert Bitcoin to Satoshis."""
    if not isinstance(btc, (int, float)) or btc < 0:
        raise ValueError("BTC value must be a non-negative number")
    return int(btc * SATS_PER_BTC)


def format_hex_prefix(hex_str: str) -> str:
    """Ensure a hex string starts with '0x'."""
    cleaned = hex_str.strip()
    if not cleaned.startswith("0x") and not cleaned.startswith("0X"):
        return f"0x{cleaned}"
    return cleaned.lower()


def truncate_address(address: str, leading: int = 6, trailing: int = 4) -> str:
    """Truncate a wallet address for display purposes."""
    if len(address) <= leading + trailing:
        return address
    return f"{address[:leading]}...{address[-trailing:]}"
