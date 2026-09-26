import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "rpc_url": "https://rpc.ankr.com/eth"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load config file: {e}. Using defaults.")
    
    return config

def get_config_value(key: str, default: Any = None) -> Any:
    """Helper for accessing specific config keys."""
    config = load_config()
    return config.get(key, default)

if __name__ == "__main__":
    current_config = load_config()
    print(f"Loaded wallet configuration: {current_config}")