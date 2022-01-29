
## What is a blockchain?

In my own word, a blockchain is a chain of the block that hard to change the infomation. First I will start with a block, The block contain with block's hash, data, hash of previous block. Block's hash is generated from data and hash of previous block.
Since we assign block's hash with data and previous block's hash encryption. If we change the data in one of the block in the chain, It will make the following blocks invalid. All of I have mentioned above make the blockchain is very secure.

Explain in programing view.
```Python
class PrepHashObject:
    def __init__(self, data, prev_hash_block):
        self.merge = tuple({'data': data, 'prev_hash_block':prev_hash_block })

    def get_object(self):
        return self.merge

class Block:
    def __init__(self, data, prev_hash_block=''):
        self.data = data
        self.prev_hash_block = prev_hash_block
        self.hash = self.generate_hash(data, prev_hash_block)

    def generate_hash(self, data, prev_hash_block):
        return str(hash(PrepHashObject(data, prev_hash_block).get_object()))
    
class BlockChain:
    def __init__(self):
        self.chain = [Block('data')]
    
    def get_current_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.hash = new_block.generate_hash(new_block.data, self.get_current_block().hash)
        self.chain.append(new_block)
```

## What is a smart contract?

A smart contract is a program which is stored in a blockchain. The smart contract work same as if then statement. 
For example, If a condtion is true, then action1 occurs else action2 occures. If we compare with the real world, 
we don't have to trust third-party because the smart contract executes following the actual contract. 
Since the smart contract is stored in the blockchain, it hard to be changed. Therefore, no one can change the actual 
contract easily.

## Why Alpha?

Since I have watched K' Tascha interview on bitcast channel, I'm very impressed by  K' Tascha viewpoint. And Alpha always adapt the product following the customer need and Alpha uses decomposing and composing strategy to handle with complex problems. Alpha not only focused on DeFi platform but also researching and innovating in a blockchain.
Moreover, Alpha has many interested products that different from other DeFi platforms. All of I have mentioned is a reason why I want to work with Alpha.
