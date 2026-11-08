import re

class WalletValidationError(Exception):
    """Custom exception for wallet validation issues."""
    pass

def validate_address(address: str, chain_type: str = 'evm') -> bool:
    """Validates blockchain address format based on chain type."""
    if not isinstance(address, str) or not address:
        raise WalletValidationError("Address must be a non-empty string")

    patterns = {
        'evm': r'^0x[a-fA-F0-9]{40}$',
        'btc': r'^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,59}$'
    }

    if chain_type not in patterns:
        raise ValueError(f"Unsupported chain type: {chain_type}")

    if not re.match(patterns[chain_type], address):
        raise WalletValidationError(f"Invalid {chain_type} address format")

    return True

def validate_amount(amount: float) -> bool:
    """Ensures transaction amount is positive and finite."""
    try:
        val = float(amount)
        if val <= 0:
            raise WalletValidationError("Amount must be greater than zero")
        return True
    except (ValueError, TypeError):
        raise WalletValidationError("Amount must be a numeric value")