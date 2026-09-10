import os
from typing import Dict, Any, Final

# Network constants for wallet-utility-13
MAINNET_RPC: Final[str] = "https://mainnet.infura.io/v3/"
TESTNET_RPC: Final[str] = "https://sepolia.infura.io/v3/"

class WalletConfig:
    """Configuration management for crypto wallet operations."""

    def __init__(self, env: str = "production") -> None:
        self.env: str = env
        self.timeout: int = int(os.getenv("WALLET_TIMEOUT", 30))
        self.retry_limit: int = 3

    def get_rpc_url(self) -> str:
        """Selects appropriate RPC endpoint based on environment."""
        return MAINNET_RPC if self.env == "production" else TESTNET_RPC

    def to_dict(self) -> Dict[str, Any]:
        """Returns serialized configuration settings."""
        return {
            "environment": self.env,
            "timeout": self.timeout,
            "rpc": self.get_rpc_url(),
            "retry_limit": self.retry_limit
        }

def load_defaults() -> WalletConfig:
    """Factory function for default config instance."""
    return WalletConfig(env=os.getenv("APP_ENV", "production"))