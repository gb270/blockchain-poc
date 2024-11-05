import hashlib
import time

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, transactions: list, nonce: int = 0) -> None:
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        # will contain list of all transactions contained in each block
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}"
        return hashlib.sha1(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty: int) -> None:
        prefix_str = '0' * difficulty
        while self.hash[:difficulty] != prefix_str:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def get_hash(self) -> str:
        return self.hash
    

    # added as was having difficulties using Block object with json
    # Would be better if there was an easier fix
    def to_dict(self):
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'nonce': self.nonce,
            'hash': self.hash
        }

    # making printing possible
    def __repr__(self):
        return (f"Block(index={self.index}, previous_hash='{self.previous_hash}', "
                f"timestamp={self.timestamp}, transactions={self.transactions}, "
                f"nonce={self.nonce}, hash='{self.hash}')")


# testing
if __name__ == "__main__":
    block = Block(1, 0, time.time(), [], 0)
    print(block.get_hash())

    valid_nonce = None
    for i in range(100000):
        block = Block(1, 0, time.time(), ["1234", "23532523", "435234652"], i)
        if block.get_hash()[:4] == "0000":
            print(i)
            valid_nonce = i
            break

    if valid_nonce:
        print(f"block hash is: {block.get_hash()}")
    else:
        print("No valid nonce found within search range")
