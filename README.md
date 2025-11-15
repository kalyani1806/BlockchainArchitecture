# BlockchainArchitecture
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Decentralized Double-Spending Prevention Protocol</title>
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
        h1 {
            text-align: center;
            margin-bottom: 30px;
        }
        ul, ol {
            margin-top: 0;
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
                This project demonstrates a <strong>decentralized protocol</strong> designed to prevent the same digital asset from being spent more than once. 
                Unlike traditional centralized systems, this protocol relies on a <strong>peer-to-peer network of nodes</strong> to validate transactions and maintain a shared ledger, eliminating the need for a central authority.
            </p>
        </div>

        <div class="section">
            <h2>Problem Addressed</h2>
            <p>
                In digital transactions, a major challenge is <strong>double spending</strong>, where a user tries to spend the same digital currency multiple times. 
                Without a central system to verify each transaction, it becomes difficult to prevent fraud. 
                This project simulates a solution for that problem using a decentralized network.
            </p>
        </div>

        <div class="section">
            <h2>Key Features</h2>
            <ul>
                <li>Decentralized validation: Transactions are verified by multiple nodes in the network.</li>
                <li>Double-spending prevention: Each transaction is checked against the ledger and mempool to ensure the same digital asset is not spent twice.</li>
                <li>Consensus mechanism: Nodes reach agreement before confirming transactions to make the system reliable and secure.</li>
                <li>Distributed ledger: The network maintains a shared ledger of all confirmed transactions, which is publicly verifiable.</li>
                <li>Simulation of a network: Demonstrates transaction broadcasting and consensus among nodes without a central server.</li>
            </ul>
        </div>

        <div class="section">
            <h2>How the Protocol Works</h2>
            <ol>
                <li>A user creates a transaction specifying the sender, receiver, amount, and a unique transaction ID.</li>
                <li>The transaction is broadcast to all nodes in the network.</li>
                <li>Each node validates the transaction against its ledger and mempool.</li>
                <li>Valid transactions are temporarily stored in the node’s mempool.</li>
                <li>A consensus mechanism confirms the transaction when enough nodes agree.</li>
                <li>The confirmed transaction is permanently added to the ledger.</li>
            </ol>
        </div>

        <div class="section">
            <h2>Applications</h2>
            <ul>
                <li>Cryptocurrency systems like Bitcoin and Ethereum.</li>
                <li>Any decentralized digital payment system.</li>
                <li>Preventing fraud in digital assets and tokens.</li>
            </ul>
        </div>

        <div class="section">
            <h2>Conclusion</h2>
            <p>
                This project successfully simulates a <strong>decentralized double-spending prevention system</strong>. 
                It shows how transactions can be validated and confirmed in a peer-to-peer network without relying on a central authority. 
                The simulation demonstrates core blockchain principles like <strong>transaction validation, consensus, and ledger maintenance</strong>, providing a practical understanding of decentralized digital currency systems.
            </p>
        </div>

        <div class="footer">
            &copy; 2025 Decentralized Transaction Protocol Project
        </div>
    </div>
</body>
</html>

