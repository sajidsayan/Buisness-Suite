import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime, timedelta

class AccountingModule(ctk.CTkFrame):
    def __init__(self, parent, connection):
        super().__init__(parent)
        self.conn = connection
        
        self.setup_ui()
        self.load_transactions()
        
    def setup_ui(self):
        """Setup Accounting UI"""
        # Header with stats
        header = ctk.CTkFrame(self)
        header.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(header, text="💰 Accounting & Finance", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=10, pady=10)
        
        # Quick stats
        stats_frame = ctk.CTkFrame(header)
        stats_frame.pack(fill="x", padx=10, pady=5)
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
        income = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
        expense = cursor.fetchone()[0] or 0
        
        profit = income - expense
        
        stats = [
            ("Total Income", f"${income:,.2f}", "green"),
            ("Total Expenses", f"${expense:,.2f}", "red"), 
            ("Net Profit", f"${profit:,.2f}", "blue" if profit >= 0 else "red")
        ]
        
        for i, (title, value, color) in enumerate(stats):
            stat_card = ctk.CTkFrame(stats_frame, height=80)
            stat_card.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")
            stats_frame.grid_columnconfigure(i, weight=1)
            
            ctk.CTkLabel(stat_card, text=title, font=ctk.CTkFont(size=12)).pack(pady=(10,5))
            ctk.CTkLabel(stat_card, text=value, font=ctk.CTkFont(size=18, weight="bold"), 
                        text_color=color).pack()
        
        # Action buttons
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkButton(btn_frame, text="+ Add Income", command=self.add_income).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="+ Add Expense", command=self.add_expense).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="📊 Reports", command=self.show_reports).pack(side="left", padx=5)
        
        # Transactions table
        self.create_transactions_table()
        
    def create_transactions_table(self):
        """Create transactions table"""
        table_frame = ctk.CTkFrame(self)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        columns = ("ID", "Type", "Amount", "Description", "Category", "Date")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
            
        # Color coding for income/expense
        self.tree.tag_configure('income', background='#d4edda')
        self.tree.tag_configure('expense', background='#f8d7da')
        
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def load_transactions(self):
        """Load transactions from database"""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
        
        for row in cursor.fetchall():
            tag = 'income' if row[1] == 'income' else 'expense'
            self.tree.insert("", "end", values=row, tags=(tag,))
            
    def add_income(self):
        self.add_transaction('income')
        
    def add_expense(self):
        self.add_transaction('expense')
        
    def add_transaction(self, transaction_type):
        """Add income/expense transaction"""
        dialog = ctk.CTkToplevel(self)
        dialog.title(f"Add {transaction_type.title()}")
        dialog.geometry("400x350")
        
        ctk.CTkLabel(dialog, text="Amount:").pack(pady=5)
        amount_entry = ctk.CTkEntry(dialog, width=300)
        amount_entry.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Description:").pack(pady=5)
        desc_entry = ctk.CTkEntry(dialog, width=300)
        desc_entry.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Category:").pack(pady=5)
        
        if transaction_type == 'income':
            categories = ["Sales", "Services", "Investments", "Other"]
        else:
            categories = ["Supplies", "Salaries", "Utilities", "Marketing", "Other"]
            
        category_combo = ctk.CTkComboBox(dialog, values=categories)
        category_combo.pack(pady=5)
        
        def save_transaction():
            try:
                amount = float(amount_entry.get())
                cursor = self.conn.cursor()
                cursor.execute('''
                    INSERT INTO transactions (type, amount, description, category)
                    VALUES (?, ?, ?, ?)
                ''', (transaction_type, amount, desc_entry.get(), category_combo.get()))
                self.conn.commit()
                
                dialog.destroy()
                self.load_transactions()
                self.setup_ui()  # Refresh stats
            except ValueError:
                pass
                
        ctk.CTkButton(dialog, text="Save", command=save_transaction).pack(pady=20)
        
    def show_reports(self):
        """Show financial reports"""
        # This would open a detailed reports window with charts
        pass