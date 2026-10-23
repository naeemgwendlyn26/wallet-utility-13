import logging
import sys
from typing import Optional

class WalletLogger:
    """Centralized logging for crypto operations with exception handling."""
    def __init__(self, name: str = "wallet-utility-13"):
        self.logger = logging.getLogger(name)
        self._setup_logger()

    def _setup_logger(self) -> None:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_error(self, message: str, exc: Optional[Exception] = None) -> None:
        """Sanitized error logging for crypto-sensitive flows."""
        if exc:
            error_type = type(exc).__name__
            self.logger.error(f"{message} | Error: {error_type} | Details: {str(exc)}")
        else:
            self.logger.error(message)

    def log_tx_failure(self, tx_hash: str, reason: str) -> None:
        """Standardized logging for blockchain transaction edge cases."""
        if not tx_hash:
            self.logger.warning("Attempted to log transaction failure with empty hash")
            return
        self.logger.error(f"Transaction failed: {tx_hash} | Reason: {reason}")