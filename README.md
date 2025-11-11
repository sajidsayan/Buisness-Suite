<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mega Business Suite Pro</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #333;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            padding: 40px 20px;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }

        .header h1 {
            font-size: 3.5em;
            color: #2c3e50;
            margin-bottom: 10px;
            background: linear-gradient(45deg, #2c3e50, #3498db);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .header h2 {
            font-size: 1.5em;
            color: #7f8c8d;
            font-weight: 300;
        }

        .badges {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 20px 0;
            flex-wrap: wrap;
        }

        .badge {
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: 600;
            color: white;
        }

        .badge.python { background: #3776ab; }
        .badge.ui { background: #27ae60; }
        .badge.database { background: #e74c3c; }
        .badge.license { background: #9b59b6; }
        .badge.platform { background: #34495e; }

        .nav-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 20px 0;
            flex-wrap: wrap;
        }

        .nav-link {
            padding: 10px 20px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 25px;
            transition: all 0.3s ease;
            font-weight: 600;
        }

        .nav-link:hover {
            background: #2980b9;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }

        .section {
            background: rgba(255, 255, 255, 0.95);
            margin: 30px 0;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        .section h2 {
            color: #2c3e50;
            margin-bottom: 20px;
            font-size: 2.2em;
            border-left: 5px solid #3498db;
            padding-left: 15px;
        }

        .section h3 {
            color: #34495e;
            margin: 25px 0 15px 0;
            font-size: 1.5em;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }

        .feature-card {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #3498db;
            transition: transform 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-icon {
            font-size: 2.5em;
            margin-bottom: 15px;
        }

        .feature-card h4 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 1.3em;
        }

        .modules-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .modules-table th {
            background: #3498db;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }

        .modules-table td {
            padding: 15px;
            border-bottom: 1px solid #ecf0f1;
        }

        .modules-table tr:hover {
            background: #f8f9fa;
        }

        .status-complete {
            background: #27ae60;
            color: white;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 0.8em;
            font-weight: 600;
        }

        .code-block {
            background: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            font-family: 'Courier New', monospace;
            overflow-x: auto;
        }

        .install-steps {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 4px solid #3498db;
        }

        .step {
            margin: 15px 0;
            padding-left: 20px;
            position: relative;
        }

        .step:before {
            content: "▶";
            position: absolute;
            left: 0;
            color: #3498db;
            font-weight: bold;
        }

        .file-structure {
            background: #34495e;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 10px;
            font-family: 'Courier New', monospace;
            margin: 20px 0;
        }

        .file-item {
            margin: 5px 0;
            padding-left: 20px;
        }

        .folder:before {
            content: "📁 ";
        }

        .file:before {
            content: "📄 ";
        }

        .footer {
            text-align: center;
            padding: 40px 20px;
            color: white;
            margin-top: 50px;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2.5em;
            }
            
            .features-grid {
                grid-template-columns: 1fr;
            }
            
            .nav-links {
                flex-direction: column;
                align-items: center;
            }
            
            .nav-link {
                width: 200px;
                text-align: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏢 Mega Business Suite Pro</h1>
            <h2>Complete All-in-One Business Management Software</h2>
            
            <div class="badges">
                <div class="badge python">Python 3.8+</div>
                <div class="badge ui">CustomTkinter UI</div>
                <div class="badge database">SQLite Database</div>
                <div class="badge license">MIT License</div>
                <div class="badge platform">Multi-Platform</div>
            </div>

            <div class="nav-links">
                <a href="#features" class="nav-link">🚀 Features</a>
                <a href="#installation" class="nav-link">📦 Installation</a>
                <a href="#modules" class="nav-link">📊 Modules</a>
                <a href="#usage" class="nav-link">🎯 Usage</a>
                <a href="#technical" class="nav-link">🔧 Technical</a>
            </div>
        </div>

        <!-- Features Section -->
        <div id="features" class="section">
            <h2>🌟 Key Features</h2>
            
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">📊</div>
                    <h4>Real-time Dashboard</h4>
                    <p>Live business overview with KPIs, activity feed, and quick stats monitoring</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">👥</div>
                    <h4>CRM System</h4>
                    <p>Complete customer management with contact tracking and communication history</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">💰</div>
                    <h4>Accounting</h4>
                    <p>Financial tracking, income/expense management, and comprehensive reporting</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">📦</div>
                    <h4>Inventory Management</h4>
                    <p>Stock tracking, low stock alerts, and supplier management system</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">👨‍💼</div>
                    <h4>HR Management</h4>
                    <p>Employee records, payroll, attendance, and performance tracking</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">📋</div>
                    <h4>Project Management</h4>
                    <p>Kanban board, task tracking, team collaboration, and progress monitoring</p>
                </div>
            </div>
        </div>

        <!-- Installation Section -->
        <div id="installation" class="section">
            <h2>📦 Installation Guide</h2>
            
            <h3>System Requirements</h3>
            <ul>
                <li><strong>Python:</strong> 3.8 or higher</li>
                <li><strong>RAM:</strong> 4GB minimum, 8GB recommended</li>
                <li><strong>Storage:</strong> 500MB free space</li>
                <li><strong>OS:</strong> Windows 10+, macOS 10.14+, Ubuntu 18.04+</li>
            </ul>

            <h3>Quick Installation</h3>
            <div class="install-steps">
                <div class="step">Clone the repository</div>
                <div class="code-block">
git clone https://github.com/yourusername/mega-business-suite.git<br>
cd mega-business-suite
                </div>

                <div class="step">Run automatic installer</div>
                <div class="code-block">python install.py</div>

                <div class="step">Launch the application</div>
                <div class="code-block">python main.py</div>
            </div>

            <h3>Manual Installation</h3>
            <div class="code-block">
# Install dependencies<br>
pip install -r requirements.txt<br><br>

# Create necessary directories<br>
mkdir -p data exports backups assets/icons<br><br>

# Initialize database<br>
python -c "from data.database import BusinessDatabase; BusinessDatabase()"
            </div>
        </div>

        <!-- Modules Section -->
        <div id="modules" class="section">
            <h2>📊 Business Modules</h2>
            
            <table class="modules-table">
                <thead>
                    <tr>
                        <th>Module</th>
                        <th>Icon</th>
                        <th>Description</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Dashboard</strong></td>
                        <td>📊</td>
                        <td>Real-time business overview with KPIs and analytics</td>
                        <td><span class="status-complete">Complete</span></td>
                    </tr>
                    <tr>
                        <td><strong>CRM</strong></td>
                        <td>👥</td>
                        <td>Customer relationship management and contact tracking</td>
                        <td><span class="status-complete">Complete</span></td>
                    </tr>
                    <tr>
                        <td><strong>Accounting</strong></td>
                        <td>💰</td>
                        <td>Financial management with income/expense tracking</td>
                        <td><span class="status-complete">Complete</span></td>
                    </tr>
                    <tr>
                        <td><strong>Inventory</strong></td>
                        <td>📦</td>
                        <td>Stock management with alerts and supplier tracking</td>
                        <td><span class="status-complete">Complete</span></td>
                    </tr>
                    <tr>
                        <td><strong>HR Management</strong></td>
                        <td>👨‍💼</td>
                        <td>Employee records, payroll, and performance management</td>
                        <td><span class="status-complete">Complete</span></td>
                    </tr>
                    <tr>
                        <td><strong>Projects</strong></td>
                        <td>📋</td>
                        <td>Project tracking with Kanban board and task management</td>
                        <td><span class="status-complete">Complete</span></td>
                    </tr>
                    <tr>
                        <td><strong>Analytics</strong></td>
                        <td>📈</td>
                        <td>Business intelligence with charts and reporting</td>
                        <td><span class="status-complete">Complete</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Usage Section -->
        <div id="usage" class="section">
            <h2>🎯 Quick Start Guide</h2>
            
            <h3>First Time Setup</h3>
            <div class="install-steps">
                <div class="step">Launch the application</div>
                <div class="code-block">python main.py</div>
                
                <div class="step">Explore the Dashboard for business overview</div>
                <div class="step">Generate sample data using "Generate Sample" buttons</div>
                <div class="step">Navigate between modules using the sidebar</div>
                <div class="step">Start adding your actual business data</div>
            </div>

            <h3>Basic Workflow</h3>
            <ol>
                <li>Add customers in CRM module</li>
                <li>Create products in Inventory module</li>
                <li>Record transactions in Accounting module</li>
                <li>Manage projects in Projects module</li>
                <li>View reports in Analytics module</li>
            </ol>
        </div>

        <!-- Technical Section -->
        <div id="technical" class="section">
            <h2>🔧 Technical Details</h2>
            
            <h3>Architecture</h3>
            <div class="code-block">
Application Layer (CustomTkinter UI)<br>
    ↓<br>
Business Logic Layer (Python Modules)<br>
    ↓<br>
Data Access Layer (SQLite Database)<br>
    ↓<br>
Storage Layer (Local Filesystem)
            </div>

            <h3>File Structure</h3>
            <div class="file-structure">
                <div class="file-item folder">mega-business-suite/</div>
                <div class="file-item file">main.py</div>
                <div class="file-item file">install.py</div>
                <div class="file-item file">requirements.txt</div>
                <div class="file-item folder">modules/</div>
                <div class="file-item file" style="margin-left: 20px;">crm.py</div>
                <div class="file-item file" style="margin-left: 20px;">accounting.py</div>
                <div class="file-item file" style="margin-left: 20px;">inventory.py</div>
                <div class="file-item file" style="margin-left: 20px;">hr.py</div>
                <div class="file-item file" style="margin-left: 20px;">projects.py</div>
                <div class="file-item file" style="margin-left: 20px;">analytics.py</div>
                <div class="file-item folder">ui/</div>
                <div class="file-item file" style="margin-left: 20px;">components.py</div>
                <div class="file-item file" style="margin-left: 20px;">themes.py</div>
                <div class="file-item folder">data/</div>
                <div class="file-item file" style="margin-left: 20px;">database.py</div>
                <div class="file-item folder">assets/</div>
                <div class="file-item folder">exports/</div>
                <div class="file-item folder">backups/</div>
            </div>

            <h3>Database Schema</h3>
            <div class="code-block">
-- Core Business Tables<br>
CREATE TABLE customers (<br>
&nbsp;&nbsp;&nbsp;&nbsp;id INTEGER PRIMARY KEY,<br>
&nbsp;&nbsp;&nbsp;&nbsp;name TEXT NOT NULL,<br>
&nbsp;&nbsp;&nbsp;&nbsp;email TEXT UNIQUE,<br>
&nbsp;&nbsp;&nbsp;&nbsp;phone TEXT,<br>
&nbsp;&nbsp;&nbsp;&nbsp;company TEXT,<br>
&nbsp;&nbsp;&nbsp;&nbsp;status TEXT DEFAULT 'Active'<br>
);<br><br>

CREATE TABLE transactions (<br>
&nbsp;&nbsp;&nbsp;&nbsp;id INTEGER PRIMARY KEY,<br>
&nbsp;&nbsp;&nbsp;&nbsp;type TEXT NOT NULL,<br>
&nbsp;&nbsp;&nbsp;&nbsp;amount REAL NOT NULL,<br>
&nbsp;&nbsp;&nbsp;&nbsp;description TEXT,<br>
&nbsp;&nbsp;&nbsp;&nbsp;category TEXT,<br>
&nbsp;&nbsp;&nbsp;&nbsp;date TIMESTAMP DEFAULT CURRENT_TIMESTAMP<br>
);
            </div>
        </div>

        <div class="footer">
            <h3>Mega Business Suite Pro</h3>
            <p>Complete Business Management Solution</p>
            <p>© 2024 All Rights Reserved | MIT License</p>
        </div>
    </div>

    <script>
        // Smooth scrolling for navigation links
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                const targetSection = document.querySelector(targetId);
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            });
        });

        // Add animation to feature cards on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe feature cards
        document.querySelectorAll('.feature-card').forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(card);
        });
    </script>
</body>
</html>
