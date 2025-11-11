import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os
from PIL import Image, ImageTk
import sys

# Import modules
from modules.crm import CRMModule
from modules.accounting import AccountingModule
from modules.inventory import InventoryModule
from modules.hr import HRModule
from modules.projects import ProjectModule
from modules.analytics import AnalyticsModule

class BusinessSuite(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Mega Business Suite Pro")
        self.geometry("1400x900")
        self.minsize(1200, 800)
        
        # Configure theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Initialize database
        self.init_database()
        
        # Setup UI
        self.setup_ui()
        
    def init_database(self):
        """Initialize SQLite database"""
        os.makedirs("data", exist_ok=True)
        self.conn = sqlite3.connect("data/business_suite.db", check_same_thread=False)
        
        # Create tables for different modules
        cursor = self.conn.cursor()
        
        # CRM table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                company TEXT,
                status TEXT,
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Accounting table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT,
                category TEXT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Inventory table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sku TEXT UNIQUE,
                price REAL,
                quantity INTEGER,
                category TEXT
            )
        ''')
        
        self.conn.commit()
        
    def setup_ui(self):
        """Setup the main user interface"""
        # Create main container
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create sidebar
        self.create_sidebar()
        
        # Create main content area
        self.create_main_content()
        
    def create_sidebar(self):
        """Create the sidebar navigation"""
        sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_rowconfigure(8, weight=1)
        
        # Logo and title
        logo_label = ctk.CTkLabel(
            sidebar, 
            text="🏢 Business Suite", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        logo_label.grid(row=0, column=0, padx=20, pady=20)
        
        # Navigation buttons
        nav_buttons = [
            ("📊 Dashboard", self.show_dashboard),
            ("👥 CRM", self.show_crm),
            ("💰 Accounting", self.show_accounting),
            ("📦 Inventory", self.show_inventory),
            ("👨‍💼 HR Management", self.show_hr),
            ("📋 Projects", self.show_projects),
            ("📈 Analytics", self.show_analytics),
            ("⚙️ Settings", self.show_settings)
        ]
        
        for i, (text, command) in enumerate(nav_buttons, 1):
            btn = ctk.CTkButton(
                sidebar,
                text=text,
                command=command,
                height=40,
                anchor="w",
                font=ctk.CTkFont(size=14)
            )
            btn.grid(row=i, column=0, padx=10, pady=5, sticky="ew")
        
        # User section at bottom
        user_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        user_frame.grid(row=9, column=0, padx=10, pady=20, sticky="ew")
        
        user_label = ctk.CTkLabel(user_frame, text="👤 Admin User")
        user_label.pack()
        
    def create_main_content(self):
        """Create the main content area"""
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        # Show dashboard by default
        self.show_dashboard()
        
    def clear_main_frame(self):
        """Clear the main content area"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
    def show_dashboard(self):
        """Show dashboard view"""
        self.clear_main_frame()
        
        # Dashboard header
        header = ctk.CTkFrame(self.main_frame, height=80)
        header.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        header.grid_columnconfigure(0, weight=1)
        
        title = ctk.CTkLabel(header, text="📊 Business Dashboard", 
                           font=ctk.CTkFont(size=24, weight="bold"))
        title.grid(row=0, column=0, sticky="w", padx=20, pady=20)
        
        # Stats cards
        stats_frame = ctk.CTkFrame(self.main_frame)
        stats_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        
        stats = [
            ("Total Revenue", "$125,430", "↑ 12%"),
            ("Active Customers", "1,243", "↑ 8%"),
            ("Pending Orders", "47", "↓ 3%"),
            ("Inventory Items", "856", "→ Stable")
        ]
        
        for i, (title, value, trend) in enumerate(stats):
            card = ctk.CTkFrame(stats_frame, height=100)
            card.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
            stats_frame.grid_columnconfigure(i, weight=1)
            
            ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=12)).pack(pady=(10,5))
            ctk.CTkLabel(card, text=value, font=ctk.CTkFont(size=24, weight="bold")).pack()
            ctk.CTkLabel(card, text=trend, text_color="green").pack(pady=(5,10))
        
        # Recent activity
        activity_frame = ctk.CTkFrame(self.main_frame)
        activity_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.main_frame.grid_rowconfigure(2, weight=1)
        
        ctk.CTkLabel(activity_frame, text="Recent Activity", 
                    font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w", padx=20, pady=10)
        
        # Activity list
        activities = [
            "New customer 'TechCorp' registered",
            "Invoice #INV-0012 paid",
            "Low stock alert for Product XYZ",
            "New employee onboarding completed",
            "Monthly report generated"
        ]
        
        for activity in activities:
            ctk.CTkLabel(activity_frame, text=f"• {activity}").pack(anchor="w", padx=30, pady=2)
    
    def show_crm(self):
        """Show CRM module"""
        self.clear_main_frame()
        crm_module = CRMModule(self.main_frame, self.conn)
        crm_module.pack(fill="both", expand=True)
        
    def show_accounting(self):
        """Show Accounting module"""
        self.clear_main_frame()
        accounting_module = AccountingModule(self.main_frame, self.conn)
        accounting_module.pack(fill="both", expand=True)
        
    def show_inventory(self):
        """Show Inventory module"""
        self.clear_main_frame()
        inventory_module = InventoryModule(self.main_frame, self.conn)
        inventory_module.pack(fill="both", expand=True)
        
    def show_hr(self):
        """Show HR module"""
        self.clear_main_frame()
        hr_module = HRModule(self.main_frame, self.conn)
        hr_module.pack(fill="both", expand=True)
        
    def show_projects(self):
        """Show Projects module"""
        self.clear_main_frame()
        project_module = ProjectModule(self.main_frame, self.conn)
        project_module.pack(fill="both", expand=True)
        
    def show_analytics(self):
        """Show Analytics module"""
        self.clear_main_frame()
        analytics_module = AnalyticsModule(self.main_frame, self.conn)
        analytics_module.pack(fill="both", expand=True)
        
    def show_settings(self):
        """Show Settings"""
        self.clear_main_frame()
        
        ctk.CTkLabel(self.main_frame, text="Settings", 
                    font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)
        
        # Theme settings
        theme_frame = ctk.CTkFrame(self.main_frame)
        theme_frame.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(theme_frame, text="Appearance", 
                    font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", padx=10, pady=10)
        
        theme_var = ctk.StringVar(value="dark")
        
        def change_theme():
            ctk.set_appearance_mode(theme_var.get())
            
        ctk.CTkRadioButton(theme_frame, text="Dark", variable=theme_var, 
                          value="dark", command=change_theme).pack(anchor="w", padx=20, pady=5)
        ctk.CTkRadioButton(theme_frame, text="Light", variable=theme_var, 
                          value="light", command=change_theme).pack(anchor="w", padx=20, pady=5)

if __name__ == "__main__":
    # Check if dependencies are installed
    try:
        import customtkinter
        import pandas
        print("✅ All dependencies are installed!")
    except ImportError as e:
        print("❌ Missing dependencies. Please run: python install.py")
        sys.exit(1)
    
    app = BusinessSuite()
    app.mainloop()