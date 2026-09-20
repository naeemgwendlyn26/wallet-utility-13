import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "NETWORK": "mainnet",
    "RPC_URL": "https://rpc.ankr.com/eth",
    "RETRY_ATTEMPTS": 3,
    "TIMEOUT_SECONDS": 30,
    "LOG_LEVEL": "INFO"
}

def load_config() -> Dict[str, Any]:
    """Loads configuration from environment variables with safe defaults."""
    config = DEFAULT_CONFIG.copy()
    
    # Override defaults with environment variables if present
    for key in config:
        env_value = os.getenv(key)
        if env_value is not None:
            # Attempt type casting based on default types
            expected_type = type(config[key])
            try:
                config[key] = expected_type(env_value)
            except (ValueError, TypeError):
                continue
                
    return config

# Instantiate active configuration
settings = load_config()