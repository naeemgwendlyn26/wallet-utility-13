import re

def satoshi_to_btc(satoshis: int) -> float:
    """Convert an amount in Satoshis to Bitcoin (BTC).

    Args:
        satoshis: The integer amount of Satoshis to convert.

    Returns:
        The equivalent amount in BTC as a float.
    """
    if satoshis < 0:
        raise ValueError("Satoshi amount cannot be negative.")
    return satoshis / 100_000_000.0

def btc_to_satoshi(btc: float) -> int:
    """Convert an amount in Bitcoin (BTC) to Satoshis.

    Args:
        btc: The float amount of BTC to convert.

    Returns:
        The equivalent amount in Satoshis as an integer.
    """
    if btc < 0:
        raise ValueError("BTC amount cannot be negative.")
    return round(btc * 100_000_000)

def is_valid_evm_address(address: str) -> bool:
    """Check if the given string is a valid Ethereum/EVM address format.

    This performs a basic hex validation and length check.

    Args:
        address: The string address to validate.

    Returns:
        True if the format matches a 40-character hex string prefixed with 0x.
    """
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))

def format_wallet_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Format a long wallet address into an abbreviated, user-friendly string.

    Args:
        address: The full wallet address string.
        prefix_len: Number of characters to preserve at the start.
        suffix_len: Number of characters to preserve at the end.

    Returns:
        The shortened address representation (e.g., 0x1f98...e15a).
    """
    if len(address) <= (prefix_len + suffix_len + 3):
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"