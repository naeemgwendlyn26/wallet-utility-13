import logging
import re
import sys
from typing import Any, Optional


class CryptoSanitizingFormatter(logging.Formatter):
    """Formatter that redacts sensitive crypto keys and credentials from log output."""

    PATTERNS = [
        (r"\b(0x)?[a-fA-F0-9]{64}\b", "[REDACTED_PRIVATE_KEY]"),
        (r"\b[5KL][1-9A-HJ-NP-Za-k8-9]{50,51}\b", "[REDACTED_WIF_KEY]"),
        (r"(?i)(api[_-]?key|secret|password)\s*[:=]\s*['"]?([^'"\s]+)", r"\1=[REDACTED]"),
    ]

    def format(self, record: logging.LogRecord) -> str:
        original_msg = super().format(record)
        sanitized = original_msg

        try:
            for pattern, replacement in self.PATTERNS:
                sanitized = re.sub(pattern, replacement, sanitized)
        except Exception as err:
            return f"[LOG REDACTION ERROR: {err}] {record.levelname}: fallback"

        return sanitized


class RobustWalletLogger:
    """Configures safe logging with fallback handling for I/O and formatting errors."""

    def __init__(self, name: str = "wallet", log_file: Optional[str] = None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self._setup_handlers(log_file)

    def _setup_handlers(self, log_file: Optional[str]) -> None:
        formatter = CryptoSanitizingFormatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        if log_file:
            try:
                file_handler = logging.FileHandler(log_file, encoding="utf-8")
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)
            except (OSError, PermissionError) as err:
                self.logger.warning(
                    f"Failed to setup file logging for '{log_file}': {err}"
                )

    def log_safe(self, level: int, msg: str, *args: Any, **kwargs: Any) -> None:
        """Logs message safely, preventing app crashes if formatting fails."""
        try:
            self.logger.log(level, msg, *args, **kwargs)
        except Exception as err:
            sys.stderr.write(f"CRITICAL LOGGING ERROR: {err} | Original: {msg}\n")
