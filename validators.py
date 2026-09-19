import re

def is_valid_ethereum_address(address: str) -> bool:
    """Validates standard hexadecimal Ethereum address format."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address))

def is_valid_amount(amount: str) -> bool:
    """Checks if amount string represents a positive decimal."""
    try:
        value = float(amount)
        return value > 0
    except (ValueError, TypeError):
        return False

def validate_transaction_payload(payload: dict) -> bool:
    """Verifies required keys for transaction execution."""
    required = {'to', 'from', 'value', 'data'}
    if not isinstance(payload, dict):
        return False
    return all(key in payload for key in required)

def is_valid_mnemonic(phrase: str) -> bool:
    """Validates basic BIP-39 mnemonic word count."""
    if not isinstance(phrase, str):
        return False
    words = phrase.strip().split()
    return len(words) in [12, 15, 18, 21, 24]