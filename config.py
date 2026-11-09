import os
import json
from typing import Any, Dict

# Default configuration for wallet-utility-13
DEFAULT_CONFIG = {
    "rpc_url": "https://mainnet.infura.io/v3/",
    "timeout": 30,
    "retry_attempts": 3,
    "debug_mode": False
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file with fallback to defaults.
    """
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(config_path):
        return config

    try:
        with open(config_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        # Use defaults if file is corrupt or unreadable
        pass
        
    return config

if __name__ == "__main__":
    # Example usage for wallet-utility-13 node connectivity
    settings = load_config()
    print(f"Active RPC: {settings['rpc_url']}")