import re
from typing import Any, Dict, Optional

def validate_wallet_address(address: str) -> bool:
    """Validate cryptocurrency address format."""
    if not isinstance(address, str) or len(address) < 26 or len(address) > 35:
        return False
    return bool(re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address))

def validate_transaction_payload(payload: Dict[str, Any]) -> Optional[str]:
    """Verify structure and values of transaction data."""
    required_fields = ['sender', 'recipient', 'amount']
    
    for field in required_fields:
        if field not in payload:
            return f'missing field: {field}'
            
    if not isinstance(payload['amount'], (int, float)) or payload['amount'] <= 0:
        return 'invalid transaction amount'
        
    if not validate_wallet_address(payload['sender']) or not validate_wallet_address(payload['recipient']):
        return 'invalid wallet address format'
        
    return None

def sanitize_input(data: str) -> str:
    """Remove dangerous characters from user input."""
    return re.sub(r'[^a-zA-Z0-9]', '', data)