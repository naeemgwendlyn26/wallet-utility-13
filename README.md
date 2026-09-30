# wallet-utility-13

`wallet-utility-13` is a lightweight, Python-based toolkit designed for secure management and rapid auditing of cryptocurrency wallets. It provides developers and power users with a streamlined interface for monitoring balances and automating transactional workflows across EVM-compatible chains.

## Features

*   **HD Wallet Generation:** Derives BIP-39 compliant mnemonic phrases and extended private keys for multi-chain account management.
*   **Balance Aggregation:** Supports real-time balance fetching across Ethereum, Polygon, and BSC via integrated RPC providers.
*   **Batch Transaction Signing:** Securely signs multiple offline transactions with configurable gas estimation and nonce management.
*   **Audit Logger:** Exports wallet activity and transaction history to structured CSV formats for easier financial reconciliation.

## Installation

Ensure you have Python 3.9+ installed. Clone the repository and install the dependencies:

```bash
git clone https://github.com/Developer/wallet-utility-13.git
cd wallet-utility-13
pip install -r requirements.txt
```

## Usage

You can initialize a new wallet instance and fetch current balances by running the following script:

```python
from wallet_utility import WalletManager

# Initialize with mnemonic
manager = WalletManager(mnemonic="your twelve word seed phrase here")

# Retrieve balance for the primary address
balance = manager.get_balance(chain="ethereum")
print(f"Current ETH Balance: {balance} ETH")

# Send a transaction
tx_hash = manager.transfer(to="0xRecipientAddress", amount=0.5, gas_strategy="fast")
print(f"Transaction successful: {tx_hash}")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.