import re

def validate_address(address: str) -> bool:
    """Validates Ethereum-like address format."""
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def validate_amount(amount: float) -> bool:
    """Ensures transaction amount is positive and within limits."""
    return isinstance(amount, (int, float)) and 0 < amount < 1000000

def process_transactions(transactions: list):
    """Main processing loop with integrated input validation."""
    results = []
    for tx in transactions:
        address = tx.get('to')
        amount = tx.get('value')

        if not validate_address(address):
            print(f"Invalid address format: {address}")
            continue

        if not validate_amount(amount):
            print(f"Invalid amount: {amount}")
            continue

        # Process validated transaction
        results.append({"status": "success", "tx": tx.get('id')})
    
    return results

if __name__ == '__main__':
    mock_data = [
        {'id': 1, 'to': '0x742d35Cc6634C0532925a3b844Bc454e4438f44e', 'value': 0.5},
        {'id': 2, 'to': 'invalid_addr', 'value': 10}
    ]
    processed = process_transactions(mock_data)
    print(f"Processed {len(processed)} transactions.")