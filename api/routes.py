from flask import Flask, jsonify, request


def setup_routes():

    app = Flask(__name__)
    
    @app.route('/chain', methods=['GET'])
    def get_full_chain():
        """Get the full blockchain"""
        # how to handle multiple chians?
        # maybe this one just returns longest one and we have different 
        # function to display all?
        pass

    @app.route('/transaction', methods=['POST'])
    def create_transaction():
        """Add a new transaction to the blockchain"""
        pass

    @app.route('/mine', methods =['POST'])
    def mine():
        """Mine a new block in the blockchain"""
        # might need to pass some parameters here?
        pass

    @app.route('/pool', methods=['GET'])
    def get_transaction_pool():
        """Returns all transactions currently in pool. 
            I.e. not in current users blockchain.
        """
        pass
        # need way of inputting then users blockchain so they can see
        # all the transactions that they don't have.

    return app
