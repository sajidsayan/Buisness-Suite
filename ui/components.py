import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import os

class ModernButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
class StatsCard(ctk.CTkFrame):
    def __init__(self, master, title, value, trend=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.title_label = ctk.CTkLabel(self, text=title, font=ctk.CTkFont(size=12))
        self.title_label.pack(pady=(10, 5))
        
        self.value_label = ctk.CTkLabel(self, text=value, font=ctk.CTkFont(size=24, weight="bold"))
        self.value_label.pack(pady=5)
        
        if trend:
            trend_color = "green" if trend.startswith("↑") else "red" if trend.startswith("↓") else "gray"
            self.trend_label = ctk.CTkLabel(self, text=trend, text_color=trend_color)
            self.trend_label.pack(pady=(5, 10))
    
    def update_value(self, new_value, new_trend=None):
        self.value_label.configure(text=new_value)
        if new_trend:
            trend_color = "green" if new_trend.startswith("↑") else "red" if new_trend.startswith("↓") else "gray"
            self.trend_label.configure(text=new_trend, text_color=trend_color)

class DataTable(ctk.CTkFrame):
    def __init__(self, master, columns, **kwargs):
        super().__init__(master, **kwargs)
        
        self.columns = columns
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=10)
        
        # Configure columns
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        
        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        # Pack
        self.tree.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
    
    def load_data(self, data):
        """Load data into table"""
        self.clear()
        for row in data:
            self.tree.insert("", "end", values=row)
    
    def clear(self):
        """Clear table data"""
        for item in self.tree.get_children():
            self.tree.delete(item)
    
    def get_selected(self):
        """Get selected row"""
        selection = self.tree.selection()
        if selection:
            return self.tree.item(selection[0])['values']
        return None

class SearchBar(ctk.CTkFrame):
    def __init__(self, master, placeholder="Search...", on_search=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.on_search = on_search
        
        self.search_var = ctk.StringVar()
        self.search_entry = ctk.CTkEntry(
            self, 
            placeholder_text=placeholder,
            textvariable=self.search_var,
            width=300
        )
        self.search_entry.pack(side="left", padx=5)
        
        self.search_btn = ctk.CTkButton(
            self, 
            text="🔍", 
            width=40,
            command=self.perform_search
        )
        self.search_btn.pack(side="left", padx=5)
        
        # Bind Enter key
        self.search_entry.bind("<Return>", lambda e: self.perform_search())
    
    def perform_search(self):
        if self.on_search:
            self.on_search(self.search_var.get())

class Pagination(ctk.CTkFrame):
    def __init__(self, master, on_page_change=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.current_page = 1
        self.total_pages = 1
        self.on_page_change = on_page_change
        
        self.prev_btn = ctk.CTkButton(self, text="◀", width=40, command=self.prev_page)
        self.prev_btn.pack(side="left", padx=5)
        
        self.page_label = ctk.CTkLabel(self, text="Page 1 of 1")
        self.page_label.pack(side="left", padx=10)
        
        self.next_btn = ctk.CTkButton(self, text="▶", width=40, command=self.next_page)
        self.next_btn.pack(side="left", padx=5)
    
    def set_total_pages(self, total_pages):
        self.total_pages = total_pages
        self.update_display()
    
    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_display()
            if self.on_page_change:
                self.on_page_change(self.current_page)
    
    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_display()
            if self.on_page_change:
                self.on_page_change(self.current_page)
    
    def update_display(self):
        self.page_label.configure(text=f"Page {self.current_page} of {self.total_pages}")
        self.prev_btn.configure(state="normal" if self.current_page > 1 else "disabled")
        self.next_btn.configure(state="normal" if self.current_page < self.total_pages else "disabled")

class NotificationBadge(ctk.CTkLabel):
    def __init__(self, master, count=0, **kwargs):
        super().__init__(master, text=str(count), **kwargs)
        self.count = count
        self.update_display()
    
    def set_count(self, count):
        self.count = count
        self.update_display()
    
    def update_display(self):
        self.configure(text=str(self.count))
        if self.count > 0:
            self.configure(fg_color="red", text_color="white")
        else:
            self.configure(fg_color="transparent", text_color="transparent")

class LoadingSpinner(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label = ctk.CTkLabel(self, text="Loading...")
        self.label.pack(pady=20)
        
        self.progress = ctk.CTkProgressBar(self, mode='indeterminate')
        self.progress.pack(pady=10, padx=20, fill="x")
    
    def start(self):
        self.progress.start()
        self.lift()
    
    def stop(self):
        self.progress.stop()
        self.lower()