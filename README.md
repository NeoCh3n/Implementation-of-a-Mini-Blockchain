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

Example of result for task 

### 1
```
Creating accounts for Alice and Bob...

Alice's Private Key:
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEApv5/7iqraE3zo203k4DGdug2xRpYonFEH3o9qarMuplag0cZ
2B6lIpT/yVPIqo45vCZgJmr6/aLehJBwhWME5YP9zT1DekVsjEc/gULYfvz1Ve5z
PWrCoCzqSeP+Nt2OhX8F/uO5OYtjwWUim0LlnmfLv5MNU4gih+srBFWJ1mtcQDeg
sflxIfDvvVPeE4tcbxLZIbkAtShdGyL8cKIKLL0FIozPwURwVAb2oGDOZ4+Dgr4L
nsYHs2QR9aQnv7J3lxkPbO8LlCqKN2rCIRX9gs9cL7IuK5oG9JDzPRqJTCwZBJy2
9GbKTYnQ/p1ReH5isT+9a8paoUuWRE6k7VddrQIDAQABAoH/Rab9tSBP7GpeNMwg
RbsbRWDrPmdpdFfJ9cjqYRMx34ZQHf+mcprHYmxRmVJY7pG5SjK3djJFYYVUZxL0
TZH/eNgjILDCO3aAlx517K0t2K034BF4qkHA6/HP/+VuBpDUi/ZS3zaOYKr78K5a
wNl7l12zuol+6QMYDrV5yf+qtzWcqbruJDa3GBRtWJ8O5MOYeQwXDDANzmkKas5L
TpCDL4yHl7ms8n5mdDaDM2qGsTFwj1ahVtpqyY8fCETqIMKMzl+qBz8fSbgRAGOf
YKscCUE7EVJ/niO7Qh0NpJuTHqf3FUIAxBz0o10e81hkDW0wN7xkTSjsWlqLtvHH
14vhAoGBANnaHShnCnsr6IeZ95+GEbhGV7qbWGnbh2x6tQpMcS1rbq6BncQ+PK+h
FHh/VhndZ8PbDn8Vmrajwhl2268TqH8dgsVMbQkSZ0uCqE+rB+7SirZNMLi3C94u
K0MYEOv7uy+qSzrvmWGc+NjYj3hEZXNFgZfmkl+KEiuI0hNQW5OZAoGBAMQ8hoiV
cZGX9MbAJbsNxKfaeDzuqzOAV0AoY7dD9rCZu7UfqBM5GdVWGxBzQsTL08lN6W6s
gWldebLhvjWnwgS0G/RzkaHbpmypi2gZL8lWJ4EmLLi6rydJ1RdJ0BXXvwa/i1nd
GTKtIv7anSWAuP2X4OoGsXLNTaOTayG1gac1AoGBANl5GmhtzJG++Gb9tauC/Ad3
+TXow+8Q3nTVXgsE2mqb96au796qvowZAkVz4HD7jA2BjUwiNgsjGK2w8Icq2abj
v9rTe3l17LX9naXCN64acayhDAUpfehzMG7PBH1/E5L2rhkMfJJsUCKwtTA7Hwde
mIsZ+n7zZ0YcVJJBQtnpAoGAbBEU2YTLHS28q/NHFALaCMIEMzIQb/U+l2Nmvpcb
9FdFCtLbIXLxqg2YK+/9lhjVkedpJPy068yBZ6RvtmajLynstyspySQIO5EG55Xv
PgZHDRVzzWtpZ85+HiwU/uJoHZRAboWXCdRVEFpd7jg8J9OLFfYHpLwxBGL7vX2S
X/0CgYEA1vKU0cki1vHqkr2aoT8oT3i2PPnp3OEZ6oH7XwjVQFhA2rlt1PX4OgnX
YShx/MWk1AzzRULEtRrgDjEJyWaZVzeFOxLvfWpA5gY5HCEV4YLdQFLMcsbcMbMC
YaRe1cK3FWETZqixuBHQvDsfd+fTQ1hbrapS7Zb7lj26BCcWSjw=
-----END RSA PRIVATE KEY-----


Alice's Public Key:
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApv5/7iqraE3zo203k4DG
dug2xRpYonFEH3o9qarMuplag0cZ2B6lIpT/yVPIqo45vCZgJmr6/aLehJBwhWME
5YP9zT1DekVsjEc/gULYfvz1Ve5zPWrCoCzqSeP+Nt2OhX8F/uO5OYtjwWUim0Ll
nmfLv5MNU4gih+srBFWJ1mtcQDegsflxIfDvvVPeE4tcbxLZIbkAtShdGyL8cKIK
LL0FIozPwURwVAb2oGDOZ4+Dgr4LnsYHs2QR9aQnv7J3lxkPbO8LlCqKN2rCIRX9
gs9cL7IuK5oG9JDzPRqJTCwZBJy29GbKTYnQ/p1ReH5isT+9a8paoUuWRE6k7Vdd
rQIDAQAB
-----END PUBLIC KEY-----


Bob's Private Key:
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAnJMrdpljbWJz6vwZbFJlDj7qgW4gEBHcwWxOCwriB4dLVzfg
zrc/XR/KW6CQ+CIdVdebOfx3vTz1AH+WdgJr9I6hOWll/m3avrEKVfM/b62Dqtv7
5oxsMurLkPSGKXmCYqb5KyWTPozrUWai3DAWNfDltS17YkiwdDKXOmJvmp2zvOZf
lhcHwM64gdMkTCYRzToMnBLvjLiEytPvrVoCuOdc6W2/I/Qc8qLYSSXQbsBb0VcC
f3/9L5UbIA9QhtEiuPNYPGWZLF8fzK/9fHmHdIQTLtD+i9Nz7fryBWO7W6Gep87j
j9rw7U/DwgU3mjKppoCoOvWMOEODUscBAfeYjwIDAQABAoIBAAiqAiUxbrWOVaDC
q3t5gbsMkzhvShnpiyAu6JCm3QQSogIlBu0Zacmy6SUx2OPKK3plEGNgi5WuqlYJ
OV+1WZjyTYyaPvkZxhl4PXytFa0N2nPZcXJ8Ab69jF8skMH5xdPErpQLI7852Ams
lsV9abU5a9SfPC0fnZgIdqLV8JwLGMefOWPO1cbBRUjqKb0VUqb7NzUz+esxz5XS
/R+8Wvrvs4YdLGEMT3Agq46fwo/1fZgUUwQv6R8im5ZDBhZCavDlQqQhAoLd88tO
znQ9GsZ6A73r8jvGiYrtkWyhJWxW1DiEZEkUnJBElQSPbTs2R8iXyUq25E5QAQmN
8RqWBuUCgYEA0uJa7fJF4xeN69hge4/ox0YFFzoC/HWkx9VbXMqNHFMUSur1iWRi
onElZHrXyTSNRiEjD5dWRfY/V9m+lo9FvFcNvaNCWq7qY2l3htYQfFmIk31NrbR+
kuP+xVBcF7zjPUQ8YEZZKIlVA6yw1qdwPvnmDAhNwAr/SebfX1521PUCgYEAvhJq
5oB4VUrVbVClwawIyive7fD/Pv/NDmlyk8CitNJqqxWuJHARo2r/wE5n7BHIPaNc
bSKeK3wiNx/e1ndHjCBxwry9jBQr38VV6rwK35R8NPoRVbtJoe7DpCtWEAOr86pV
E68YajHZaTXgTkRcw+kqn/l2oRD5BQnaztC1JPMCgYEAy8n6XR9W8hF9EIDVHBMB
vDCqErv4zsdRKdvAoncKzmhqn8tW5CKiPqBgpi0gAkxKiY7UNujkck94/who6U4i
8dKecLgoE0IdN1xgKWkMHV7YYM8iFc7q0kCJn1v84uOiJT6fqdnRpx6vjRGBAq5k
BjewW8haek8mTOBS0/KRm1ECgYBrzGRGoJweu5d6LSAlTF2b0+/WgTUyVL/GqbVq
6PkelqwapewjDFBkn323YoB8GcW4d5sm5lhQj1GUdAXdGr9AUPJUINlbxeDwQ6or
vERqc3tSTHViaxsitRjOVim0YXC3fGZOCKNPL0B/9CdoHEuEbQxYuJI4XTjuS52G
aEYkUwKBgQCE4DxkRZFBrk6xZ5rgosu7Wt8M/ggfPuHoVmqirFKaXgI06qfqdmwX
Td3t+/bW+Vm6d2HvhsYfMCrCta1t1xi/Nu8sens4dR/x6vkwFhLaao/59N1U3+EB
FJAtK/nnKFDxAcowxOZdkR+XM5azs1sYPUhBw0pjFJZBwKWbydtWcA==
-----END RSA PRIVATE KEY-----


Bob's Public Key:
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnJMrdpljbWJz6vwZbFJl
Dj7qgW4gEBHcwWxOCwriB4dLVzfgzrc/XR/KW6CQ+CIdVdebOfx3vTz1AH+WdgJr
9I6hOWll/m3avrEKVfM/b62Dqtv75oxsMurLkPSGKXmCYqb5KyWTPozrUWai3DAW
NfDltS17YkiwdDKXOmJvmp2zvOZflhcHwM64gdMkTCYRzToMnBLvjLiEytPvrVoC
uOdc6W2/I/Qc8qLYSSXQbsBb0VcCf3/9L5UbIA9QhtEiuPNYPGWZLF8fzK/9fHmH
dIQTLtD+i9Nz7fryBWO7W6Gep87jj9rw7U/DwgU3mjKppoCoOvWMOEODUscBAfeY
jwIDAQAB
-----END PUBLIC KEY-----


Creating Merkle Tree for a sample transaction...
Merkle Root: 34be9eb4e4bc61b18df8e2123cfd57779f7b53736469e94d021f4e68fd27e777

Running the blockchain simulation...
Block containing 'b'Transaction 2'': 1
Block Details:
Previous Hash: 9ea94bf003eaae447616580dba0e5edc4ff602294f3e3829bc9da6f4b2f507b4
Transactions: [b'Transaction 1', b'Transaction 2']
Merkle Root: 39704f929d837dc8bd8e86c70c4fb06cf740e7294f1036d030e92fe545f18275
Block Hash: 728905316d8d2febb14bf156f9933a320470495a8665c0881403840319cbc182
```

