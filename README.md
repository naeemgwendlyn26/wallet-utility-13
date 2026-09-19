# wallet-utility-13

A high-performance Python toolkit for streamlined cryptocurrency wallet management and cryptographic operations. This utility provides a secure, lightweight interface for developers to generate addresses, manage mnemonic phrases, and automate balance lookups across multiple EVM-compatible networks.

## Features

*   **BIP-39 Mnemonic Generation:** Securely generate and derive HD wallets from industry-standard mnemonic phrases.
*   **Multi-Chain Compatibility:** Seamlessly interact with Ethereum, Polygon, and BSC networks using a unified codebase.
*   **Encrypted Key Storage:** Utilize local AES-256 encryption to protect private keys at rest.
*   **Balance Aggregation:** Efficiently fetch native token balances across multiple addresses with asynchronous request support.

## Installation

Ensure you have Python 3.9+ installed. It is recommended to use a virtual environment:

```bash
# Clone the repository
git clone https://github.com/Developer/wallet-utility-13.git
cd wallet-utility-13

# Install dependencies
pip install -r requirements.txt
```

## Basic Usage

The following snippet demonstrates how to generate a new wallet and derive the private key from a mnemonic phrase.

```python
from wallet_utility import WalletManager

# Initialize the manager
manager = WalletManager()

# Create a new wallet
new_wallet = manager.create_wallet()
print(f"Address: {new_wallet.address}")

# Derive address from existing mnemonic
mnemonic = "your secret twelve word phrase here"
wallet = manager.from_mnemonic(mnemonic)
print(f"Derived Public Key: {wallet.public_key}")
```

## Security Warning
*Always store your mnemonic phrases offline.* This tool is intended for development and automation purposes; ensure proper security audits are conducted before using this utility in production financial environments.

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Distributed under the MIT License. See `LICENSE` for more information.