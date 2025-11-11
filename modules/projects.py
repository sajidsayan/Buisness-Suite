import customtkinter as ctk
import sqlite3
from datetime import datetime

class ProjectModule(ctk.CTkFrame):
    def __init__(self, parent, connection):
        super().__init__(parent)
        self.conn = connection
        
        # Create projects table
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                status TEXT,
                priority TEXT,
                start_date TEXT,
                end_date TEXT,
                budget REAL
            )
        ''')
        self.conn.commit()
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup Projects UI"""
        header = ctk.CTkFrame(self)
        header.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(header, text="📋 Project Management", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=10)
        
        # Project overview with Kanban-style columns
        self.create_kanban_board()
        
    def create_kanban_board(self):
        """Create Kanban board for project management"""
        kanban_frame = ctk.CTkFrame(self)
        kanban_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        columns = [
            ("📋 Backlog", "backlog"),
            ("🔄 In Progress", "in_progress"), 
            ("✅ Completed", "completed")
        ]
        
        for i, (title, status) in enumerate(columns):
            col_frame = ctk.CTkFrame(kanban_frame)
            col_frame.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
            kanban_frame.grid_columnconfigure(i, weight=1)
            kanban_frame.grid_rowconfigure(0, weight=1)
            
            # Column header
            ctk.CTkLabel(col_frame, text=title, font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
            
            # Add project button
            ctk.CTkButton(col_frame, text="+ Add Project", 
                         command=lambda s=status: self.add_project(s)).pack(pady=5)
            
            # Projects list (would be populated from database)
            projects_frame = ctk.CTkScrollableFrame(col_frame)
            projects_frame.pack(fill="both", expand=True, padx=5, pady=5)
            
    def add_project(self, status):
        """Add new project dialog"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add New Project")
        dialog.geometry("500x400")
        
        ctk.CTkLabel(dialog, text="Project Name:").pack(pady=5)
        name_entry = ctk.CTkEntry(dialog, width=400)
        name_entry.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Description:").pack(pady=5)
        desc_entry = ctk.CTkTextbox(dialog, width=400, height=100)
        desc_entry.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Priority:").pack(pady=5)
        priority_combo = ctk.CTkComboBox(dialog, values=["Low", "Medium", "High", "Critical"])
        priority_combo.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Budget:").pack(pady=5)
        budget_entry = ctk.CTkEntry(dialog, width=400)
        budget_entry.pack(pady=5)
        
        def save_project():
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO projects (name, description, status, priority, start_date, budget)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                name_entry.get(),
                desc_entry.get("1.0", "end-1c"),
                status,
                priority_combo.get(),
                datetime.now().strftime("%Y-%m-%d"),
                float(budget_entry.get() or 0)
            ))
            self.conn.commit()
            
            dialog.destroy()
            # Refresh the Kanban board
            
        ctk.CTkButton(dialog, text="Save Project", command=save_project).pack(pady=20)