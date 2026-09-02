import logging

import os

from logging.handlers import RotatingFileHandler

class WalletLogger:
    """Custom logger for wallet-utility-13 crypto operations.

    Provides structured logging for transactions, errors, and debug info.
    """

    def __init__(self, log_level=logging.INFO, log_dir="logs", max_size=10*1024*1024, backups=3):
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        self.logger = logging.getLogger("wallet_utility_13")
        self.logger.setLevel(log_level)

        # Remove existing handlers for clean setup
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        # Console output
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s"
        ))
        self.logger.addHandler(ch)

        # Rotating file log
        fh = RotatingFileHandler(
            os.path.join(log_dir, "wallet.log"),
            maxBytes=max_size,
            backupCount=backups
        )
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        ))
        self.logger.addHandler(fh)

    def info(self, msg):
        """Log info message."""
        self.logger.info(msg)

    def error(self, msg):
        """Log error message."""
        self.logger.error(msg)

    def debug(self, msg):
        """Log debug message."""
        self.logger.debug(msg)

    def log_transaction(self, tx_id, from_addr, to_addr, amount, currency="ETH"):
        """Log a successful or attempted transaction."""
        msg = f"TX {tx_id}: {from_addr} -> {to_addr} {amount} {currency}"
        self.info(msg)

    def log_wallet_action(self, action, wallet_address, details=""):
        """Log wallet related actions like balance check or key generation."""
        msg = f"Wallet {action} for {wallet_address}: {details}"
        self.info(msg)

    def log_exception(self, exc, context=""):
        """Log an exception with context."""
        self.error(f"Exception in {context}: {type(exc).__name__} - {exc}")

# Sample usage for testing
if __name__ == "__main__":
    wl = WalletLogger(log_level=logging.DEBUG)
    wl.log_transaction("0x123def", "0xabc", "0xdef", "0.5")
    wl.log_wallet_action("balance_check", "0xabc", "balance: 10.0 ETH")
    try:
        raise ValueError("Invalid signature")
    except Exception as e:
        wl.log_exception(e, "sign_transaction")
