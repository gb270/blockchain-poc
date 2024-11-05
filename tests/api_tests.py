import requests

BASE_URL = 'http://127.0.0.1:5000'

headers = {'Content-Type': 'application/json'}

def create_transaction(sender: str, receiver: str, amount: float):
    response = requests.post(f"{BASE_URL}/transaction", json={'sender': sender, 'receiver': receiver, 'amount': amount}, headers=headers)
    print(response.json())

def get_transaction_pool():
    response = requests.get(f"{BASE_URL}/pool", headers=headers)
    print("Transaction Pool:")
    print(response.json())

def mine_block():
    response = requests.post(f"{BASE_URL}/mine", headers=headers)
    print(response.json())

def get_full_chain():
    response = requests.get(f"{BASE_URL}/chain", headers=headers)
    print("Blockchain:")
    print(response.json())

def test_api():
    create_transaction('Alice', 'Bob', 10.0)

    create_transaction('Charlie', 'David', 15.5)

    get_transaction_pool()

    mine_block()

    get_full_chain()

    create_transaction('Larry', 'Tommy', 52.1)
    create_transaction('Alice', 'Charlie', 10.0)
    create_transaction('David', 'Bob', 100.0)

    mine_block()
    get_full_chain()
    mine_block()
    get_full_chain()




if __name__ == "__main__":
    test_api()