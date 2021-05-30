class Block:
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """
    def __init__(self, data):
        self.data = data


class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - datasets of transactions
    """
    def __init__(self):
        self.chain = []
    
    def add_block(self, data):
        self.chain.append(Block(data))
    