import re
from typing import Union


class WalletError(Exception):
    """Base exception class for wallet utility errors."""
    pass


class InvalidAddressError(WalletError):
    """Raised when a cryptocurrency address is invalid."""
    pass


class ConversionError(WalletError):
    """Raised when unit conversion fails or exceeds bounds."""
    pass


def validate_eth_address(address: str) -> str:
    """Validate and normalize an Ethereum hex address."""
    if not isinstance(address, str):
        raise InvalidAddressError("Address must be a string")

    clean_address = address.strip()
    if not clean_address:
        raise InvalidAddressError("Address cannot be empty")

    if not re.match(r"^0x[a-fA-F0-9]{40}$", clean_address):
        raise InvalidAddressError(f"Invalid Ethereum address format: '{address}'")

    return clean_address.lower()


def safe_from_wei(amount_wei: Union[int, str], decimals: int = 18) -> float:
    """Convert Wei to standard token unit with edge-case handling."""
    if not isinstance(decimals, int) or decimals < 0 or decimals > 36:
        raise ConversionError("Decimals must be an integer between 0 and 36")

    try:
        if isinstance(amount_wei, str):
            clean_str = amount_wei.strip()
            if clean_str.startswith("0x") or clean_str.startswith("0X"):
                int_val = int(clean_str, 16)
            else:
                int_val = int(clean_str)
        elif isinstance(amount_wei, int):
            int_val = amount_wei
        else:
            raise ConversionError(f"Unsupported type for amount: {type(amount_wei).__name__}")

        if int_val < 0:
            raise ConversionError("Token amount cannot be negative")

        return int_val / (10 ** decimals)
    except ValueError as err:
        raise ConversionError(f"Failed to parse Wei amount: {err}") from err
    except OverflowError as err:
        raise ConversionError("Value exceeds numerical bounds") from err
