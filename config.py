import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "rpc_url": "https://rpc.ankr.com/eth",
    "timeout": 30,
    "retry_attempts": 3
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def get_setting(key: str, default: Any = None) -> Any:
    """Retrieves specific setting from loaded config."""
    config = load_config()
    return config.get(key, default)

if __name__ == "__main__":
    current_config = load_config()
    print(f"Loaded network: {current_config['network']}")