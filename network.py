from node import receive_transaction

def broadcast_transaction(tx, network_nodes):
    for node in network_nodes:
        node.receive_transaction(tx)
