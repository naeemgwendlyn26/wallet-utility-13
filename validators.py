import re
from typing import Optional

def is_valid_ethereum_address(address: str) -> bool:
    """Validate standard Ethereum address format."""
    if not isinstance(address, str):
        return False
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def is_valid_bitcoin_address(address: str) -> bool:
    """Validate common Bitcoin address formats (legacy, segwit)."""
    if not isinstance(address, str):
        return False
    # Regex for P2PKH, P2SH, and Bech32
    regex = r'^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-zA-HJ-NP-Z0-9]{25,59})$'
    return bool(re.match(regex, address))

def sanitize_amount(amount: str) -> Optional[float]:
    """Parse and sanitize decimal string inputs."""
    try:
        value = float(amount)
        return value if value >= 0 else None
    except (ValueError, TypeError):
        return None

def validate_transaction_payload(data: dict) -> bool:
    """Verify structure of crypto transaction request."""
    required = {'sender', 'receiver', 'amount', 'currency'}
    if not isinstance(data, dict) or not required.issubset(data.keys()):
        return False
    
    if data['currency'].upper() == 'ETH':
        return is_valid_ethereum_address(data['receiver'])
    elif data['currency'].upper() == 'BTC':
        return is_valid_bitcoin_address(data['receiver'])
    
    return False