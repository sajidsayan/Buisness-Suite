import sqlite3
import json
from datetime import datetime
import pandas as pd

class BusinessDatabase:
    def __init__(self, db_path="data/business_suite.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize all database tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Customers table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                company TEXT,
                status TEXT DEFAULT 'Active',
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_contact TIMESTAMP,
                notes TEXT
            )
        ''')
        
        # Transactions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL CHECK(type IN ('income', 'expense')),
                amount REAL NOT NULL,
                description TEXT,
                category TEXT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                reference TEXT,
                status TEXT DEFAULT 'completed'
            )
        ''')
        
        # Products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sku TEXT UNIQUE,
                price REAL NOT NULL,
                cost REAL,
                quantity INTEGER DEFAULT 0,
                min_stock INTEGER DEFAULT 5,
                category TEXT,
                supplier TEXT,
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Employees table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                position TEXT,
                department TEXT,
                salary REAL,
                hire_date TEXT,
                status TEXT DEFAULT 'Active',
                manager_id INTEGER,
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Projects table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'planning',
                priority TEXT DEFAULT 'Medium',
                start_date TEXT,
                end_date TEXT,
                budget REAL,
                actual_cost REAL DEFAULT 0,
                progress INTEGER DEFAULT 0,
                manager_id INTEGER,
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Invoices table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS invoices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                invoice_number TEXT UNIQUE,
                customer_id INTEGER,
                amount REAL,
                status TEXT DEFAULT 'draft',
                due_date TEXT,
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customers (id)
            )
        ''')
        
        # Settings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def get_connection(self):
        """Get database connection"""
        return sqlite3.connect(self.db_path)
    
    def execute_query(self, query, params=()):
        """Execute a query and return results"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        return result
    
    def get_customers(self, status=None):
        """Get all customers or filtered by status"""
        if status:
            return self.execute_query("SELECT * FROM customers WHERE status = ?", (status,))
        return self.execute_query("SELECT * FROM customers ORDER BY created_date DESC")
    
    def get_financial_summary(self):
        """Get financial summary"""
        conn = self.get_connection()
        
        # Total income
        income_result = self.execute_query("SELECT SUM(amount) FROM transactions WHERE type = 'income'")
        total_income = income_result[0][0] or 0
        
        # Total expenses
        expense_result = self.execute_query("SELECT SUM(amount) FROM transactions WHERE type = 'expense'")
        total_expenses = expense_result[0][0] or 0
        
        # Monthly breakdown
        monthly_data = self.execute_query('''
            SELECT strftime('%Y-%m', date) as month, 
                   type,
                   SUM(amount) as total
            FROM transactions 
            GROUP BY month, type
            ORDER BY month DESC
            LIMIT 12
        ''')
        
        return {
            'total_income': total_income,
            'total_expenses': total_expenses,
            'net_profit': total_income - total_expenses,
            'monthly_data': monthly_data
        }
    
    def get_low_stock_products(self):
        """Get products with low stock"""
        return self.execute_query('''
            SELECT * FROM products 
            WHERE quantity <= min_stock 
            ORDER BY quantity ASC
        ''')
    
    def export_to_csv(self, table_name):
        """Export table data to CSV"""
        conn = self.get_connection()
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        filename = f"exports/{table_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(filename, index=False)
        conn.close()
        return filename
    
    def backup_database(self):
        """Create database backup"""
        import shutil
        backup_file = f"backups/business_suite_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
        shutil.copy2(self.db_path, backup_file)
        return backup_file