import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "network": "mainnet",
    "timeout": 30,
    "retry_attempts": 3,
    "rpc_url": "https://api.mainnet.node"
}

class ConfigLoader:
    """Utility for loading and merging wallet configurations."""
    
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.settings = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Loads config from file if present, else defaults."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    file_config = json.load(f)
                    self.settings.update(file_config)
            except (json.JSONDecodeError, IOError):
                pass
        return self.settings

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a single setting value."""
        return self.settings.get(key, default)

# Instantiate global config for application use
loader = ConfigLoader()
settings = loader.load()