### 2

```
ddd Tx1
ddd Tx2
ddd Tx3
ddd Tx4
tree ['55f743d0d1b9bd86bbd96a46ba4272ddde19f09e3f6e47832e34bb2779a120b580ed43f7a11b3295850dd90cc0cfc9a80334f433af8d3d88a1c5e78aff14988f', '13288c2ba4bbc9af05aa9ccd39b0cc603dc9e30471d97565c9ef3c3604b7ca2375af2038a4bcf0230372d08b917047bdcbad80e5f130061bd5b31596df174b67']
tree ['55f743d0d1b9bd86bbd96a46ba4272ddde19f09e3f6e47832e34bb2779a120b580ed43f7a11b3295850dd90cc0cfc9a80334f433af8d3d88a1c5e78aff14988f13288c2ba4bbc9af05aa9ccd39b0cc603dc9e30471d97565c9ef3c3604b7ca2375af2038a4bcf0230372d08b917047bdcbad80e5f130061bd5b31596df174b67']
Merkle Root:  55f743d0d1b9bd86bbd96a46ba4272ddde19f09e3f6e47832e34bb2779a120b580ed43f7a11b3295850dd90cc0cfc9a80334f433af8d3d88a1c5e78aff14988f13288c2ba4bbc9af05aa9ccd39b0cc603dc9e30471d97565c9ef3c3604b7ca2375af2038a4bcf0230372d08b917047bdcbad80e5f130061bd5b31596df174b67
data integrity： True
data integrity： False
```

