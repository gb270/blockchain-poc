import hashlib
import time
# using relative import as we are in same parent directory (I think...)
from .block import Block

class Blockchain:
    def __init__(self):
        # list of blocks, intialised with genesis block
        self.chain = [self.create_genesis_block()]
        # dict of transactions, identified by hash
        self.transaction_pool = {}


    def create_genesis_block(self):
        # For now, we will just keep the genesis_block as a hash that doesn't start with the normal number of 0s
        # without passing a nonce we go to the default value of 0
        return Block(0, "0", time.time(), [])
    

    def add_block(self):
        # NOTE: might want to add verification here, based on hash, to check that previous hash is valid (i.e. starts with X number of zeros)
        last_block = self.chain[-1]
        new_block = Block(
            index = len(self.chain),
            previous_hash=last_block.hash,
            timestamp=time.time(),
            # NOTE: at the moment this just takes all transactions from pool and then clears the pool
            # we need a way to store the history of these so we can check future transactions are valid
            # transactions=list(self.transaction_pool.values())
            transactions = list(self.transaction_pool.keys())
        )

        new_block.mine_block(difficulty=4)

        self.transaction_pool.clear()
        self.chain.append(new_block)

        # adding return just for api usage
        return new_block.index

    def get_chain(self):
        # return self.chain
        return [block.to_dict() for block in self.chain]

    def add_transaction(self, sender: str, receiver: str, amount: float):
        transaction_id = self.create_transaction_id(sender, receiver, amount)

        transaction_info = {
            'id': transaction_id,
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'timestamp': time.time()
        }

        self.transaction_pool[transaction_id] = transaction_info

        # used to return id to user once they submit transaction
        return transaction_id
    
    def create_transaction_id(self, sender, receiver, amount):
        # NOTE: could there be an issue that we are running time.time() at different times?
        transaction_data = f"{sender}{receiver}{amount}{time.time()}"
        # NOTE: we are using sha1 because this is just a demo.
        return hashlib.sha1(transaction_data.encode()).hexdigest()
    
    def get_transaction_pool(self):
        return self.transaction_pool
    


# testing
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_transaction('Alice', 'Bob', 10.0)
    blockchain.add_transaction('Charlie', 'David', 15.5)

    print(blockchain.get_transaction_pool())
    print(blockchain.get_chain())
    blockchain.add_block()
    print(blockchain.get_chain())
    print(blockchain.get_transaction_pool())

    blockchain.add_transaction('Alice', 'David', 20.0)
    blockchain.add_transaction('Bob', 'Alice', 21.3)
    blockchain.add_transaction('Eric', 'Alice', 12.34)

    blockchain.add_block()
    print(blockchain.get_chain())

