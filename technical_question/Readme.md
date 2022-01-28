
## What is a blockchain?
```
In my own word, a blockchain is a chain of the block that hard to change the infomation. First I will start with a block, The block contain with block's hash, data, hash of previous block. Block's hash is generated from data and hash of previous block.
Since we assign block's hash with data and previous block's hash encryption. If we change the data in one of the block in the chain, It will make the following blocks invalid. All of I have mentioned above make the blockchain is very secure.
```
Explain in programing view.
```Python
class PrepHashObject():
    def __init__(self, data, prev_hash_block):
        self.merge = tuple({'data': data, 'prev_hash_block':prev_hash_block })

    def get_object(self):
        return self.merge

class Block():
    def __init__(self, data, prev_hash_block=''):
        self.data = data
        self.prev_hash_block = prev_hash_block
        self.hash = self.generate_hash(data, prev_hash_block)

    def generate_hash(self, data, prev_hash_block):
        return str(hash(PrepHashObject(data, prev_hash_block).get_object()))
    
class BlockChain():
    def __init__(self):
        self.chain = [Block('data')]
    
    def get_current_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.hash = new_block.generate_hash(new_block.data, self.get_current_block().hash)
        self.chain.append(new_block)
```

## What is a smart contract?
```
```

## Why Alpha?
```
```
