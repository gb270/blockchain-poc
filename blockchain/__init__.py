from .blockchain import Blockchain
from .block import Block

# create global instance of blockchain for across project
blockchain_instance = Blockchain()

__all__ = ['Block', 'Blockchain']