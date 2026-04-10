# ISA ST400: Special Topics: Introduction to Blockchain

**Credits:** 3  
**Level:** undergraduate  
**Prerequisites:** None

## Course Description
Blockchain technology from management perspective. Students develop smart contracts and deploy the smart contracts in a private Ethereum environment.

## Key Topics
- Blockchain
- Smart contracts
- Ethereum
- Distributed ledger
- Cryptocurrency concepts

---

## Information Bank
*Research and supplementary materials for each key topic below.*

### Blockchain

Blockchain is a decentralized, distributed digital ledger technology that records transactions across a network of computers in a way that makes the records virtually impossible to alter retroactively. It operates as a protocol for the secure transfer of unique instances of value -- such as money, property, contracts, and identity credentials -- via the internet without requiring a third-party intermediary like a bank or government. Each "block" contains a set of transactions, a timestamp, and a cryptographic hash linking it to the previous block, forming a tamper-evident chain.

- **Decentralization**: Data is spread across a vast network of computers (nodes), eliminating single points of failure and removing the need for a central governing authority to validate transactions.
- **Immutability**: Once data is written to the blockchain, it cannot be altered or deleted. Any attempt to change a block would break the cryptographic hash chain, immediately alerting the network.
- **Consensus mechanisms**: Nodes agree on the valid state of the ledger through algorithms such as Proof of Work (PoW) or Proof of Stake (PoS), ensuring all copies of the ledger remain synchronized.
- **Cryptographic security**: Public-key cryptography secures transactions and identities, allowing participants to sign and verify data without exposing private information.
- **Transparency**: All transactions on a public blockchain are visible to every participant, enabling auditability and reducing opportunities for fraud.
- **Peer-to-peer architecture**: Participants interact directly without intermediaries, reducing transaction costs and processing delays.

**Practical Applications:** Blockchain is used far beyond cryptocurrency -- enterprises deploy it for supply chain tracking, regulatory compliance auditing, digital identity management, and cross-border payments, where its tamper-proof ledger reduces fraud risk and eliminates costly intermediaries.

---

### Smart contracts

A smart contract is a self-executing computer program stored on a blockchain that automatically enforces and executes the terms of an agreement when predetermined conditions are met. The terms between parties are written directly into code using conditional "if-then" logic, removing the need for intermediaries such as lawyers, banks, or escrow agents. Once deployed to a blockchain, a smart contract's code is immutable and its execution is transparent and verifiable by all network participants.

- **Automated execution**: Smart contracts trigger actions automatically when conditions are satisfied -- for example, releasing payment once a shipment is confirmed delivered -- eliminating manual processing that can take days or weeks.
- **Trustlessness**: Two parties can enter into binding agreements without knowing or trusting each other, because the blockchain network guarantees execution exactly as programmed.
- **Immutability and transparency**: Once deployed, smart contract code cannot be changed. All execution history is publicly verifiable on the blockchain, increasing accountability and reducing disputes.
- **Deployment lifecycle**: A smart contract is written (commonly in Solidity for Ethereum), compiled to bytecode, deployed to a blockchain address, and then waits for triggering transactions to execute its functions.
- **State and storage**: Smart contracts maintain their own persistent state (data variables) on the blockchain and can hold funds (such as Ether) in escrow until release conditions are met.
- **Limitations**: Smart contracts cannot access off-chain data on their own and require "oracles" to feed external information. Bugs in contract code can lead to irreversible financial losses since the code cannot be patched once deployed.

**Practical Applications:** Smart contracts power decentralized finance (DeFi) platforms, automated insurance payouts, supply chain verification, tokenized real estate transactions, and decentralized autonomous organizations (DAOs), reducing arbitration costs and fraud while accelerating settlement times.

---

### Ethereum

Ethereum is a decentralized, open-source blockchain platform conceived in 2013 by Vitalik Buterin and launched on July 30, 2015. Unlike Bitcoin, which was designed primarily as a digital currency, Ethereum was built to be a programmable "world computer" where developers can write and deploy smart contracts and decentralized applications (dApps) that run without downtime, censorship, or third-party interference. Ether (ETH) is the platform's native cryptocurrency, used to pay transaction fees (called "gas") and compensate validators who secure the network.

