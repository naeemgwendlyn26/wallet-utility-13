import os
import json
from typing import Any, Dict

class ConfigLoader:
    """Handles application configuration with fallback defaults."""
    
    DEFAULT_CONFIG = {
        "rpc_url": "https://mainnet.infura.io/v3/",
        "timeout": 30,
        "retries": 3,
        "verify_ssl": True
    }

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.settings = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads config from file or returns defaults if missing."""
        if not os.path.exists(self.config_path):
            return self.DEFAULT_CONFIG

        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
            return {**self.DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return self.DEFAULT_CONFIG

    def get(self, key: str, default: Any = None) -> Any:
        """Access configuration keys safely."""
        return self.settings.get(key, default)

# Instantiate global config for the wallet-utility-13 module
config = ConfigLoader()