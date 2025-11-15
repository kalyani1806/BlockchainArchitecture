class Transaction:
    def __init__(self, sender, receiver, amount, tx_id):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.tx_id = tx_id
