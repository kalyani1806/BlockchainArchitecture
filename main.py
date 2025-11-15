from transaction import Transaction
from node import receive_transaction
from ledger import ledger

# Create some example transactions
tx1 = Transaction("Alice", "Bob", 50, "tx001")
tx2 = Transaction("Alice", "Charlie", 30, "tx002")

# Simulate nodes
node1 = type('Node', (), {"receive_transaction": receive_transaction})()
node2 = type('Node', (), {"receive_transaction": receive_transaction})()
network_nodes = [node1, node2]

# Broadcast transactions
from network import broadcast_transaction
broadcast_transaction(tx1, network_nodes)
broadcast_transaction(tx2, network_nodes)

# Print ledger
for tx in ledger:
     print(tx.sender, "->", tx.receiver, ":", tx.amount)