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
`create_account()` will create a new blockchain account, and generate a public-private key pair.

`run_blockchain()` will recorde transaction. It will verify the transaction, create transaction record, and broadcast transaction to net.

`create_merkle_tree()` will construct a Merkle tree to verify the contents of data structures. Transaction will be stored in block and it will ensure the integrity of the transaction data.

Task4:
Integrity verification

Function defined:
`simulate_tampering(blockchain)` will simulate tampering and recalculate the Merkle root and hash, to find if there is a tampering.
