import hashlib
from Construction_4_3 import Blockchain

# Function to simulate data tampering in a blockchain
def simulate_tampering(blockchain):
    # Simulate tampering by modifying a transaction in the last block
    if len(blockchain.chain) > 1:
        tampered_transaction = "Tampered Tx"
        blockchain.chain[-1].transactions[0] = tampered_transaction
        
        # Recalculate the Merkle root for the tampered block
        tampered_merkle_root = blockchain.chain[-1].calculate_merkle_root()
        # Recalculate the block hash
        tampered_block_hash = blockchain.chain[-1].calculate_hash()
        
        print("Tampered Merkle Root:", tampered_merkle_root)
        print("Tampered Block Hash:", tampered_block_hash)
        
        # Compare the recalculated hash with the original one
        if tampered_block_hash != blockchain.chain[-1].hash:
            print("Block has been tampered with!")
        else:
            print("No tampering detected.")
    else:
        print("Blockchain does not contain enough blocks to simulate tampering.")

# Example usage
blockchain = Blockchain()
blockchain.add_block(["Tx1", "Tx2"])
blockchain.add_block(["Tx3", "Tx4"])

simulate_tampering(blockchain) #This will print "Block has been tampered with!" if the block has been tampered with