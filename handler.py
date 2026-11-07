"""Transaction and payload edge case error handler for wallet operations."""

import logging
from typing import Any, Dict, Optional, Tuple

logger = logging.getLogger(__name__)


class CryptoHandlerError(Exception):
    """Base exception for wallet handler failures."""
    pass


class InvalidAddressError(CryptoHandlerError):
    """Raised when a wallet address is malformed."""
    pass


class InsufficientBalanceError(CryptoHandlerError):
    """Raised when account balance cannot cover transaction cost + gas."""
    pass


def safe_execute_transaction(
    tx_data: Dict[str, Any],
    wallet_balance: float,
    rpc_client: Optional[Any] = None
) -> Tuple[bool, Optional[str]]:
    """Validates and executes a crypto transaction, handling key edge cases.

    Returns a tuple of (success_status, tx_hash_or_error_message).
    """
    try:
        # Edge case 1: Missing or invalid transaction fields
        recipient = tx_data.get("recipient")
        amount = tx_data.get("amount", 0.0)
        gas_fee = tx_data.get("gas_fee", 0.0)

        if not recipient or not isinstance(recipient, str):
            raise InvalidAddressError("Recipient address is missing or invalid")

        if len(recipient) < 26 or len(recipient) > 42:
            raise InvalidAddressError(f"Invalid address length: {len(recipient)}")

        # Edge case 2: Invalid non-positive amount
        if amount <= 0:
            raise ValueError(f"Invalid transaction amount: {amount}")
        
        total_cost = amount + gas_fee
        
        # Edge case 3: Insufficient balance including gas estimation
        if wallet_balance < total_cost:
            raise InsufficientBalanceError(
                f"Balance {wallet_balance} insufficient for total cost {total_cost}"
            )

        # Edge case 4: RPC Network connection simulation or execution failure
        if rpc_client is not None:
            tx_hash = rpc_client.send_raw_transaction(tx_data)
        else:
            # Dry-run fallback calculation
            tx_hash = f"0xmock_{hash(str(tx_data)) & 0xffffffff:08x}"

        logger.info(f"Transaction executed successfully: {tx_hash}")
        return True, tx_hash

    except (InvalidAddressError, InsufficientBalanceError) as err:
        logger.warning(f"Wallet transaction edge case handled: {err}")
        return False, str(err)
    except ValueError as err:
        logger.warning(f"Value validation error: {err}")
        return False, f"Validation failure: {err}"
    except Exception as err:
        logger.error(f"Unexpected transaction execution error: {err}", exc_info=True)
        return False, f"System error: {type(err).__name__}"
