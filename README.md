# BlockchainArchitecture
Decentralized Double-Spending Prevention Protocol
Project Overview

This project demonstrates a decentralized protocol designed to prevent the same digital asset from being spent more than once. Unlike traditional centralized systems, this protocol relies on a peer-to-peer network of nodes to validate transactions and maintain a shared ledger, eliminating the need for a central authority.

Problem Addressed

In digital transactions, a major challenge is double spending, where a user tries to spend the same digital currency multiple times. Without a central system to verify each transaction, it becomes difficult to prevent fraud. This project simulates a solution for that problem using a decentralized network.

Key Features

Decentralized validation: Transactions are verified by multiple nodes in the network.

Double-spending prevention: Each transaction is checked against the ledger and mempool to ensure the same digital asset is not spent twice.

Consensus mechanism: Nodes reach agreement before confirming transactions to make the system reliable and secure.

Distributed ledger: The network maintains a shared ledger of all confirmed transactions, which is publicly verifiable.

Simulation of a network: Demonstrates transaction broadcasting and consensus among nodes without a central server.

How the Protocol Works

A user creates a transaction specifying the sender, receiver, amount, and a unique transaction ID.

The transaction is broadcast to all nodes in the network.

Each node validates the transaction against its ledger and mempool.

Valid transactions are temporarily stored in the node’s mempool.

A consensus mechanism confirms the transaction when enough nodes agree.

The confirmed transaction is permanently added to the ledger.

Applications

Cryptocurrency systems like Bitcoin and Ethereum.

Any decentralized digital payment system.

Preventing fraud in digital assets and tokens.

Conclusion

This project successfully simulates a decentralized double-spending prevention system. It shows how transactions can be validated and confirmed in a peer-to-peer network without relying on a central authority. The simulation demonstrates core blockchain principles like transaction validation, consensus, and ledger maintenance, providing a practical understanding of decentralized digital currency systems.

