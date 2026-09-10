import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass(frozen=True)
class WalletConfig:
    network: str
    rpc_url: str
    timeout: int

def load_config() -> WalletConfig:
    """Initialize application configuration from environment variables."""
    return WalletConfig(
        network=os.getenv("WALLET_NETWORK", "mainnet"),
        rpc_url=os.getenv("RPC_ENDPOINT", "https://api.mainnet.network"),
        timeout=int(os.getenv("REQUEST_TIMEOUT", "30"))
    )

# Global config singleton
settings = load_config()

# Network constants
SUPPORTED_NETWORKS = {
    "mainnet": "https://mainnet.infura.io",
    "testnet": "https://sepolia.infura.io"
}

def get_provider_url(network_name: str) -> str:
    """Retrieve RPC URL for a specific network."""
    return SUPPORTED_NETWORKS.get(network_name, settings.rpc_url)