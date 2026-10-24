import decimal
from typing import Union


def satoshi_to_btc(sats: int) -> decimal.Decimal:
    """Convert satoshis to BTC decimal value."""
    if sats < 0:
        raise ValueError("Satoshi amount cannot be negative")
    return (decimal.Decimal(sats) / decimal.Decimal(10**8)).normalize()


def btc_to_satoshi(btc: Union[float, str, decimal.Decimal]) -> int:
    """Convert BTC value to satoshis."""
    btc_dec = decimal.Decimal(str(btc))
    if btc_dec < 0:
        raise ValueError("BTC amount cannot be negative")
    return int(btc_dec * decimal.Decimal(10**8))


def wei_to_eth(wei: int) -> decimal.Decimal:
    """Convert Wei to ETH decimal value."""
    if wei < 0:
        raise ValueError("Wei amount cannot be negative")
    return (decimal.Decimal(wei) / decimal.Decimal(10**18)).normalize()


def truncate_address(address: str, prefix_len: int = 6, suffix_len: int = 4) -> str:
    """Truncate a crypto wallet address for UI display."""
    if not address:
        return ""
    if len(address) <= (prefix_len + suffix_len):
        return address
    return f"{address[:prefix_len]}...{address[-suffix_len:]}"


def format_fiat(amount: Union[float, decimal.Decimal], currency: str = "USD") -> str:
    """Format numerical amount into standardized fiat representation."""
    val = decimal.Decimal(str(amount))
    symbols = {"USD": "$", "EUR": "€", "GBP": "£"}
    symbol = symbols.get(currency.upper(), f"{currency.upper()} ")
    return f"{symbol}{val:,.2f}"
