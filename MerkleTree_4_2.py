import hashlib 

transaction_list = []
class trasanctions:
        def __init__(self, amount_of_coins,digital_signature,sender_address,receiver_address):
            self.amount_of_coins = amount_of_coins
            self.digital_signature = digital_signature
            self.sender_address = sender_address
            self.receiver_address = receiver_address
            self.transaction_contents = f"{amount_of_coins}|{digital_signature}|{sender_address}|{receiver_address}"

transaction_data1 = trasanctions('100',hashlib.sha3_256(str(100).encode()).hexdigest(),'SenderAddress1','ReceiverAddress1')
transaction_data2 = trasanctions('50',hashlib.sha3_256(str(50).encode()).hexdigest(),'SenderAddress2','ReceiverAddress2')
transaction_data3 = trasanctions('150',hashlib.sha3_256(str(50).encode()).hexdigest(),'SenderAddress3','ReceiverAddress3')
transaction_data4 = trasanctions('50',hashlib.sha3_256(str(50).encode()).hexdigest(),'SenderAddress4','ReceiverAddress4')

transaction_list = [transaction_data1.transaction_contents, transaction_data2.transaction_contents, transaction_data3.transaction_contents, transaction_data4.transaction_contents]
 
for tx in transaction_list:
    print('tx: ', tx)

def build_merkle_tree(leaves):
    tree = [list(map(lambda x: hashlib.sha256(x.encode()).hexdigest(), leaves))]
    while len(tree[-1]) > 1:
        level = []
        for i in range(0, len(tree[-1]), 2):
            if i + 1 == len(tree[-1]):
                level.append(tree[-1][i])
            else:
                level.append(hashlib.sha256((tree[-1][i] + tree[-1][i + 1]).encode()).hexdigest())
        tree.append(level)
    return tree

def verify_data_integrity(data, root_hash):
    tree = build_merkle_tree(data)
    return root_hash == tree[-1][0]
 
# transactions data
tree = build_merkle_tree(transaction_list)
print("Merkle Tree:", tree)

root_hash = tree[-1][0]
print("Root Hash:", root_hash)
print("Data is Valid:", verify_data_integrity(transaction_list, root_hash))