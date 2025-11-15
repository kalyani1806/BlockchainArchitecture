from transaction import Transaction
from ledger import ledger, calculate_balance

mempool = []
REQUIRED_CONFIRMATIONS = 2  # Example threshold

def validate_transaction(tx):
    if calculate_balance(tx.sender) < tx.amount:
        return False
    for confirmed_tx in ledger:
        if confirmed_tx.tx_id == tx.tx_id:
            return False
    return True

def receive_transaction(tx):
    if validate_transaction(tx):
        mempool.append(tx)
        if consensus(mempool):
            ledger.append(tx)
            mempool.remove(tx)

def consensus(transactions):
    return len(transactions) >= REQUIRED_CONFIRMATIONS
