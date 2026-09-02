import time
import random
from typing import Callable, Any, Type

def retry_on_network_error(
    operation: Callable[[], Any],
    max_retries: int = 3,
    base_delay: float = 1.0,
) -> Any:
    """Retry network operations with exponential backoff and jitter.

    Used for crypto API calls like balance queries or transaction broadcasts.
    """
    last_exception = None
    for attempt in range(max_retries):
        try:
            return operation()
        except (ConnectionError, TimeoutError, OSError) as e:
            last_exception = e
            if attempt == max_retries - 1:
                break
            # Exponential backoff with jitter
            delay = base_delay * (2 ** attempt) + random.uniform(0, 0.5)
            time.sleep(delay)
    raise RuntimeError(f"Network operation failed after {max_retries} retries") from last_exception

# Practical example for wallet utility
def query_blockchain(address: str) -> dict:
    """Simulate a network call to fetch crypto wallet data."""
    # Real implementation would use web3.py or requests to RPC endpoint
    if random.random() < 0.6:
        raise ConnectionError("Failed to connect to Ethereum node")
    return {"address": address, "balance": "1.5", "transactions": 42}

def get_wallet_data(address: str) -> dict:
    """Fetch wallet data with built-in retry logic."""
    return retry_on_network_error(lambda: query_blockchain(address))

if __name__ == "__main__":
    test_address = "0x1234567890abcdef1234567890abcdef12345678"
    try:
        data = get_wallet_data(test_address)
        print(f"Wallet data: {data}")
    except RuntimeError as e:
        print(f"Failed to get data: {e}")