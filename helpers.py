"""Utility helper functions for crypto wallet operations."""

from typing import Optional, Dict, Any


def format_wei_to_ether(wei_amount: int) -> float:
    """Convert wei integer to ether float representation.

    Args:
        wei_amount: Amount in wei as an integer.

    Returns:
        Equivalent amount in ether as a float.
    """
    if wei_amount < 0:
        raise ValueError("Wei amount cannot be negative")
    return wei_amount / 10**18


def sanitize_address(wallet_address: str) -> str:
    """Validate and normalize a cryptocurrency wallet address.

    Args:
        wallet_address: Raw wallet address string.

    Returns:
        Normalized lowercase address string.
    """
    cleaned = wallet_address.strip().lower()
    if not cleaned.startswith("0x") or len(cleaned) != 42:
        raise ValueError("Invalid Ethereum address format")
    return cleaned


def build_tx_payload(to_address: str, value_wei: int, gas_limit: int = 21000) -> Dict[str, Any]:
    """Construct a standard transaction payload dictionary.

    Args:
        to_address: Recipient wallet address.
        value_wei: Amount to transfer in wei.
        gas_limit: Maximum gas units allowed for the transaction.

    Returns:
        Dictionary containing the formatted transaction parameters.
    """
    recipient = sanitize_address(to_address)
    return {
        "to": recipient,
        "value": value_wei,
        "gas": gas_limit,
    }
