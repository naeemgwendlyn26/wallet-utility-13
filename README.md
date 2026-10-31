# wallet-utility-13

A high-performance Python toolkit designed for seamless cryptocurrency wallet management and cryptographic operations. This utility provides a streamlined interface for key derivation, transaction signing, and balance monitoring across multiple EVM-compatible networks.

## Features

*   **BIP-39 Implementation:** Generate secure, industry-standard mnemonic phrases and hierarchical deterministic (HD) wallets with customizable derivation paths.
*   **Multi-Chain Support:** Native integration for signing transactions and querying RPC nodes across Ethereum, BSC, Polygon, and Arbitrum.
*   **Encrypted Storage:** Built-in AES-256 local keystore utility to protect sensitive private keys and sensitive configuration data at rest.
*   **Balance Aggregator:** Lightweight asynchronous fetching of token balances using `aiohttp` for rapid, concurrent portfolio snapshots.

## Installation

Ensure you have Python 3.10+ installed. Clone the repository and install the required dependencies via `pip`:

```bash
git clone https://github.com/Developer/wallet-utility-13.git
cd wallet-utility-13
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

This snippet demonstrates how to generate a new wallet and derive the corresponding public address:

```python
from wallet_utility import WalletManager

# Initialize manager
manager = WalletManager()

# Create new HD wallet
mnemonic, address = manager.create_new_wallet()

print(f"Address: {address}")
print(f"Mnemonic: {mnemonic}")

# Sign a transaction
tx_hash = manager.sign_transaction(private_key, to_address, amount=0.01)
print(f"Transaction broadcasted: {tx_hash}")
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Distributed under the MIT License. See `LICENSE` for more information.