from typing import Dict, List, Any


def format_token_amount(raw_amount: int, decimals: int = 18) -> str:
    """Format raw integer token amount into decimal string representation."""
    if decimals < 0:
        raise ValueError("Decimals cannot be negative")

    str_amount = str(raw_amount).zfill(decimals + 1)
    integer_part = str_amount[:-decimals] or "0"
    fractional_part = str_amount[-decimals:].rstrip("0")

    if fractional_part:
        return f"{integer_part}.{fractional_part}"
    return integer_part


def normalize_tx_hash(tx_hash: str) -> str:
    """Standardize transaction hash with 0x prefix and lowercase formatting."""
    cleaned = tx_hash.strip()
    if not cleaned.startswith("0x"):
        cleaned = f"0x{cleaned}"
    return cleaned.lower()


def process_wallet_balance_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Process and format raw wallet balance records into structured output."""
    processed = []
    for item in data:
        symbol = item.get("symbol", "UNKNOWN").upper()
        decimals = int(item.get("decimals", 18))
        raw_balance = int(item.get("raw_balance", 0))
        address = item.get("token_address", "")

        processed.append({
            "symbol": symbol,
            "balance": format_token_amount(raw_balance, decimals),
            "decimals": decimals,
            "token_address": address.lower() if address else None,
            "raw_balance": raw_balance,
        })
    return processed
