import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import sqlite3

class InventoryModule(ctk.CTkFrame):
    def __init__(self, parent, connection):
        super().__init__(parent)
        self.conn = connection
        
        self.setup_ui()
        self.load_products()
        
    def setup_ui(self):
        """Setup Inventory UI"""
        header = ctk.CTkFrame(self)
        header.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(header, text="📦 Inventory Management", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=10)
        
        # Stats
        stats_frame = ctk.CTkFrame(header)
        stats_frame.pack(fill="x", padx=10, pady=10)
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*), SUM(quantity), SUM(price * quantity) FROM products")
        total_products, total_items, total_value = cursor.fetchone()
        
        stats = [
            ("Total Products", str(total_products or 0)),
            ("Total Items", str(total_items or 0)),
            ("Total Value", f"${total_value or 0:,.2f}")
        ]
        
        for i, (title, value) in enumerate(stats):
            stat_card = ctk.CTkFrame(stats_frame)
            stat_card.grid(row=0, column=i, padx=10, pady=5, sticky="nsew")
            stats_frame.grid_columnconfigure(i, weight=1)
            
            ctk.CTkLabel(stat_card, text=title, font=ctk.CTkFont(size=12)).pack(pady=(10,5))
            ctk.CTkLabel(stat_card, text=value, font=ctk.CTkFont(size=16, weight="bold")).pack(pady=(5,10))
        
        # Action buttons
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkButton(btn_frame, text="+ Add Product", command=self.add_product).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="📋 Low Stock", command=self.show_low_stock).pack(side="left", padx=5)
        
        # Products table
        self.create_products_table()
        
    def create_products_table(self):
        """Create products inventory table"""
        table_frame = ctk.CTkFrame(self)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        columns = ("ID", "Name", "SKU", "Price", "Quantity", "Category")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
            
        # Low stock highlighting
        self.tree.tag_configure('low_stock', background='#fff3cd')
        
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def load_products(self):
        """Load products from database"""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products ORDER BY name")
        
        for row in cursor.fetchall():
            tags = ('low_stock',) if row[4] < 10 else ()
            self.tree.insert("", "end", values=row, tags=tags)
            
    def add_product(self):
        """Add new product dialog"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add New Product")
        dialog.geometry("400x400")
        
        fields = [
            ("Product Name", "text"),
            ("SKU", "text"),
            ("Price", "number"),
            ("Quantity", "number"),
            ("Category", "combo")
        ]
        
        entries = {}
        
        for i, (label, field_type) in enumerate(fields):
            ctk.CTkLabel(dialog, text=label).pack(pady=5)
            
            if field_type == "text" or field_type == "number":
                entry = ctk.CTkEntry(dialog, width=300)
                entry.pack(pady=5)
                entries[label] = entry
            elif field_type == "combo":
                combo = ctk.CTkComboBox(dialog, values=["Electronics", "Clothing", "Food", "Office", "Other"])
                combo.pack(pady=5)
                entries[label] = combo
                
        def save_product():
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO products (name, sku, price, quantity, category)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                entries["Product Name"].get(),
                entries["SKU"].get(),
                float(entries["Price"].get()),
                int(entries["Quantity"].get()),
                entries["Category"].get()
            ))
            self.conn.commit()
            
            dialog.destroy()
            self.load_products()
            self.setup_ui()  # Refresh stats
            
        ctk.CTkButton(dialog, text="Save Product", command=save_product).pack(pady=20)
        
    def show_low_stock(self):
        """Show low stock alert"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT name, quantity FROM products WHERE quantity < 10")
        low_stock = cursor.fetchall()
        
        if low_stock:
            alert_text = "Low Stock Items:\n" + "\n".join([f"{name}: {qty} left" for name, qty in low_stock])
            ctk.CTkMessageBox.showwarning("Low Stock Alert", alert_text)