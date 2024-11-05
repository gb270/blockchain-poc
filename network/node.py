"""
Here we will start off with basic logic.
The idea is that users can broadcast to a pool. (we can handle all this
logic using the API that will store all this info for testing)
Nodes then take transactions from this pool and verify that they are legitimate
by doing three things:
1. Check the signature verification
2. Prevent double spending
3. Ensure the transaction follows the correct structure.

If this is correct they can either broadcast this to other nodes or add a block
to the blockchain.

To add a block to the blockchain we need to mine it. This is where the 
conensus mechanism comes into play. 
For this PoC we will start off by working with a PoW consensus mechanism
and ask the users to solve a much simpler cryptographic problem (just for demo purposes)
then later on we can explore ways to find solutions that more directly
and naturally avoid 51% attacks.

When a node receives a new block it must validate it before adding it to its
own blockchain.
1. Verify all transactions are legitimate
2. Confirm PoW.
3. Ensure that the previous_hash in the new block matches the latest block
in the chain.

In order to ensure integrity, nodes reject invalid chains and they only accept
the longest chain rule (for now, this strategy is suceptible to 51% attack
so we may explore other options in the future.)

"""

