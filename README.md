# Blockchain Proof-Of-Concept

A simple blockchain proof-of-concept with Python and Flask, designed for local execution.
This project includes basic blockchain functionality, including transaction management, mining, and a RESTful API for interaction.

## Project Structure
- blockchain: Contains the core blockchain and transaction functionality.
- network: Manages transaction validation and wallet tracking.
- tests: Contains API tests to verify the functionality of various components.
- api: The main Flask application that exposes interaction through a RESTful endpoint.

## Features
- Blockchain: Provides basic blockchain functionality, including adding transactions, mining new blocks and validating the chain.
- Transaction Pool: Manages a pool of pending transactions, ensuring only valid transactions are added.
- Wallet Tracking: Allows viewing of individual wallet balances based on transaction history.
- API: Provides endpoints for managing tranasactions, mining and retrieving blockchain data.

## Routes
The API exposes the following routes:
- **`GET /chain`**: Returns the full blockchain.
- **`POST /transaction`**: Adds a new transaction to the transaction pool.
- **`POST /mine`**: Mines a new block using the current transaction pool.
- **`GET /pool`**: Returns all transactions currently in the transaction pool.
- **`GET /review_transaction`**: Returns information for a validated transaction.
- **`GET /wallet`**: Returns balance for a given users wallet.

## Prerequisites
- Python 3.9 or higher
- Flask
- Requests library (for testing)

## Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/gb270/blockchain-poc.git
cd blockchain-poc
```

### 2. Create a virtual environment

It is highly recommended to use a virtual environment to manage dependencies. For more info on virtual environments, I highly recommend this [link](https://realpython.com/python-virtual-environments-a-primer/).

```bash
python3 -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Run the Flask API

```bash
python main.py
```

### 5. Run the tests

Whilst your flask server is running, from another terminal run:

```bash
python -m tests.api_tests
```

You can also test the API by just sending a request directly to the endpoint.

## License

This project is licensed under the GNU GPL. See the [License](LICENSE) file for more details. 

