"""
can use this to keep track of all transactions.
Provide functionality here that allows users to query what occured at each transaction.

We will instantiate this with the blockchain object so that we can keep it consistent between all classes
"""
class TransactionHistory:
    def __init__(self, transaction_history:dict = {}) -> None:
        self.transaction_history = transaction_history

    def get_transaction(self, transaction_id: str) -> dict:
        return self.transaction_history[transaction_id]
    
    def get_transaction_history(self) -> dict:
        return self.transaction_history
    
    def add_transaction(self, transaction_id: str, transaction_info: dict) -> None:
        self.transaction_history[transaction_id] = transaction_info