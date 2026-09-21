import os
from typing import Final
from functools import lru_cache

# Performance constants for wallet-utility-13
# Using lru_cache for frequent configuration access

DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3
CACHE_SIZE: Final[int] = 128

@lru_cache(maxsize=CACHE_SIZE)
def get_network_config(network_id: str) -> dict:
    """Fetches and caches network parameters to reduce I/O overhead."""
    # Simulated configuration dictionary retrieval
    configs = {
        "mainnet": {"rpc": "https://mainnet.infura.io", "chain_id": 1},
        "testnet": {"rpc": "https://sepolia.infura.io", "chain_id": 11155111}
    }
    return configs.get(network_id, {})

# Environment overrides with standard defaults
API_KEY: Final[str] = os.getenv("WALLET_API_KEY", "default_key")
BATCH_SIZE: Final[int] = int(os.getenv("TX_BATCH_SIZE", "100"))

# Validation thresholds
MIN_GAS_LIMIT: Final[int] = 21000
MAX_GAS_LIMIT: Final[int] = 10000000