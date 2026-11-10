import re
from decimal import Decimal, InvalidOperation
from typing import Union, Dict

# Unit conversion multipliers relative to base unit
ETH_UNITS = {
    "wei": Decimal("1"),
    "gwei": Decimal("1000000000"),
    "ether": Decimal("1000000000000000000"),
}

BTC_UNITS = {
    "satoshi": Decimal("1"),
    "btc": Decimal("100000000"),
}


def convert_crypto_unit(
    amount: Union[int, float, str, Decimal],
    from_unit: str,
    to_unit: str,
    chain: str = "eth"
) -> Decimal:
    """Convert value between different crypto denominations (e.g. Wei to Ether)."""
    units = ETH_UNITS if chain.lower() in ("eth", "ethereum") else BTC_UNITS
    from_u = from_unit.lower()
    to_u = to_unit.lower()

    if from_u not in units or to_u not in units:
        raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit} for chain '{chain}'")

    try:
        dec_amount = Decimal(str(amount))
    except (InvalidOperation, TypeError) as err:
        raise ValueError(f"Invalid amount provided: {amount}") from err

    # Convert to base unit first, then target unit
    base_value = dec_amount * units[from_u]
    return base_value / units[to_u]


def sanitize_wallet_address(address: str, chain: str = "eth") -> str:
    """Format and validate basic wallet address structure."""
    cleaned = address.strip()
    if chain.lower() in ("eth", "ethereum"):
        if not re.match(r"^0x[a-fA-F0-9]{40}$", cleaned):
            raise ValueError(f"Invalid Ethereum address format: {cleaned}")
        return cleaned.lower()
    elif chain.lower() in ("btc", "bitcoin"):
        if not re.match(r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,62}$", cleaned):
            raise ValueError(f"Invalid Bitcoin address format: {cleaned}")
        return cleaned
    raise ValueError(f"Unsupported chain: {chain}")


def format_tx_summary(tx_hash: str, amount: Decimal, symbol: str) -> Dict[str, str]:
    """Return a sanitized dictionary summary of a transaction."""
    short_hash = f"{tx_hash[:6]}...{tx_hash[-4:]}" if len(tx_hash) > 10 else tx_hash
    return {
        "hash_short": short_hash,
        "amount_formatted": f"{amount:.6f} {symbol.upper()}",
    }
