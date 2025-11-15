# BlockchainArchitecture
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Project README - Decentralized Double-Spending Prevention Protocol</title>
    <style>
        body {
            font-family: "Times New Roman", serif;
            background-color: #f9f9f9;
            color: #333;
            margin: 40px;
            line-height: 1.6;
        }
        .container {
            background-color: #fff;
            padding: 30px 40px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            max-width: 900px;
            margin: auto;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        pre {
            background-color: #eee;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
            font-family: Consolas, monospace;
            font-size: 14px;
        }
        .section {
            margin-bottom: 25px;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            font-size: 0.9em;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Decentralized Double-Spending Prevention Protocol</h1>

        <div class="section">
            <h2>Project Overview</h2>
            <p>
                This project demonstrates a decentralized protocol to prevent the same digital asset from being spent more than once. 
                Transactions are validated by multiple nodes in a peer-to-peer network, and consensus ensures that double spending is avoided without any central authority.
            </p>
        </div>

        <div class="section">
            <h2>Features</h2>
            <ul>
                <li>Decentralized transaction validation</li>
                <li>Double-spending prevention using a distributed ledger</li>
                <li>Consensus mechanism to confirm transactions</li>
                <li>Simulation of network nodes broadcasting transactions</li>
            </ul>
        </div>

        <div class="section">
            <h2>Project Structure</h2>
            <ul>
                <li>transaction.py - Defines the Transaction class</li>
                <li>ledger.py - Maintains the ledger and calculates balances</li>
                <li>node.py - Node logic including validation, mempool, and consensus</li>
                <li>network.py - Handles transaction broadcasting</li>
                <li>main.py - Driver script to test transactions and print the ledger</li>
                <li>flowchart.png/pdf - Flowchart of the protocol (optional)</li>
            </ul>
        </div>

        <div class="section">
            <h2>How the Protocol Works</h2>
            <ol>
                <li>User creates a transaction with sender, receiver, amount, and unique ID</li>
                <li>Transaction is broadcast to all nodes</li>
                <li>Nodes validate against ledger and mempool to prevent double spending</li>
                <li>Validated transactions are added to mempool</li>
                <li>Consensus confirms the transaction</li>
                <li>Transaction is added to the ledger permanently</li>
            </ol>
        </div>

        <div class="section">
            <h2>Example Output</h2>
            <pre>
Alice -> Bob : 50
Alice -> Charlie : 30
            </pre>
        </div>

        <div class="section">
            <h2>Embedded HTML Code</h2>
            <p>Below is the HTML code for this project README:</p>
            <pre>
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Decentralized Double-Spending Prevention Protocol&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Project README&lt;/h1&gt;
    &lt;p&gt;This is an example of embedding HTML code in the README.&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
            </pre>
        </div>

        <div class="section">
            <h2>How to Run</h2>
            <ol>
                <li>Install Python 3.x</li>
                <li>Place all files in the same folder</li>
                <li>Run <code>python main.py</code> to test transactions</li>
                <li>View the ledger in the console</li>
            </ol>
        </div>

        <div class="section">
            <h2>Conclusion</h2>
            <p>
                This project simulates a decentralized network capable of preventing double-spending. 
                It illustrates core blockchain principles including transaction validation, distributed consensus, and ledger maintenance.
            </p>
        </div>

        <div class="footer">
            &copy; 2025 Decentralized Transaction Protocol Project
        </div>
    </div>
</body>
</html>

