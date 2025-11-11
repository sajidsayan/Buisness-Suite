import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import sqlite3
from faker import Faker

class CRMModule(ctk.CTkFrame):
    def __init__(self, parent, connection):
        super().__init__(parent)
        self.conn = connection
        self.fake = Faker()
        
        self.setup_ui()
        self.load_customers()
        
    def setup_ui(self):
        """Setup CRM UI"""
        # Header
        header = ctk.CTkFrame(self)
        header.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(header, text="👥 Customer Relationship Management", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(side="left", padx=10)
        
        # Action buttons
        btn_frame = ctk.CTkFrame(header)
        btn_frame.pack(side="right", padx=10)
        
        ctk.CTkButton(btn_frame, text="+ Add Customer", command=self.add_customer_dialog).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="🎲 Generate Sample", command=self.generate_sample_data).pack(side="left", padx=5)
        
        # Main content
        content = ctk.CTkFrame(self)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Customer list
        self.create_customer_table(content)
        
    def create_customer_table(self, parent):
        """Create customer table with scrollable frame"""
        # Table frame
        table_frame = ctk.CTkFrame(parent)
        table_frame.pack(fill="both", expand=True)
        
        # Create treeview
        columns = ("ID", "Name", "Email", "Phone", "Company", "Status", "Created")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        
        # Configure columns
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack tree and scrollbar
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind double-click event
        self.tree.bind("<Double-1>", self.edit_customer)
        
    def load_customers(self):
        """Load customers from database"""
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Fetch from database
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customers ORDER BY created_date DESC")
        
        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)
            
    def add_customer_dialog(self):
        """Dialog for adding new customer"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add New Customer")
        dialog.geometry("400x300")
        dialog.transient(self)
        dialog.grab_set()
        
        # Form fields
        ctk.CTkLabel(dialog, text="Name:").pack(pady=5)
        name_entry = ctk.CTkEntry(dialog, width=300)
        name_entry.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Email:").pack(pady=5)
        email_entry = ctk.CTkEntry(dialog, width=300)
        email_entry.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Phone:").pack(pady=5)
        phone_entry = ctk.CTkEntry(dialog, width=300)
        phone_entry.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Company:").pack(pady=5)
        company_entry = ctk.CTkEntry(dialog, width=300)
        company_entry.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Status:").pack(pady=5)
        status_combo = ctk.CTkComboBox(dialog, values=["Active", "Inactive", "Prospect"])
        status_combo.pack(pady=5)
        
        def save_customer():
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO customers (name, email, phone, company, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (name_entry.get(), email_entry.get(), phone_entry.get(), 
                  company_entry.get(), status_combo.get()))
            self.conn.commit()
            
            dialog.destroy()
            self.load_customers()
            
        ctk.CTkButton(dialog, text="Save Customer", command=save_customer).pack(pady=20)
        
    def edit_customer(self, event):
        """Edit selected customer"""
        selection = self.tree.selection()
        if not selection:
            return
            
        item = self.tree.item(selection[0])
        customer_id = item['values'][0]
        
        # Similar to add_customer_dialog but with pre-filled data
        # Implementation would be similar to add_customer_dialog
        
    def generate_sample_data(self):
        """Generate sample customer data"""
        cursor = self.conn.cursor()
        
        for _ in range(10):
            cursor.execute('''
                INSERT INTO customers (name, email, phone, company, status)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                self.fake.name(),
                self.fake.email(),
                self.fake.phone_number(),
                self.fake.company(),
                self.fake.random_element(elements=("Active", "Inactive", "Prospect"))
            ))
            
        self.conn.commit()
        self.load_customers()