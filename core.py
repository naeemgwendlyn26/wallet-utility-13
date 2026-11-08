import logging
import re

# Configure basic logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('wallet-utility-13')

def validate_address(address: str) -> bool:
    """Validate cryptocurrency address format (hex string)"""
    return bool(re.match(r'^0x[a-fA-F0-9]{40}$', address))

def process_transactions(queue: list):
    """
    Main processing loop for incoming transactions.
    Validates addresses before execution to ensure network security.
    """
    for tx in queue:
        address = tx.get('address')
        amount = tx.get('amount', 0)

        # Validation checks
        if not isinstance(address, str) or not validate_address(address):
            logger.error(f'invalid address format detected: {address}')
            continue

        if not isinstance(amount, (int, float)) or amount <= 0:
            logger.error(f'invalid amount for {address}: {amount}')
            continue

        # Process transaction logic
        logger.info(f'processing valid transaction: {address} -> {amount} ETH')

if __name__ == '__main__':
    sample_data = [
        {'address': '0x71C7656EC7ab88b098defB751B7401B5f6d8976F', 'amount': 1.5},
        {'address': 'invalid_addr', 'amount': 0.5},
        {'address': '0x71C7656EC7ab88b098defB751B7401B5f6d8976F', 'amount': -10}
    ]
    process_transactions(sample_data)