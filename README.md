# BlockchainArchitecture
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Decentralized Double-Spending Prevention Protocol</title>
  <style>
    :root{
      --bg:#0f172a; --card:#0b1220; --muted:#94a3b8; --accent:#7c3aed; --glass:rgba(255,255,255,0.04);
      --radius:14px;
      color-scheme: dark;
    }
    *{box-sizing:border-box}
    body{font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial; margin:0; background:linear-gradient(180deg,#071129 0%, #081229 60%); color:#e6eef8; -webkit-font-smoothing:antialiased; -moz-osx-font-smoothing:grayscale}
    .container{max-width:980px;margin:40px auto;padding:28px}
    header{display:flex;align-items:center;gap:18px;margin-bottom:22px}
    .logo{width:64px;height:64px;border-radius:12px;background:linear-gradient(135deg,var(--accent),#2dd4bf);display:flex;align-items:center;justify-content:center;font-weight:700;color:#021025;box-shadow:0 6px 18px rgba(124,58,237,0.14)}
    h1{font-size:22px;margin:0}
    p.lead{color:var(--muted);margin:6px 0 0}

    .card{background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));padding:20px;border-radius:var(--radius);box-shadow:0 6px 30px rgba(2,6,23,0.6);margin-bottom:16px}
    .grid{display:grid;grid-template-columns:1fr 320px;gap:18px}
    @media (max-width:880px){.grid{grid-template-columns:1fr}}
    h2{margin:0 0 10px}
    ul{margin:10px 0 0;padding-left:18px;color:var(--muted)}
    li{margin:6px 0}

    .section-title{display:flex;align-items:center;gap:10px}
    .muted{color:var(--muted);font-size:14px}

    pre{background:var(--glass);border-radius:10px;padding:12px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px;color:#dff3ff;overflow:auto}
    .code-meta{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
    .btn{background:linear-gradient(90deg,var(--accent),#06b6d4);border:none;color:#021025;padding:8px 12px;border-radius:9px;font-weight:600;cursor:pointer}
    .footer{color:var(--muted);font-size:13px;margin-top:6px}

    nav.kv{display:flex;gap:12px;flex-wrap:wrap;margin-top:12px}
    nav a{padding:8px 12px;border-radius:10px;background:rgba(255,255,255,0.02);color:var(--muted);text-decoration:none;font-size:13px}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">D</div>
      <div>
        <h1>Decentralized Double-Spending Prevention Protocol</h1>
        <p class="lead">A simple, readable simulation showing how a peer-to-peer network prevents double spending without a central authority.</p>
      </div>
    </header>

    <div class="grid">
      <main>
        <section class="card">
          <div class="section-title"><h2>Project Overview</h2></div>
          <p class="muted">This project simulates a decentralized protocol that prevents the same digital asset from being spent more than once. It uses a peer-to-peer network of validating nodes and a shared ledger to confirm transactions.</p>
        </section>

        <section class="card">
          <div class="section-title"><h2>Problem Addressed</h2></div>
          <p class="muted">Double spending is the attempt to use the same digital token in more than one transaction. Without central validation, it's difficult to stop. This simulation demonstrates how a decentralized network can guard against that risk by validating transactions collectively and recording them on a shared ledger.</p>
        </section>

        <section class="card">
          <div class="section-title"><h2>Key Features</h2></div>
          <ul>
            <li><strong>Decentralized validation</strong> — transactions are verified by multiple nodes.</li>
            <li><strong>Double-spending prevention</strong> — checks against ledger & mempool before acceptance.</li>
            <li><strong>Consensus mechanism</strong> — nodes agree before confirming.</li>
            <li><strong>Distributed ledger</strong> — shared, append-only record of confirmed transactions.</li>
            <li><strong>Network simulation</strong> — demonstrates broadcasting and consensus without a central server.</li>
          </ul>
        </section>

        <section class="card">
          <div class="section-title"><h2>How the Protocol Works</h2></div>
          <ol class="muted" style="margin-left:18px">
            <li>A user creates a transaction with sender, receiver, amount, and a unique transaction ID.</li>
            <li>The transaction is broadcast to all nodes in the network.</li>
            <li>Each node validates the transaction against its ledger and mempool.</li>
            <li>Valid transactions are stored in the node’s mempool.</li>
            <li>A consensus mechanism confirms the transaction when enough nodes agree.</li>
            <li>The confirmed transaction is permanently added to the ledger.</li>
          </ol>

          <div style="margin-top:12px">
            <div class="code-meta"><strong>Sample transaction (JSON)</strong><button class="btn" id="copyTx">Copy</button></div>
            <pre id="sample">{
  "txid": "b1f5c8...",
  "sender": "Alice",
  "receiver": "Bob",
  "amount": 10.0,
  "timestamp": "2025-11-15T12:34:56Z",
  "signature": "MEUCIQ..."
}</pre>
          </div>
        </section>

        <section class="card">
          <div class="section-title"><h2>Applications</h2></div>
          <ul>
            <li>Cryptocurrency systems like Bitcoin and Ethereum (conceptual similarities).</li>
            <li>Decentralized digital payment platforms.</li>
            <li>Tokenized assets where preventing double-spend is critical (NFTs, vouchers).</li>
          </ul>
        </section>

        <section class="card">
          <div class="section-title"><h2>Conclusion</h2></div>
          <p class="muted">This simulation illustrates how decentralized networks use transaction validation, mempool checks, consensus, and a distributed ledger to prevent double spending without a central authority. It's a practical demonstration of core blockchain principles and can be extended into a full prototype or educational demo.</p>
        </section>

      </main>

      <aside>
        <div class="card">
          <h3>Quick Links</h3>
          <nav class="kv">
            <a href="#">Overview</a>
            <a href="#">How it works</a>
            <a href="#">Sample data</a>
            <a href="#">Applications</a>
          </nav>
          <p class="footer">Tip: copy the sample transaction and paste it into your simulator's broadcast routine.</p>
        </div>

        <div class="card">
          <h3>Notes for Developers</h3>
          <ul>
            <li class="muted">Use deterministic txid generation (SHA-256 of tx payload).</li>
            <li class="muted">Validate signatures and nonce/timestamp to prevent replay.</li>
            <li class="muted">Implement mempool checks to disallow conflicting spends.</li>
            <li class="muted">Pick a consensus strategy that fits your simulation (voting, PoW lite, PBFT, etc.).</li>
          </ul>
        </div>

        <div class="card">
          <h3>Export</h3>
          <p class="muted">You can save this HTML file, open it in a browser, or adapt components into a static site for demos.</p>
        </div>
      </aside>
    </div>

    <footer style="text-align:center;margin-top:18px;color:var(--muted)">Made for instructional/demo use — not production. © 2025</footer>
  </div>

  <script>
    document.getElementById('copyTx').addEventListener('click', async function(){
      const text = document.getElementById('sample').innerText;
      try{await navigator.clipboard.writeText(text); this.innerText='Copied'; setTimeout(()=>this.innerText='Copy',1200)}catch(e){alert('Copy failed: '+e)}
    });
  </script>
</body>
</html>
