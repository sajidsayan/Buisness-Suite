import customtkinter as ctk
import sqlite3
try:
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

class AnalyticsModule(ctk.CTkFrame):
    def __init__(self, parent, connection):
        super().__init__(parent)
        self.conn = connection
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup Analytics Dashboard UI"""
        header = ctk.CTkFrame(self)
        header.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(header, text="📈 Business Analytics", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", padx=10)
        
        # Analytics controls
        controls_frame = ctk.CTkFrame(header)
        controls_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkButton(controls_frame, text="Sales Report", command=self.show_sales_report).pack(side="left", padx=5)
        ctk.CTkButton(controls_frame, text="Customer Analytics", command=self.show_customer_analytics).pack(side="left", padx=5)
        ctk.CTkButton(controls_frame, text="Financial Overview", command=self.show_financial_overview).pack(side="left", padx=5)
        
        # Charts area
        self.charts_frame = ctk.CTkFrame(self)
        self.charts_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Show default dashboard
        self.show_default_dashboard()
        
    def show_default_dashboard(self):
        """Show default analytics dashboard"""
        self.clear_charts()
        
        if not MATPLOTLIB_AVAILABLE:
            ctk.CTkLabel(self.charts_frame, text="Matplotlib not available for charts").pack(pady=50)
            return
            
        # Create sample charts
        self.create_sample_chart("Monthly Revenue", [10000, 12000, 8000, 15000, 20000, 18000])
        self.create_sample_chart("Customer Growth", [100, 120, 150, 180, 220, 250])
        
    def clear_charts(self):
        """Clear charts area"""
        for widget in self.charts_frame.winfo_children():
            widget.destroy()
            
    def create_sample_chart(self, title, data):
        """Create a sample chart"""
        if not MATPLOTLIB_AVAILABLE:
            return
            
        chart_frame = ctk.CTkFrame(self.charts_frame)
        chart_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(data, marker='o')
        ax.set_title(title)
        ax.grid(True)
        
        canvas = FigureCanvasTkAgg(fig, chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        
    def show_sales_report(self):
        """Generate sales report"""
        self.clear_charts()
        # Implementation would fetch real data and create charts
        
    def show_customer_analytics(self):
        """Show customer analytics"""
        self.clear_charts()
        # Implementation would analyze customer data
        
    def show_financial_overview(self):
        """Show financial overview"""
        self.clear_charts()
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT type, SUM(amount) FROM transactions GROUP BY type")
        results = cursor.fetchall()
        
        if results and MATPLOTLIB_AVAILABLE:
            chart_frame = ctk.CTkFrame(self.charts_frame)
            chart_frame.pack(fill="both", expand=True, padx=5, pady=5)
            
            fig, ax = plt.subplots(figsize=(6, 4))
            
            types = [row[0] for row in results]
            amounts = [row[1] for row in results]
            
            ax.pie(amounts, labels=types, autopct='%1.1f%%')
            ax.set_title("Income vs Expenses")
            
            canvas = FigureCanvasTkAgg(fig, chart_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)