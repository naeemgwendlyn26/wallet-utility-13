# wallet-utility-13

A high-performance Python toolkit designed for seamless cryptocurrency wallet management and cryptographic operations. This utility provides a streamlined interface for interacting with blockchain assets while prioritizing security and speed.

## Features

*   **HD Wallet Generation:** Securely derive hierarchical deterministic wallets (BIP39/BIP44) with customizable derivation paths.
*   **Balance Aggregation:** Multi-chain support for querying wallet balances across EVM-compatible networks via integrated RPC nodes.
*   **Encrypted Export:** Batch export private keys or mnemonics into AES-256 encrypted local storage files.
*   **Transaction Signing:** Minimalist library for offline transaction signing to ensure private keys never expose to the network layer.

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

The following example demonstrates how to generate a new wallet and retrieve its corresponding address:

```python
from wallet_utility import WalletManager

# Initialize the manager
manager = WalletManager()

# Generate a new BIP39 mnemonic
mnemonic = manager.generate_mnemonic()

# Derive the primary wallet address
wallet = manager.derive_wallet(mnemonic, path="m/44'/60'/0'/0/0")

print(f"Address: {wallet.address}")
print(f"Private Key: {wallet.private_key}")
```

## Security Warning
This utility handles sensitive cryptographic material. Always run in a secure, air-gapped environment when performing mainnet transactions. Never share your mnemonic or private keys with anyone.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.