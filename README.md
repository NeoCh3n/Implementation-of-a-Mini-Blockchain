.# Implementation-of-a-Mini-Blockchain

Group member:
23408405 CHEN Bowen
23416351 CHEN Chaoyan
22457453 LAM Wai Hung

Task 1:
type ‘python block_chain_4_1.py’ to execute the code

Functions defined: 
create_account() to create a public key and a private key

run_blockchain() to record a transcation and store it in merkle tree

create_merkle_tree() to create a merkle tree to store the transcation record

Main():
create public keys and private keys for Alice and Bob

Stimulate a transaction of 100 coins from Alice to Bob

Store the transaction in a block of Merkle Tree()

Task3:
Construction of blockchain

Function defined :
create_account(): This function will create a new blockchain account, which likely involves generating a public-private key pair that can be used for secure transactions.

run_blockchain(): This function will handle the process of recording a transaction on the blockchain. It will validate the transaction, creating a transaction record, and broadcasting the transaction to the network.

create_merkle_tree(): The function will construct a Merkle tree. Merkle trees are used in blockchains to efficiently and securely verify the contents of large data structures like transaction records.

The transaction is stored in a block within a Merkle Tree using the `create_merkle_tree()` function. The Merkle Tree helps to ensure the integrity of the transaction data within the block and across the blockchain.

Task4:
Integrity verification of transactions and blockchains

Function defined:
`simulate_tampering(blockchain)`: This function takes a `Blockchain` object as an argument and simulates tampering by altering a transaction in the last block of the blockchain. It then recalculates the Merkle root and block hash to determine if tampering can be detected.

 Simulation process:

 - The script first creates a `Blockchain` instance and adds two blocks with sample transactions.
 - The `simulate_tampering` function is then called to demonstrate the effect of tampering with the block data on the blockchain.
  - Modify the transactions in the last block.
  - Recalculate the Merkel root of the tampered block.
  - Recalculate the hashes of the tampered blocks.
  - The recalculated hash is checked to see if it matches the original hash of the block.
 - If the recalculated hash does not match the original hash, the script prints a message stating that the block has been tampered with.



