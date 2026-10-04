import logging
from typing import Dict, Any
from .core import CryptoWallet
from .exceptions import WalletError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('wallet-utility-13')

class WalletHandler:
    def __init__(self, config: Dict[str, Any]):
        self.wallet = CryptoWallet(config.get('api_key'))
        self.timeout = config.get('timeout', 30)

    def process_transaction(self, tx_data: Dict[str, Any]) -> Dict[str, Any]:
        """Executes and validates transaction cycles."""
        try:
            if not tx_data.get('address'):
                raise ValueError('Invalid destination address')
            
            result = self.wallet.execute(tx_data)
            logger.info(f"Transaction processed: {result.get('txid')}")
            return {"status": "success", "data": result}

        except WalletError as e:
            logger.error(f"Wallet operation failed: {e}")
            return {"status": "error", "message": str(e)}

    def get_status(self) -> Dict[str, bool]:
        return {"active": self.wallet.is_connected()}
