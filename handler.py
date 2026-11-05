import logging

logger = logging.getLogger(__name__)

class WalletError(Exception):
    """Base exception for wallet operations."""
    pass

def execute_transaction(tx_func, *args, **kwargs):
    """Wraps execution to catch common crypto failures."""
    try:
        return tx_func(*args, **kwargs)
    except ConnectionError as e:
        logger.error(f"Network connectivity failure: {e}")
        raise WalletError("Unable to reach node provider") from e
    except ValueError as e:
        logger.error(f"Invalid transaction parameters: {e}")
        raise WalletError("Malformed transaction data") from e
    except Exception as e:
        logger.critical(f"Unexpected system error: {e}")
        raise WalletError("Internal wallet processing failure") from e

def validate_address(address: str, chain: str) -> bool:
    """Ensures address formatting matches chain requirements."""
    if not address or not isinstance(address, str):
        return False
    
    # Basic hex-string format check for EVM-compatible wallets
    if chain == "evm":
        return address.startswith("0x") and len(address) == 42
    
    return False