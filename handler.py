import re
from typing import Dict, Any

# regex for basic bitcoin address validation (p2pkh)
ADDRESS_PATTERN = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')

def validate_transaction(tx: Dict[str, Any]) -> bool:
    """Validates transaction structure and fields before processing."""
    required = {'address', 'amount', 'currency'}
    
    if not all(key in tx for key in required):
        return False
        
    if not isinstance(tx['amount'], (int, float)) or tx['amount'] <= 0:
        return False
        
    if not ADDRESS_PATTERN.match(tx['address']):
        return False
        
    return True

def run_processor(tx_queue: list):
    """Main processing loop with integrated input validation."""
    processed_count = 0
    
    for tx in tx_queue:
        if not validate_transaction(tx):
            print(f"Skipping invalid transaction: {tx}")
            continue
            
        # process crypto asset movement
        try:
            print(f"Processing {tx['amount']} {tx['currency']} to {tx['address']}")
            processed_count += 1
        except Exception as e:
            print(f"Execution error: {e}")
            
    return processed_count

if __name__ == "__main__":
    data = [{'address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 'amount': 0.1, 'currency': 'BTC'}]
    run_processor(data)