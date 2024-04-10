# This code will integrate the creation of blockchain accounts, single-input single-output transactions,
# and the construction of a verifiable Merkle tree for inclusion in the blockchain.

import hashlib
import time
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


# Reuse functions from previously reviewed files for account creation and Merkle tree construction
def create_account():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    public_key = private_key.public_key()
    private_key_pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                encryption_algorithm=serialization.NoEncryption())
    public_key_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                             format=serialization.PublicFormat.SubjectPublicKeyInfo)
    return private_key_pem.decode(), public_key_pem.decode()

def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def calculate_merkle_root(transactions):
    tree = [calculate_hash(tx) for tx in transactions]
    while len(tree) > 1:
        temp_tree = []
        for i in range(0, len(tree), 2):
            combined_hash = calculate_hash(tree[i] + tree[min(i+1, len(tree)-1)])
            temp_tree.append(combined_hash)
        tree = temp_tree
    return tree[0]

class Block:
    def __init__(self, transactions, previous_hash=''):
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.merkle_root = calculate_merkle_root(transactions)
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_header = str(self.timestamp) + self.previous_hash + self.merkle_root
        return calculate_hash(block_header)
class Block:
    def __init__(self, transactions, previous_hash=''):
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.merkle_root = calculate_merkle_root(transactions)
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = str(self.timestamp) + self.previous_hash + self.merkle_root + ''.join(self.transactions)
        return calculate_hash(block_string)
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(['Genesis Block'], '0')
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, transactions):
        previous_hash = self.get_latest_block().hash
        new_block = Block(transactions, previous_hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if current_block.hash != current_block.calculate_hash():
                print("Current Block's hash is incorrect")
                return False
            
            if current_block.previous_hash != previous_block.hash:
                print("Previous Block's hash does not match with saved previous hash")
                return False
        return True

# Example usage
blockchain = Blockchain()
blockchain.add_block(["Tx1", "Tx2"])
blockchain.add_block(["Tx3", "Tx4"])

for block in blockchain.chain:
    print(f"Block Hash: {block.hash}, Previous Hash: {block.previous_hash}, Merkle Root: {block.merkle_root}")
