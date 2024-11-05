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
            Note that these are not neccesarily valid transactions
        """
        # need way of inputting then users blockchain so they can see
        # all the transactions that they don't have.

        return jsonify({'message': 'transaction pool returned successfully', 'transaction_pool': blockchain_instance.get_transaction_pool()}), 200
    
    @app.route('/review_transaction', methods=['GET'])
    def get_completed_transaction():
        data = request.get_json()
        transaction_id = data.get('transaction_id')
        transaction_info = blockchain_instance.transaction_history.get_transaction(transaction_id)
        if isinstance(transaction_info, dict):

            return jsonify({'message': 'transaction info retrieved succesfully', 'transaction_info': transaction_info}), 200
        
        else:
            return jsonify({'message': 'could not find transaction id'}), 404
    
    @app.route('/wallet', methods=['GET'])
    def get_balance():
        data = request.get_json()
        person = data.get('person')
        balance = blockchain_instance.wallet_manager.get_balance(person)

        if isinstance(balance, float):
            return jsonify({'message': f"balance found for {person}", 'balance': balance}), 200
        
        else:
            return jsonify({'message': f"could not find wallet for {person}"}), 404


    return app
