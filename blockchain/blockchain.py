import hashlib
import time
# using relative import as we are in same parent directory (I think...)
from .block import Block
from network import TransactionValidator, TransactionHistory, WalletManager

class Blockchain:
    def __init__(self):
        # list of blocks, intialised with genesis block
        self.chain = [self.create_genesis_block()]
        # dict of transactions, identified by hash
        self.transaction_pool = {}
        # validated pool only needs to be a list as we are just storing hashes, the info will be kept in the 
        # transaction history
        self.validated_pool = []
        # NOTE: can extend these to create a way for blockchains to catch up
        # what I mean is that if we just upload transaction history, wallet etc, then we can use this to see where a blockchain
        # compares with other blockchain
        self.transaction_history = TransactionHistory()
        # NOTE: this can be changed to adjust initial balances
        wallet = {'Alice': 10.0, 'Bob': 0.0, 'David': 2000.0, 'Larry': 52.2, 'Charlie':2.0}
        self.wallet_manager = WalletManager(wallet)
        self.transaction_validator = TransactionValidator(self.transaction_pool, self.wallet_manager, self.transaction_history)




    def create_genesis_block(self):
        # For now, we will just keep the genesis_block as a hash that doesn't start with the normal number of 0s
        # without passing a nonce we go to the default value of 0
        return Block(0, "0", time.time(), [])
    

    def add_block(self):
        # NOTE: might want to add verification here, based on hash, to check that previous hash is valid (i.e. starts with X number of zeros)
        last_block = self.chain[-1]
        
        # before adding new block we run verification
        self.transaction_validator.check_valid_transactions()
        self.validated_pool = self.transaction_validator.get_validated_pool()
        new_block = Block(
            index = len(self.chain),
            previous_hash=last_block.hash,
            timestamp=time.time(),
            # NOTE: at the moment this just takes all transactions from pool and then clears the pool
            # we need a way to store the history of these so we can check future transactions are valid
            # transactions=list(self.transaction_pool.values())
            transactions = self.validated_pool
        )

        new_block.mine_block(difficulty=4)

        self.transaction_pool.clear()
        self.validated_pool.clear()
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
    
    def get_validated_pool(self):
        return self.validated_pool
    


# testing
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_transaction('Alice', 'Bob', 10.0)
    blockchain.add_transaction('Charlie', 'David', 15.5)
    blockchain.add_transaction('Alice', 'Charlie', 1.0)
    print(blockchain.wallet_manager.get_balance('Eric'))

    print(blockchain.get_transaction_pool())
    print(blockchain.get_chain())
    blockchain.add_block()
    print(blockchain.get_chain())
    print(blockchain.get_transaction_pool())

    blockchain.add_transaction('David', 'Alice', 20.0)
    blockchain.add_transaction('Bob', 'Alice', 21.3)
    blockchain.add_transaction('Alice', 'Eric', 12.34)

    blockchain.add_block()
    print(blockchain.get_chain())

    print(blockchain.wallet_manager.get_wallet())
    print(blockchain.transaction_history.get_transaction_history())
    print(blockchain.wallet_manager.get_balance('Eric'))
