import os
import logging
from typing import Dict, Any

class ConfigError(Exception):
    """Custom exception for wallet configuration failures."""
    pass

def load_wallet_config() -> Dict[str, Any]:
    """Load and validate environment configurations."""
    required_vars = ['RPC_URL', 'WALLET_ADDRESS', 'NETWORK_ID']
    config = {}

    try:
        for var in required_vars:
            value = os.getenv(var)
            if not value:
                raise ConfigError(f"Missing required environment variable: {var}")
            config[var] = value
            
        # Validate network identifier format
        if not config['NETWORK_ID'].isdigit():
            raise ConfigError("NETWORK_ID must be a numeric string")
            
    except ConfigError as e:
        logging.error(f"Configuration failure: {e}")
        raise
    except Exception as e:
        logging.critical(f"Unexpected configuration error: {e}")
        raise ConfigError("Internal configuration load failure") from e

    return config

# Initialize global configuration safely
try:
    SETTINGS = load_wallet_config()
except ConfigError:
    SETTINGS = {}
    logging.warning("Wallet utility running in unconfigured state")