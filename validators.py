import re

def is_valid_address(address: str, chain: str = 'eth') -> bool:
    """Validate cryptocurrency address format for supported chains."""
    patterns = {
        'eth': r'^0x[a-fA-F0-9]{40}$',
        'btc': r'^(1|3|bc1)[a-zA-Z0-9]{25,39}$',
        'sol': r'^[1-9A-HJ-NP-Za-km-z]{32,44}$'
    }
    
    pattern = patterns.get(chain.lower())
    if not pattern:
        raise ValueError(f"Unsupported chain: {chain}")
        
    return bool(re.match(pattern, address))

def sanitize_amount(amount: str) -> float:
    """Normalize string input to float for ledger operations."""
    try:
        cleaned = re.sub(r'[^0-9.]', '', str(amount))
        return float(cleaned)
    except (ValueError, TypeError):
        return 0.0

def validate_transaction_payload(data: dict) -> bool:
    """Ensure required fields exist in transaction dictionary."""
    required = {'sender', 'recipient', 'amount', 'currency'}
    return all(key in data for key in required)

if __name__ == '__main__':
    # Example usage for testing
    test_addr = "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"
    print(f"Valid ETH address: {is_valid_address(test_addr, 'eth')}")