### 3

```
Block Hash: 77205fa2105cb5d14b10389d6a5e4f9918c7467aa3ea092e43ac9cb4c5ff93ed, Previous Hash: 0, Merkle Root : 89eb0ac031a63d2421cd05a2fbe41f3ea35f5c3712ca839cbf6b85c4ee07b7a3
Block Hash:1647000b9e9c908b7da8e4e12717f02655c5dd9e9ec01802e02b70fb45cdof1f, Previous Hash: 77205fa2105cb5d14b10389d6a5e4f9918c7467aa3ea092e43ac9cb4c5ff93ed, Merkle Root: 0971909734e9c49e0f45caeb15a450d717de387a0a27df245e7e924bb7e62b0e
Block Hash: 95ed06775959d7c044e4ae293e8f3998fc15d36032a3d224e412ef48300a46dc,Previous Hash: 1647000b9e9c908b7da8e4e12717f02655c5dd9e9ec01802e02b70fb45cdof1f, Merkle Root : 20401ceff3308595e26df24646583f4e3b38f4448c692ab80558f69fea74a3d7
```

### 4

```
Block Hash: 5a3916f21f765560b948974f5424d2b74a787682548abbbd697f4bdf32e62, Previous Hash: 0, Merkle Root: 89ebOac031a63d2421cd05a2fbe41f3ea35f5c3712ca839cbf6b85c4ee07b7a3
Block Hash: a49eacd30ac5ee059708f37c66839ed945cdc63ba858bdb99079ef2f2659b0, Previous Hash: 5a3916f21f765560b948974f5424d2b74a787682548abbbd697f4bdf32e62, Merkle Root: 0971909734e9c49e0f45caeb15a450d717de387a0a27df245e7e924bb7e62bbe
Block Hash: 0154de71eca460ff898031a69c1d86131404da234fbdd30b316143d8701f602, Previous Hash: a49eacd30ac5ee0597e08f37c66839ed945cdc63ba858bdb99079ef2f2659b0, Merkle Root: 2b4b1ceff3308595e26df24646583f4e3b38f4448c692ab80558f69fea74a3d7
Block Hash: ed40649fb7a2a1633b148f6fd4c95f55506b68ed199ed29efe891c31ba7109cd, Previous Hash: 0, Merkle Root: 89eb0ac031a63d2421cd05a2fbe41f3ea35f5c3712ca839cbf6b85c4ee07b7a3
Block Hash: ce047546bd8738055a49776891b8832ad342500b4e69f9a6f49f9124e7d941, Previous Hash: ed40649fb7a2a1633b148f6fd4c95/55506b68ed199ed29efe891c31ba7109cd, Merkle Root: 0971909734e9c49e0f45caeb15a450d717de387a0a27df245e7e924bb7e62b0e
Block Hash: b9b310321abdecfb512a8ea26b38356f3a32762e9386d2ecd52789acf05f844, Previous Hash: ce047546bd8738055a4e9776891b8832ad342500b469f9a6f49f9124e7d941, Merkle Root: 2b4b1ceff330859526df24646583f4e3b38f4448c692ab80558f69fea74a3d7
Tampered Merkle Root: 2b4b1ceff3308595e26df24646583f4e3b38f4448c692ab80558f69fea74a3d7
Tampered Block Hash: 4694d1516e1f9eec80c4d9afalaf974647578c047d3136749231fe783666fdf2
Block has been tampered with!
```