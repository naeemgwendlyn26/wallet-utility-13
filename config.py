import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "NETWORK": "mainnet",
    "RPC_URL": "https://eth-mainnet.public.blastapi.io",
    "TIMEOUT": 30,
    "RETRY_ATTEMPTS": 3
}

class ConfigLoader:
    """Handles application configuration with environment overrides."""
    
    def __init__(self, overrides: Dict[str, Any] = None):
        self._config = DEFAULT_CONFIG.copy()
        if overrides:
            self._config.update(overrides)
            
        # Override with environment variables if present
        for key in self._config.keys():
            env_val = os.getenv(f"WALLET_{key}")
            if env_val is not None:
                self._config[key] = self._cast_type(key, env_val)

    def _cast_type(self, key: str, value: str) -> Any:
        """Casts environment variables to match default types."""
        default_val = DEFAULT_CONFIG.get(key)
        if isinstance(default_val, int):
            return int(value)
        return value

    def get(self, key: str) -> Any:
        """Retrieves config value by key."""
        return self._config.get(key)

# Global config instance for application usage
settings = ConfigLoader()