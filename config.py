import os
import logging

# Configure logger for wallet-utility-13
logger = logging.getLogger('wallet-utility')

def get_env_variable(key: str, default: str = None) -> str:
    """Retrieves environment variable with fallback and validation."""
    try:
        value = os.getenv(key)
        if value is None:
            if default is not None:
                return default
            raise EnvironmentError(f"Required config {key} is missing")
        return value
    except EnvironmentError as e:
        logger.critical(f"Configuration failure: {e}")
        raise

class WalletConfig:
    def __init__(self):
        try:
            self.rpc_url = get_env_variable("RPC_URL", "https://mainnet.infura.io/v3/default")
            self.timeout = int(get_env_variable("REQUEST_TIMEOUT", "30"))
            self.max_retries = int(get_env_variable("MAX_RETRIES", "3"))
        except ValueError as e:
            logger.error(f"Invalid configuration format: {e}")
            self.rpc_url = ""
            self.timeout = 30
            self.max_retries = 3

# Instantiate shared config
settings = WalletConfig()