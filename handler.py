import logging
from typing import Dict, Any
from core import WalletCore
from exceptions import WalletError

logger = logging.getLogger(__name__)

class WalletHandler:
    """Orchestrates wallet operations and request routing."""

    def __init__(self, core: WalletCore):
        self.core = core

    def process_transaction(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Executes internal transfer operations."""
        try:
            tx_id = self.core.execute_transfer(
                sender=request.get('from'),
                receiver=request.get('to'),
                amount=request.get('amount')
            )
            return {"status": "success", "tx_id": tx_id}
        except WalletError as e:
            logger.error(f"Transaction failed: {str(e)}")
            return {"status": "failed", "reason": str(e)}

    def get_balance(self, address: str) -> Dict[str, float]:
        """Fetches wallet balance from core service."""
        balance = self.core.fetch_balance(address)
        return {"address": address, "balance": balance}

    def handle_request(self, action: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Main routing entry point."""
        actions = {
            "transfer": self.process_transaction,
            "balance": lambda d: self.get_balance(d.get('address', ''))
        }

        if action not in actions:
            return {"status": "error", "message": "invalid action"}
            
        return actions[action](data)