import hashlib

# build Merkle tree
def build_tree(data):
    tree = []
    # Save the hash values of all data blocks to leaf nodes
    for d in data:
        print('ddd', d)
        tree.append(hashlib.sha256(d.encode()).hexdigest())

    # create Father node
    while len(tree) > 1:
        parent_level = []
        for i in range(0, len(tree), 2):
            # if current node only have one child node, copy it as another child node
            if i == len(tree) - 1:
                parent_level.append(tree[i] + tree[i])
            else:
                parent_level.append(tree[i] + tree[i+1])
        # add current father node to the tree
        tree = parent_level
        print('tree', tree)
    return tree[0]

# Verify data integrity
def validate(hash, data):
    # if current node is child node, compare it with hash value of data block
    if len(hash) == 64:
        return hash == hashlib.sha256(data.encode()).hexdigest()
    # if current node is father node, recursive validation of child nodes
    left = hash[0:64]
    right = hash[64:]
    return validate(left, data) or validate(right, data)

# test
data = ["Tx1", "Tx2", "Tx3", "Tx4"]
root = build_tree(data)

print("Merkle Root: ", root)
print("data integrity：",validate(root, "Tx4"))
print("data integrity：",validate(root, "Tx7"))