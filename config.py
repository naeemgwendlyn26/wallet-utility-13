import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "rpc_url": "https://cloudflare-eth.com",
    "timeout": 30,
    "retry_attempts": 3
}

class ConfigLoader:
    """Handles loading and merging of crypto wallet configurations."""
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.data = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            return DEFAULT_CONFIG
        
        try:
            with open(self.config_path, "r") as f:
                user_config = json.load(f)
                # Merge user config with defaults
                return {**DEFAULT_CONFIG, **user_config}
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.data.get(key, default)

# Singleton instance for application-wide use
settings = ConfigLoader()