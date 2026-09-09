import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "rpc_url": "https://eth-mainnet.public.blastapi.io",
    "timeout": 30,
    "retry_attempts": 3
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file or returns defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

settings = load_config()