import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables for wallet security
load_dotenv()

class Config:
    """Centralized configuration management for wallet-utility-13."""
    
    NETWORK_ENV = os.getenv('NETWORK_ENV', 'mainnet')
    TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', 30))
    RETRY_ATTEMPTS = 3
    
    @staticmethod
    def get_rpc_url() -> str:
        """Return the node provider URL based on environment."""
        return os.getenv(f'RPC_URL_{Config.NETWORK_ENV.upper()}', 'https://eth.llamarpc.com')

    @classmethod
    def to_dict(cls) -> Dict[str, Any]:
        """Export configuration as a dictionary for logging purposes."""
        return {
            'network': cls.NETWORK_ENV,
            'timeout': cls.TIMEOUT,
            'retries': cls.RETRY_ATTEMPTS,
            'rpc': cls.get_rpc_url()
        }

# Instantiate shared settings
settings = Config()