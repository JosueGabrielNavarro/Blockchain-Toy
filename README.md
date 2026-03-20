# ⛓️ Python Toy Blockchain (OOP)

A fully functional, Object-Oriented simulation of a Blockchain built from scratch in Python. 
This project was created to deeply understand the core mathematics behind decentralized consensus, immutability, and cryptographic hashing (SHA-256) before transitioning into Smart Contract development.

## 🧠 Core Concepts Applied
- **Object-Oriented Programming (OOP):** Encapsulated logic using `Block` and `Blockchain` classes.
- **Cryptographic Hashing:** Used `hashlib` (SHA-256) to secure block data.
- **Avalanche Effect:** Demonstrated how altering a single character in historical data completely changes the hash.
- **Consensus / Validation:** Built an `isChainValid()` mechanism that acts as a network auditor to detect broken cryptographic links (simulating a 51% attack defense).

## 🚀 The "Hacker" Test
To prove the network's immutability, I simulated an attack where a malicious node alters the data in `Block 2` and recalculates its own hash. 
The `isChainValid()` loop successfully detects that the `prev_hash` of `Block 3` no longer matches the manipulated `Block 2`, returning `False` and securing the network.

*Built as part of my journey to become a Web3 / ZK Protocol Engineer.*
