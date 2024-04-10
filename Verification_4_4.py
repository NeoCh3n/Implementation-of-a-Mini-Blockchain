import hashlib
from Construction_4_3 import Blockchain

def simulate_tampering(blockchain):
    if len(blockchain.chain) > 1:
        tampered_transaction = "Tampered Tx"
        blockchain.chain[-1].transactions[0] = tampered_transaction
        
        tampered_merkle_root = blockchain.chain[-1].merkle_root
        tampered_block_hash = blockchain.chain[-1].calculate_hash()
        
        print("Tampered Merkle Root:", tampered_merkle_root)
        print("Tampered Block Hash:", tampered_block_hash)
        
        if tampered_block_hash != blockchain.chain[-1].hash:
            print("Block has been tampered with!")
        else:
            print("No tampering detected.")
    else:
        print("Blockchain does not contain enough blocks to simulate tampering.")

blockchain = Blockchain()
blockchain.add_block(["Tx1", "Tx2"])
blockchain.add_block(["Tx3", "Tx4"])

for block in blockchain.chain:
    print(f"Block Hash: {block.hash}, Previous Hash: {block.previous_hash}, Merkle Root: {block.merkle_root}")

simulate_tampering(blockchain)