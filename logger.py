import logging
from typing import Optional


class WalletLogger:
    """Structured logger tailored for crypto wallet utility operations."""

    def __init__(self, name: str = "wallet_utility", level: int = logging.INFO) -> None:
        """Initialize the logger with standard formatting."""
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)

        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    @staticmethod
    def mask_address(address: str) -> str:
        """Mask a wallet address or sensitive hash for safe logging."""
        if not address or len(address) < 10:
            return "***"
        return f"{address[:6]}...{address[-4:]}"

    def log_tx(self, tx_hash: str, status: str, amount: Optional[float] = None) -> None:
        """Log a cryptocurrency transaction event with sanitized output."""
        masked_hash = self.mask_address(tx_hash)
        if amount is not None:
            msg = f"Tx {masked_hash} | Status: {status} | Amount: {amount:.4f}"
        else:
            msg = f"Tx {masked_hash} | Status: {status}"
        self.logger.info(msg)

    def info(self, message: str) -> None:
        """Log an informational message."""
        self.logger.info(message)

    def error(self, message: str, exc: Optional[Exception] = None) -> None:
        """Log an error message with optional exception details."""
        if exc:
            self.logger.error(f"{message} - Error: {exc}")
        else:
            self.logger.error(message)
