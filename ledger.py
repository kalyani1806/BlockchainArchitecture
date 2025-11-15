ledger = []

def calculate_balance(user):
    balance = 0
    for tx in ledger:
        if tx.receiver == user:
            balance += tx.amount
        if tx.sender == user:
            balance -= tx.amount
    return balance
