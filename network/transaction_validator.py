"""
Check balances for sufficient funds.
Verify transaction format.
Prevent double spending (note that if two transactions are in the same block we need to ensure the timestamp is one before another).
I.e. it is important to prevent double spending in time order. If something is double spending - we only add the latest 
"""
from .wallet_manager import WalletManager
from .transaction_history import TransactionHistory


# TODO: what if someone sends money to themselves?

class TransactionValidator:
    def __init__(self, pool: dict, wallet_manager: WalletManager, transaction_history: TransactionHistory):
        self.pool = pool
        self.wallet_manager = wallet_manager
        self.validated_pool = []
        self.transaction_history = transaction_history

    def check_valid_transactions(self):
        for transaction in self.pool:
            transaction_info = self.pool[transaction]
            amount = transaction_info['amount']
            sender = transaction_info['sender']
            receiver = transaction_info['receiver']

            # print(f"{sender} is trying to send {receiver} £{amount}")
            if self._check_valid_transaction(amount, sender, receiver):
                self.validated_pool.append(transaction)
                # print("Transaction approved")
                self.transaction_history.add_transaction(transaction, transaction_info)
            
            else:
                # print("Transaction rejected")
                continue



    # creating seperate function to check each individual function so that error can be returned
    # and not interfere with running of code
    def _check_valid_transaction(self, amount, sender, receiver) -> bool:
        # if wallet does not exist
        if sender not in self.wallet_manager.get_wallet():
            return False
        
        # if insufficient funds
        if amount > self.wallet_manager.get_balance(sender):
            return False

        if receiver not in self.wallet_manager.get_wallet().keys():
            # we need to add the receiver and then also modify the wallet of the sender by the right amount
            
            self.wallet_manager.add_new_entry(receiver, 0)
            self.wallet_manager.update_balance(sender, receiver, amount)


            return True
        
        else:

            self.wallet_manager.update_balance(sender, receiver, amount)
            return True

    # TODO: make sure that the blockchain class gets a validated pool from the transaction pool
    def get_validated_pool(self) -> list:
        return self.validated_pool





if __name__ == "__main__":
    pool = {'0c0fdacda10019c7c1e85c01b0ab2b286e6946b6': {'amount': 10.0, 'id': '0c0fdacda10019c7c1e85c01b0ab2b286e6946b6', 'receiver': 'Bob', 'sender': 'Alice', 'timestamp': 1730824340.53603}, '8709355cf695dc28d39ad0bb8d5a36325ad4e532': {'amount': 100.0, 'id': '8709355cf695dc28d39ad0bb8d5a36325ad4e532', 'receiver': 'Bob', 'sender': 'David', 'timestamp': 1730824340.544853}, '9cb3e4e6ecde02191ca0760e0635cd6d324004cf': {'amount': 10.0, 'id': '9cb3e4e6ecde02191ca0760e0635cd6d324004cf', 'receiver': 'Charlie', 'sender': 'Alice', 'timestamp': 1730824340.542599}, 'd8f84495b9d476ef1b04893faf7ba123a259ec0e': {'amount': 52.1, 'id': 'd8f84495b9d476ef1b04893faf7ba123a259ec0e', 'receiver': 'Tommy', 'sender': 'Larry', 'timestamp': 1730824340.540362}, 'e5739606efc59025ab665ce23ef68807eff72301': {'amount': 15.5, 'id': 'e5739606efc59025ab665ce23ef68807eff72301', 'receiver': 'David', 'sender': 'Charlie', 'timestamp': 1730824340.537961}}
    wallet = {'Alice': 10.0, 'Bob': 0.0, 'David': 2000.0, 'Larry': 52.2, 'Charlie':2.0}
    wallet_manager = WalletManager(wallet)
    transaction_history = TransactionHistory()
    transaction_validator = TransactionValidator(pool, wallet_manager, transaction_history)
    transaction_validator.check_valid_transactions()
    print(transaction_validator.get_validated_pool())
    print(wallet_manager.get_wallet())
    print(transaction_history.get_transaction_history())
    print(transaction_history.get_transaction('8709355cf695dc28d39ad0bb8d5a36325ad4e532'))