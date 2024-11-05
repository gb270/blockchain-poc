"""
Once a transaction is confirmed (i.e. it has been added to a block), we update the balance of all wallets here.

Wallet needs to:
- keep track of all balances
- update balances.
"""


class WalletManager:
    def __init__(self, intial_balance: dict = {}) -> None:
        self.initial_balance = intial_balance

    # TODO: what to do if person not found in dict
    # if person receives money we need to make them an entry with that amount (probably best to use a default dict)
    # if a person trying to send doesn't have any money then we shouldn't allow it
    # we want to do the transaction checks in transaction validator
    def update_balance(self, sender: str, reciever: str, amount: float) -> None:
        self.initial_balance[sender] -= amount
        self.initial_balance[reciever] += amount
    

    def get_balance(self, person: str) -> float:
        if person in self.initial_balance.keys():
            return self.initial_balance[person]
        else:
            return f"{person} does not have a wallet"
    
    def get_wallet(self) -> dict:
        return self.initial_balance
    
    def add_new_entry(self, new_entry, amount):
        self.initial_balance[new_entry] = amount

if __name__ == "__main__":
    wallet_manager = WalletManager({'Alice': 10.0, 'Bob': 0.0})
    wallet_manager.update_balance('Alice', 'Bob', 10.0)
    print(wallet_manager.get_balance('Alice'))
    print(wallet_manager.get_balance('Bob'))

    print(wallet_manager.get_wallet())



