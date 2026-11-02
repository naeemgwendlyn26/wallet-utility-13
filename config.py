from typing import Dict, Any, Optional
import os

class Config:
    """Manages configuration settings for wallet-utility-13."""

    def __init__(self, env: str = "production") -> None:
        self.env: str = env
        self.settings: Dict[str, Any] = {
            "rpc_url": os.getenv("RPC_URL", "https://mainnet.infura.io/v3/default"),
            "timeout": int(os.getenv("TIMEOUT", 30)),
            "retry_attempts": 3
        }

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.settings.get(key, default)

    def update(self, key: str, value: Any) -> None:
        """Update a configuration setting."""
        self.settings[key] = value

def load_config() -> Config:
    """Factory function to initialize config object."""
    return Config(env=os.getenv("APP_ENV", "production"))

# Global config instance
app_config: Config = load_config()