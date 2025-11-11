<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mega Business Suite Pro</title>
  <style>
    /* --- RESET & BASE --- */
    * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    html, body { height: 100%; scroll-behavior: smooth; }
    body {
      background: linear-gradient(135deg, #1e3c72, #2a5298);
      color: #333;
      overflow-x: hidden;
    }
    ::selection { background: #3498db; color: #fff; }

    /* --- PARALLAX BACKGROUND --- */
    body::before {
      content: "";
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: radial-gradient(circle at 20% 20%, rgba(52,152,219,0.3), transparent 60%),
                  radial-gradient(circle at 80% 80%, rgba(41,128,185,0.2), transparent 60%);
      z-index: -1;
      animation: moveBg 10s infinite alternate ease-in-out;
    }
    @keyframes moveBg {
      0% { background-position: 20% 20%, 80% 80%; }
      100% { background-position: 30% 30%, 70% 70%; }
    }

    /* --- HEADER --- */
    header {
      text-align: center;
      padding: 80px 20px 60px;
      color: #fff;
      position: relative;
    }
    header h1 {
      font-size: 3.8em;
      background: linear-gradient(90deg, #fff, #8ec5fc, #e0c3fc);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: shine 4s linear infinite;
    }
    @keyframes shine {
      0% { background-position: 0% 50%; }
      100% { background-position: 100% 50%; }
    }
    header h2 {
      font-size: 1.4em;
      font-weight: 300;
      color: #ecf0f1;
      margin-top: 10px;
    }

    /* --- BADGES --- */
    .badges {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      margin-top: 25px;
    }
    .badge {
      padding: 8px 14px;
      border-radius: 20px;
      color: #fff;
      font-weight: 600;
      font-size: 0.9em;
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .python { background: #3776ab; }
    .ui { background: #27ae60; }
    .database { background: #e74c3c; }
    .license { background: #9b59b6; }
    .platform { background: #34495e; }

    /* --- NAVIGATION --- */
    nav {
      position: sticky;
      top: 0;
      background: rgba(255,255,255,0.15);
      backdrop-filter: blur(10px);
      padding: 15px 10px;
      display: flex;
      justify-content: center;
      gap: 15px;
      z-index: 99;
      transition: background 0.3s;
    }
    nav a {
      color: #fff;
      text-decoration: none;
      font-weight: 600;
      padding: 8px 18px;
      border-radius: 20px;
      background: rgba(255,255,255,0.1);
      transition: 0.3s;
    }
    nav a:hover {
      background: #3498db;
      transform: translateY(-2px);
    }

    /* --- SECTION STYLE --- */
    section {
      max-width: 1100px;
      margin: 60px auto;
      background: rgba(255,255,255,0.95);
      border-radius: 20px;
      padding: 40px;
      box-shadow: 0 15px 40px rgba(0,0,0,0.1);
      animation: fadeIn 0.8s ease both;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    section h2 {
      font-size: 2em;
      color: #2c3e50;
      border-left: 6px solid #3498db;
      padding-left: 15px;
      margin-bottom: 20px;
    }

    /* --- GRID FEATURES --- */
    .grid {
      display: grid;
      gap: 20px;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    }
    .card {
      background: white;
      border-radius: 15px;
      padding: 25px;
      border-left: 4px solid #3498db;
      box-shadow: 0 4px 15px rgba(0,0,0,0.08);
      transition: 0.3s;
    }
    .card:hover { transform: translateY(-5px); }
    .card .icon { font-size: 2em; margin-bottom: 10px; }
    .card h4 { color: #2c3e50; margin-bottom: 8px; }

    /* --- TABLE --- */
    table {
      width: 100%;
      border-collapse: collapse;
      background: white;
      margin-top: 20px;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    th {
      background: #3498db;
      color: white;
      text-align: left;
      padding: 14px;
    }
    td {
      padding: 14px;
      border-bottom: 1px solid #ecf0f1;
    }
    tr:hover { background: #f9fbfd; }

    .status { background: #27ae60; color: white; padding: 4px 10px; border-radius: 12px; font-size: 0.8em; }

    /* --- CODE BLOCKS --- */
    pre {
      background: #2c3e50;
      color: #ecf0f1;
      padding: 16px;
      border-radius: 10px;
      font-family: monospace;
      overflow-x: auto;
      margin: 10px 0 25px;
    }

    /* --- FOOTER --- */
    footer {
      text-align: center;
      color: #ecf0f1;
      padding: 40px 20px;
      margin-top: 60px;
    }
    footer p { opacity: 0.9; }

    @media(max-width:768px){
      header h1 { font-size: 2.6em; }
      nav { flex-wrap: wrap; }
    }
  </style>
</head>
<body>

  <header>
    <h1>🏢 Mega Business Suite Pro</h1>
    <h2>All-in-One Modern Business Management Platform</h2>
    <div class="badges">
      <div class="badge python">Python 3.8+</div>
      <div class="badge ui">CustomTkinter UI</div>
      <div class="badge database">SQLite Database</div>
      <div class="badge license">MIT License</div>
      <div class="badge platform">Cross-Platform</div>
    </div>
  </header>

  <nav>
    <a href="#features">🚀 Features</a>
    <a href="#install">📦 Installation</a>
    <a href="#modules">📊 Modules</a>
    <a href="#usage">🎯 Usage</a>
    <a href="#tech">🔧 Technical</a>
  </nav>

  <section id="features">
    <h2>🌟 Key Features</h2>
    <div class="grid">
      <div class="card"><div class="icon">📊</div><h4>Dashboard</h4><p>Real-time KPIs, analytics, and activity tracking.</p></div>
      <div class="card"><div class="icon">👥</div><h4>CRM</h4><p>Customer relationship management and lead pipelines.</p></div>
      <div class="card"><div class="icon">💰</div><h4>Accounting</h4><p>Income, expenses, invoices, and tax reports.</p></div>
      <div class="card"><div class="icon">📦</div><h4>Inventory</h4><p>Stock control, supplier management, low-stock alerts.</p></div>
      <div class="card"><div class="icon">👨‍💼</div><h4>HR</h4><p>Employee data, attendance, payroll, performance.</p></div>
      <div class="card"><div class="icon">📋</div><h4>Projects</h4><p>Kanban workflow, tasks, team collaboration.</p></div>
    </div>
  </section>

  <section id="install">
    <h2>📦 Installation</h2>
    <p><b>Requirements:</b> Python 3.8+, 4GB RAM, 500MB disk, Windows/macOS/Linux</p>
    <pre>
git clone https://github.com/yourusername/mega-business-suite.git
cd mega-business-suite
python install.py
    </pre>
    <p>Or manual setup:</p>
    <pre>
pip install -r requirements.txt
mkdir -p data exports backups assets/icons
python -c "from data.database import BusinessDatabase; BusinessDatabase()"
python main.py
    </pre>
  </section>

  <section id="modules">
    <h2>📊 Modules</h2>
    <table>
      <tr><th>Module</th><th>Icon</th><th>Description</th><th>Status</th></tr>
      <tr><td>Dashboard</td><td>📊</td><td>KPIs & insights</td><td><span class="status">✅ Done</span></td></tr>
      <tr><td>CRM</td><td>👥</td><td>Customer tracking</td><td><span class="status">✅ Done</span></td></tr>
      <tr><td>Accounting</td><td>💰</td><td>Financial tracking</td><td><span class="status">✅ Done</span></td></tr>
      <tr><td>Inventory</td><td>📦</td><td>Stock & suppliers</td><td><span class="status">✅ Done</span></td></tr>
      <tr><td>HR</td><td>👨‍💼</td><td>Employee management</td><td><span class="status">✅ Done</span></td></tr>
      <tr><td>Projects</td><td>📋</td><td>Kanban & tasks</td><td><span class="status">✅ Done</span></td></tr>
      <tr><td>Analytics</td><td>📈</td><td>Reports & charts</td><td><span class="status">✅ Done</span></td></tr>
    </table>
  </section>

  <section id="usage">
    <h2>🎯 Quick Start</h2>
    <pre>
python main.py
    </pre>
    <ul>
      <li>Explore the dashboard overview</li>
      <li>Generate sample data</li>
      <li>Add customers, products, and transactions</li>
      <li>Manage projects and track analytics</li>
    </ul>
  </section>

  <section id="tech">
    <h2>🔧 Technical Overview</h2>
    <pre>
Application Layer (CustomTkinter)
↓
Business Logic Layer (Python)
↓
Data Layer (SQLite)
↓
Storage Layer (Filesystem)
    </pre>
    <pre>
mega-business-suite/
├── main.py
├── install.py
├── modules/
│   ├── crm.py
│   ├── accounting.py
│   ├── inventory.py
│   ├── hr.py
│   ├── projects.py
│   └── analytics.py
└── data/
    └── database.py
    </pre>
  </section>

  <footer>
    <p><b>Mega Business Suite Pro</b> — Complete Business Management Software</p>
    <p>© 2025 All Rights Reserved • MIT License</p>
  </footer>

</body>
</html>
