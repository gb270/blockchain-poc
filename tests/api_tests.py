import requests

BASE_URL = 'http://127.0.0.1:5000'

headers = {'Content-Type': 'application/json'}

def test_api():
    # Create transactions
    response = requests.post(f"{BASE_URL}/transaction", json={'sender': 'Alice', 'receiver': 'Bob', 'amount': 10.0}, headers=headers)
    print(response.json())

    response = requests.post(f"{BASE_URL}/transaction", json={'sender': 'Charlie', 'receiver': 'David', 'amount': 15.5}, headers=headers)
    print(response.json())

    # Get transaction pool
    response = requests.get(f"{BASE_URL}/pool", headers=headers)
    print("Transaction Pool:")
    print(response.json())

    # Mine a block
    response = requests.post(f"{BASE_URL}/mine", headers=headers)
    print(response.json())

    # Get the full chain
    response = requests.get(f"{BASE_URL}/chain", headers=headers)
    print("Blockchain:")
    print(response.json())

    


if __name__ == "__main__":
    test_api()