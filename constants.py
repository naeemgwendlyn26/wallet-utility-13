"""Constants for wallet-utility-13 crypto wallet operations."""

import os

from typing import Dict, Any

# Blockchain networks configuration
SUPPORTED_NETWORKS: Dict[str, Dict[str, Any]] = {
    "ethereum": {
        "chain_id": 1,
        "rpc_url": "https://mainnet.infura.io/v3/YOUR_PROJECT_ID",
        "explorer_url": "https://etherscan.io",
        "native_currency": "ETH",
    },
    "bsc": {
        "chain_id": 56,
        "rpc_url": "https://bsc-dataseed.binance.org",
        "explorer_url": "https://bscscan.com",
        "native_currency": "BNB",
    },
    "polygon": {
        "chain_id": 137,
        "rpc_url": "https://polygon-rpc.com",
        "explorer_url": "https://polygonscan.com",
        "native_currency": "MATIC",
    },
}

# Stablecoin contract addresses
STABLECOIN_ADDRESSES: Dict[str, Dict[str, str]] = {
    "usdt": {
        "ethereum": "0xdac17f958d2ee523a2206206994597c13d831ec7",
        "bsc": "0x55d398326f99059ff775485246999027b3197955",
        "polygon": "0xc2132d05d31c914a87c6611c10748aeb04b58e8f",
    },
    "usdc": {
        "ethereum": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
        "bsc": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
        "polygon": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
    },
}

# External API endpoints
API_ENDPOINTS = {
    "coingecko": "https://api.coingecko.com/api/v3",
    "gas_station": "https://ethgasstation.info/json",
}

# Default operation parameters
DEFAULT_GAS_LIMIT = 21000
TX_TIMEOUT_SECONDS = 60
MAX_RETRY_ATTEMPTS = 5
MINIMUM_BALANCE = 0.01

# Runtime configuration from environment
IS_DEBUG = os.getenv("WALLET_DEBUG", "0") == "1"

# Wallet error mappings
ERROR_MESSAGES: Dict[str, str] = {
    "insufficient_funds": "Not enough balance to complete transaction",
    "invalid_address": "Wallet address is not valid",
    "network_error": "Failed to connect to blockchain network",
    "timeout": "Operation timed out after waiting period",
}