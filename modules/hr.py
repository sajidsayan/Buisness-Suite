import customtkinter as ctk
import sqlite3
from faker import Faker

class HRModule(ctk.CTkFrame):
    def __init__(self, parent, connection):
        super().__init__(parent)
        self.conn = connection
        self.fake = Faker()
        
        # Create employees table if not exists
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                position TEXT,
                department TEXT,
                salary REAL,
                hire_date TEXT,
                status TEXT
            )
        ''')
        self.conn.commit()
        
        self.setup_ui()
        self.load_employees()
        
    def setup_ui(self):
        """Setup HR Management UI"""
        header = ctk.CTkFrame(self)
        header.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(header, text="👨‍💼 Human Resources", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=10)
        
        # Quick actions
        btn_frame = ctk.CTkFrame(header)
        btn_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkButton(btn_frame, text="+ Add Employee", command=self.add_employee).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="🎲 Generate Sample", command=self.generate_sample_data).pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="📊 Department Stats", command=self.show_department_stats).pack(side="left", padx=5)
        
        # Employee list would be implemented similarly to other modules
        # Using treeview to display employees
        
    def load_employees(self):
        """Load employees from database"""
        # Implementation similar to CRM module
        pass
        
    def add_employee(self):
        """Add new employee dialog"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add New Employee")
        dialog.geometry("400x450")
        
        fields = [
            ("Full Name", "text"),
            ("Email", "text"),
            ("Position", "combo"),
            ("Department", "combo"),
            ("Salary", "number"),
            ("Hire Date", "text"),
            ("Status", "combo")
        ]
        
        entries = {}
        positions = ["Manager", "Developer", "Analyst", "Designer", "Sales", "Support"]
        departments = ["IT", "HR", "Finance", "Marketing", "Operations", "Sales"]
        statuses = ["Active", "On Leave", "Terminated"]
        
        for label, field_type in fields:
            ctk.CTkLabel(dialog, text=label).pack(pady=5)
            
            if field_type == "text" or field_type == "number":
                entry = ctk.CTkEntry(dialog, width=300)
                entry.pack(pady=5)
                entries[label] = entry
            elif field_type == "combo":
                if label == "Position":
                    combo = ctk.CTkComboBox(dialog, values=positions)
                elif label == "Department":
                    combo = ctk.CTkComboBox(dialog, values=departments)
                elif label == "Status":
                    combo = ctk.CTkComboBox(dialog, values=statuses)
                combo.pack(pady=5)
                entries[label] = combo
                
        def save_employee():
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO employees (name, email, position, department, salary, hire_date, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                entries["Full Name"].get(),
                entries["Email"].get(),
                entries["Position"].get(),
                entries["Department"].get(),
                float(entries["Salary"].get()),
                entries["Hire Date"].get(),
                entries["Status"].get()
            ))
            self.conn.commit()
            
            dialog.destroy()
            self.load_employees()
            
        ctk.CTkButton(dialog, text="Save Employee", command=save_employee).pack(pady=20)
        
    def generate_sample_data(self):
        """Generate sample employee data"""
        cursor = self.conn.cursor()
        
        positions = ["Manager", "Developer", "Analyst", "Designer", "Sales"]
        departments = ["IT", "HR", "Finance", "Marketing", "Operations"]
        
        for _ in range(5):
            cursor.execute('''
                INSERT INTO employees (name, email, position, department, salary, hire_date, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                self.fake.name(),
                self.fake.email(),
                self.fake.random_element(positions),
                self.fake.random_element(departments),
                self.fake.random_number(digits=5),
                self.fake.date(),
                "Active"
            ))
            
        self.conn.commit()
        self.load_employees()
        
    def show_department_stats(self):
        """Show department statistics"""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT department, COUNT(*), AVG(salary) 
            FROM employees 
            GROUP BY department
        ''')
        
        stats = cursor.fetchall()
        stats_text = "Department Statistics:\n\n"
        
        for dept, count, avg_salary in stats:
            stats_text += f"{dept}: {count} employees, Avg Salary: ${avg_salary:,.2f}\n"
            
        ctk.CTkMessageBox.showinfo("Department Stats", stats_text)