- **Ethereum Virtual Machine (EVM)**: The EVM is the runtime environment that executes smart contract bytecode on every node in the network, ensuring deterministic and consistent results across the decentralized system.
- **Solidity programming language**: Solidity is Ethereum's primary high-level programming language for writing smart contracts. It is statically typed and supports inheritance, libraries, and complex user-defined types.
- **Gas and transaction fees**: Every computational operation on Ethereum costs "gas," a unit that measures the work required. Users pay gas fees in ETH to incentivize validators and prevent network spam.
- **Proof of Stake (The Merge)**: In September 2022, Ethereum transitioned from energy-intensive Proof of Work to Proof of Stake via "The Merge," reducing energy consumption by approximately 99.95% and allowing ETH holders to stake their tokens to validate transactions.
- **Decentralized applications (dApps)**: dApps combine on-chain smart contract logic with a frontend user interface, enabling applications ranging from decentralized exchanges (Uniswap) to NFT marketplaces (OpenSea) and lending protocols (Aave).
- **Private Ethereum networks**: Organizations can deploy private or permissioned Ethereum networks (using tools like Ganache or Hyperledger Besu) for testing, development, and enterprise use cases without exposing data to the public mainnet.

**Practical Applications:** Ethereum powers the vast majority of DeFi protocols, NFT ecosystems, and DAO governance systems. In a classroom setting, students deploy smart contracts on private Ethereum testnets to learn development without incurring real transaction costs.

---

### Distributed ledger

Distributed ledger technology (DLT) is a decentralized record-keeping system in which multiple nodes across a network independently maintain, validate, and update identical copies of a shared ledger -- without relying on a central trusted authority. Blockchain is the most well-known form of DLT, but the concept also encompasses other data structures such as directed acyclic graphs (DAGs) and hybrid architectures. DLT fundamentally changes how data integrity and trust are established by replacing centralized databases with peer-to-peer consensus.

- **Consensus algorithms**: Participating nodes use algorithms -- such as Proof of Work (PoW), Proof of Stake (PoS), or Byzantine Fault Tolerance (BFT) -- to agree on the correct state of the ledger, ensuring consistency even if some nodes fail or act maliciously.
- **Permissioned vs. permissionless**: Public (permissionless) DLTs like Bitcoin allow anyone to join and validate; private (permissioned) DLTs restrict participation to authorized entities, offering greater control and privacy for enterprise use cases.
- **Cryptographic security**: DLT uses hashing algorithms and digital signatures to secure data, ensure integrity, and authenticate participants. Only users with the correct cryptographic keys can read or write to the ledger.
- **Immutability**: Once a transaction is validated and recorded, it becomes part of a permanent, append-only record that cannot be deleted or retroactively modified, creating a reliable audit trail.
- **Data replication**: Every node holds a complete, synchronized copy of the ledger, eliminating single points of failure and ensuring high availability even if individual nodes go offline.
- **DLT beyond blockchain**: Non-blockchain DLTs include IOTA's Tangle (a DAG-based structure) and Hashgraph, which use alternative approaches to achieve consensus with different performance trade-offs.

**Practical Applications:** Financial institutions use DLT for real-time securities settlement and cross-border payments, while governments explore it for land registries, voting systems, and healthcare records -- any scenario where multiple parties need a shared, tamper-proof source of truth without a central intermediary.

---

### Cryptocurrency concepts

Cryptocurrency is a form of digital or virtual currency that uses cryptographic techniques for security and operates on decentralized networks, typically built on blockchain technology, without reliance on any central authority such as a government or bank. Bitcoin, released as open-source software in 2009 by the pseudonymous Satoshi Nakamoto, was the first cryptocurrency and remains the largest by market capitalization. Cryptocurrencies enable peer-to-peer value transfer over the internet, with ownership records stored on a distributed ledger that is publicly verifiable.

- **Wallets and keys**: A cryptocurrency wallet stores a pair of cryptographic keys -- a public key (the address others use to send funds) and a private key (used to authorize spending). Whoever controls the private key controls the associated funds.
- **Mining and validation**: In Proof of Work systems, "miners" compete to solve computational puzzles to validate transaction blocks and earn newly minted coins as rewards. Proof of Stake systems select validators based on the amount of cryptocurrency they have staked as collateral.
- **Tokens vs. coins**: A "coin" (e.g., Bitcoin, Ether) operates on its own native blockchain, while a "token" (e.g., ERC-20 tokens) is built on top of an existing blockchain platform and can represent assets, utility, or governance rights.
- **Volatility and market dynamics**: Cryptocurrency prices are highly volatile, driven by supply-and-demand dynamics, regulatory news, technological developments, and market sentiment rather than central bank monetary policy.
- **Decentralization and trustlessness**: Transactions are verified by network consensus rather than a trusted intermediary, making the system resistant to censorship and single points of failure.
- **Regulatory landscape**: Governments worldwide are developing frameworks for cryptocurrency taxation, anti-money-laundering (AML) compliance, and consumer protection, creating an evolving legal environment that varies significantly by jurisdiction.

**Practical Applications:** Cryptocurrencies are used for cross-border remittances with lower fees than traditional wire transfers, as programmable money within DeFi ecosystems for lending and borrowing, and increasingly by institutions as an alternative asset class for portfolio diversification.

---

