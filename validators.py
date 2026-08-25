import re
from typing import Optional, Dict, Any

def validate_bitcoin_address(address: str) -> bool:
    """Validate a Bitcoin address.
    Args:
        address: The address string.
    Returns:
        True if valid.
    """
    if not isinstance(address, str) or len(address) < 26:
        return False
    pattern = r'^(1|3)[a-km-zA-HJ-NP-Z1-9]{25,34}$'
    return bool(re.match(pattern, address))

def validate_ethereum_address(address: str) -> bool:
    """Validate an Ethereum address.
    Args:
        address: The address string.
    Returns:
        True if valid.
    """
    if not isinstance(address, str) or not address.startswith('0x') or len(address) != 42:
        return False
    hex_part = address[2:].lower()
    return all(c in '0123456789abcdef' for c in hex_part)

def validate_private_key(private_key: str) -> bool:
    """Validate a private key.
    Args:
        private_key: Hex string.
    Returns:
        True if valid.
    """
    if not isinstance(private_key, str) or len(private_key) != 64:
        return False
    try:
        int(private_key, 16)
        return True
    except ValueError:
        return False

def validate_amount(amount: float, minimum: Optional[float] = 0.0001) -> bool:
    """Validate transaction amount.
    Args:
        amount: Amount value.
        minimum: Min allowed.
    Returns:
        True if ok.
    """
    return isinstance(amount, (int, float)) and amount >= minimum

def get_validator(name: str) -> Optional[Any]:
    """Get a validator by name.
    Args:
        name: Validator name.
    Returns:
        Function or None.
    """
    validators: Dict[str, Any] = {
        'bitcoin': validate_bitcoin_address,
        'ethereum': validate_ethereum_address,
        'private_key': validate_private_key,
        'amount': validate_amount
    }
    return validators.get(name)