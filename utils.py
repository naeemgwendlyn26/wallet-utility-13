import re
from typing import Union

ETH_ADDRESS_PATTERN = re.compile(r"^0x[a-fA-F0-9]{40}$")


def is_valid_eth_address(address: str) -> bool:
    """Check if the given string matches standard Ethereum address format.

    Args:
        address: The wallet address string to validate.

    Returns:
        True if the string is a valid hex-encoded Ethereum address, False otherwise.
    """
    if not isinstance(address, str):
        return False
    return bool(ETH_ADDRESS_PATTERN.match(address))


def wei_to_ether(wei_amount: int) -> float:
    """Convert a balance from Wei to Ether.

    Args:
        wei_amount: The amount in Wei (1 Ether = 10^18 Wei).

    Returns:
        The converted value in Ether.

    Raises:
        ValueError: If the wei_amount is negative.
    """
    if wei_amount < 0:
        raise ValueError("Wei amount cannot be negative")
    return wei_amount / 10**18


def ether_to_wei(ether_amount: Union[int, float]) -> int:
    """Convert a balance from Ether to Wei.

    Args:
        ether_amount: The amount in Ether.

    Returns:
        The converted value in Wei as an integer.

    Raises:
        ValueError: If the ether_amount is negative.
    """
    if ether_amount < 0:
        raise ValueError("Ether amount cannot be negative")
    return int(ether_amount * 10**18)


def format_truncated_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Format a wallet address for compact UI displays (e.g., 0x1234...abcd).

    Args:
        address: The full wallet address string.
        prefix_len: Number of characters to keep at the start.
        suffix_len: Number of characters to keep at the end.

    Returns:
        Truncated address string with ellipses in the middle.
    """
    if len(address) <= prefix_len + suffix_len:
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"
