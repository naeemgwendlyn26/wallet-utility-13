import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "rpc_url": "https://rpc.mainnet.cryptonode.com",
    "timeout": 30,
    "retry_attempts": 3
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass

    return config

def get_setting(key: str, default: Any = None) -> Any:
    """Retrieve specific setting from current runtime config."""
    config = load_config()
    return config.get(key, default)

if __name__ == "__main__":
    # Example usage for wallet-utility-13 initialization
    current_cfg = load_config()
    print(f"Loaded configuration for {current_cfg.get('network')}")