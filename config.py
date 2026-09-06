import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "rpc_url": "https://api.mainnet-beta.solana.com",
    "timeout": 30,
    "retry_attempts": 3
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with fallback defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def get_config_value(key: str, default: Any = None) -> Any:
    """Retrieves specific config value from environment or file."""
    env_val = os.getenv(f"WALLET_{key.upper()}")
    if env_val:
        return env_val
    
    config = load_config()
    return config.get(key, default)