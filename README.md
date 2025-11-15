# BlockchainArchitecture
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Decentralized Double-Spending Prevention Protocol</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2 {
            color: #2c3e50;
        }
        code {
            background-color: #eee;
            padding: 2px 5px;
            border-radius: 4px;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
        }
        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        ul {
            margin-top: 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Decentralized Double-Spending Prevention Protocol</h1>

        <h2>Project Overview</h2>
        <p>
            This project implements a <strong>decentralized protocol</strong> that prevents the same digital asset from being spent more than once. 
            The system simulates a peer-to-peer network where nodes validate transactions, maintain a ledger, and reach consensus without relying on a central authority.
        </p>

        <h2>Features</h2>
        <ul>
            <li>Decentralized transaction validation without a central server.</li>
            <li>Double-spending prevention using a distributed ledger.</li>
            <li>Consensus mechanism for confirming transactions.</li>
            <li>Simulated network nodes and transaction broadcasting.</li>
        </ul>

        <h2>Project Structure</h2>
        <ul>
            <li><code>transaction.py</code>: Defines the Transaction class.</li>
            <li><code>ledger.py</code>: Maintains the ledger and calculates user balances.</li>
            <li><code>node.py</code>: Node logic including transaction validation, mempool, and consensus.</li>
            <li><code>network.py</code>: Broadcast transactions to all nodes in the network.</li>
            <li><code>main.py</code>: Driver code to test transactions and print the ledger.</li>
            <li><code>flowchart.pdf</code> (optional): Diagram showing the transaction flow and validation process.</li>
        </ul>

        <h2>How It Works</h2>
        <ol>
            <li>User creates a transaction specifying sender, receiver, amount, and a unique transaction ID.</li>
            <li>The transaction is broadcast to all nodes in the network.</li>
            <li>Each node validates the transaction against its ledger to ensure the sender has enough balance and that the transaction is not already spent.</li>
            <li>Validated transactions are added to the node's mempool.</li>
            <li>Consensus is reached when the transaction is confirmed by enough nodes.</li>
            <li>The confirmed transaction is added to the ledger and is visible to all nodes.</li>
        </ol>

        <h2>Example Output</h2>
        <pre>
Alice -> Bob : 50
Alice -> Charlie : 30
        </pre>

        <h2>How to Run</h2>
        <ol>
            <li>Ensure Python 3.x is installed.</li>
            <li>Place all project files in the same folder.</li>
            <li>Run the driver script: <code>python main.py</code></li>
            <li>Observe the ledger printed in the console.</li>
        </ol>

        <h2>Conclusion</h2>
        <p>
            This project demonstrates how a decentralized network can prevent double-spending using transaction validation and consensus, 
            all without relying on a central authority. It is a simplified simulation of blockchain principles.
        </p>
    </div>
</body>
</html>

