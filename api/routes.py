from flask import Flask, jsonify, request
from blockchain import blockchain_instance

def setup_routes():

    app = Flask(__name__)
    
    @app.route('/chain', methods=['GET'])
    def get_full_chain():
        """Get the full blockchain"""
        return jsonify({'message': 'Blockchain returned succesfully', 'blockchain':blockchain_instance.get_chain()})


    @app.route('/transaction', methods=['POST'])
    def create_transaction():
        """Add a new transaction to the blockchain"""
        data = request.get_json()
        sender = data.get('sender')
        receiver = data.get('receiver')
        amount = data.get('amount')

        if not sender or not receiver or amount is None:
            return jsonify({'error': 'Invalid transaction data'}), 400
        
        transaction_id = blockchain_instance.add_transaction(sender, receiver, amount)

        return jsonify({'message': 'Transaction added to pool succesfully', 'transaction_id': transaction_id}), 201

    @app.route('/mine', methods =['POST'])
    def mine():
        """Mine a new block in the blockchain"""
        # might need to pass some parameters here?
        # If we have multiple miners that have different transactions in their chain. 
        new_index = blockchain_instance.add_block()

        return jsonify({'message': 'Successfully mined new block', 'block_id': new_index}), 201

    @app.route('/pool', methods=['GET'])
    def get_transaction_pool():
        """Returns all transactions currently in pool. 
            I.e. not in current users blockchain.
        """
        # need way of inputting then users blockchain so they can see
        # all the transactions that they don't have.

        return jsonify({'message': 'blockchain returned successfully', 'blockchain': blockchain_instance.get_transaction_pool()}), 200

    return app
