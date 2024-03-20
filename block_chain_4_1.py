from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import hashlib
from merkletools import MerkleTools
from hashlib import sha256

def create_account():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    public_key = private_key.public_key()
    private_key_pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                encryption_algorithm=serialization.NoEncryption())
    public_key_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                              format=serialization.PublicFormat.SubjectPublicKeyInfo)
    return private_key_pem.decode(), public_key_pem.decode()

def create_merkle_tree(transaction_data):
    mt = MerkleTools(hash_type="sha3_256")

    def calculate_transaction_hash(data):
        return hashlib.sha3_256(data.encode()).hexdigest()

    transaction_contents = f"{transaction_data['amount_of_coins']}|{transaction_data['digital_signature']}|{transaction_data['sender_address']}|{transaction_data['receiver_address']}"
    transaction_id = calculate_transaction_hash(transaction_contents)

    mt.add_leaf(transaction_id, do_hash=True)
    mt.make_tree()
    merkle_root = mt.get_merkle_root()

    return merkle_root

def run_blockchain():
    class Block:
        def __init__(self, previous_hash, transactions):
            self.previous_hash = previous_hash
            self.transactions = transactions
            self.merkle_root = self.calculate_merkle_root()
            self.hash = self.calculate_hash()

        def calculate_merkle_root(self):
            mt = MerkleTools(hash_type="sha256")
            for transaction in self.transactions:
                mt.add_leaf(transaction.hex())
            mt.make_tree()
            return mt.get_merkle_root()

        def calculate_hash(self):
            block_contents = ''.join(str(transaction) for transaction in self.transactions) + self.previous_hash + self.merkle_root
            return sha256(block_contents.encode()).hexdigest()

    class Blockchain:
        def __init__(self):
            self.chain = []
            self.create_genesis_block()

        def create_genesis_block(self):
            genesis_block = Block('0', [b'Genesis Transaction'])
            self.chain.append(genesis_block)

        def add_block(self, transactions):
            previous_block = self.chain[-1]
            new_block = Block(previous_block.hash, transactions)
            self.chain.append(new_block)

        def store_blockchain(self, filename):
            with open(filename, 'w') as file:
                for block in self.chain:
                    file.write(f"Previous Hash: {block.previous_hash}\n")
                    file.write(f"Transactions: {block.transactions}\n")
                    file.write(f"Merkle Root: {block.merkle_root}\n")
                    file.write(f"Block Hash: {block.hash}\n\n")

        def get_block_by_transaction(self, transaction):
            for i, block in enumerate(self.chain):
                if transaction in block.transactions:
                    return block, i
            return None, None

    blockchain = Blockchain()
    blockchain.add_block([b'Transaction 1', b'Transaction 2'])
    blockchain.add_block([b'Transaction 3', b'Transaction 4'])

    blockchain.store_blockchain('blockchain.txt')

    transaction_to_find = b'Transaction 2'
    block, block_index = blockchain.get_block_by_transaction(transaction_to_find)
    if block:
        print(f"Block containing '{transaction_to_find}': {block_index}")
        print(f"Block Details:")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Transactions: {block.transactions}")
        print(f"Merkle Root: {block.merkle_root}")
        print(f"Block Hash: {block.hash}")
    else:
        print(f"Transaction '{transaction_to_find}' not found in any block.")

def main():
    print("Creating accounts for Alice and Bob...")
    private_key_a, public_key_a = create_account()
    print("\nAlice's Private Key:")
    print(private_key_a)
    print("\nAlice's Public Key:")
    print(public_key_a)

    private_key_b, public_key_b = create_account()
    print("\nBob's Private Key:")
    print(private_key_b)
    print("\nBob's Public Key:")
    print(public_key_b)

    print("\nCreating Merkle Tree for a sample transaction...")
    transaction_data = {
        "amount_of_coins": 100,
        "digital_signature": hashlib.sha3_256(str(100).encode()).hexdigest(),
        "sender_address": "SenderAddress123",
        "receiver_address": "ReceiverAddress456"
    }
    merkle_root = create_merkle_tree(transaction_data)
    print("Merkle Root:", merkle_root)

    print("\nRunning the blockchain simulation...")
    run_blockchain()

if __name__ == "__main__":
    main()