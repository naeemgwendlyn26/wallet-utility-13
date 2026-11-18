import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "chain_id": 1,
    "timeout": 30,
    "gas_buffer": 0.1
}

def load_config() -> Dict[str, Any]:
    """Loads configuration from env or falls back to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    # Mapping of environment variables to config keys
    env_mapping = {
        "RPC_URL": "rpc_url",
        "CHAIN_ID": "chain_id",
        "TIMEOUT": "timeout",
        "GAS_BUFFER": "gas_buffer"
    }

    for env_var, key in env_mapping.items():
        value = os.getenv(env_var)
        if value:
            try:
                # Type inference based on default values
                expected_type = type(config[key])
                config[key] = expected_type(value)
            except (ValueError, TypeError):
                continue
    
    return config

# Instantiate active configuration
settings = load_config()