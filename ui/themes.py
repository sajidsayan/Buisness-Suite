import customtkinter as ctk
from typing import Dict, Any

class ThemeManager:
    _themes = {
        "dark": {
            "bg": "#1a1a1a",
            "fg": "#ffffff",
            "accent": "#2fa572",
            "secondary": "#3a3a3a",
            "text": "#ffffff",
            "success": "#28a745",
            "warning": "#ffc107",
            "danger": "#dc3545",
            "info": "#17a2b8"
        },
        "light": {
            "bg": "#ffffff",
            "fg": "#000000",
            "accent": "#2fa572",
            "secondary": "#f8f9fa",
            "text": "#000000",
            "success": "#28a745",
            "warning": "#ffc107",
            "danger": "#dc3545",
            "info": "#17a2b8"
        },
        "blue": {
            "bg": "#1e2a3a",
            "fg": "#ffffff",
            "accent": "#3b82f6",
            "secondary": "#2d3748",
            "text": "#ffffff",
            "success": "#10b981",
            "warning": "#f59e0b",
            "danger": "#ef4444",
            "info": "#06b6d4"
        },
        "purple": {
            "bg": "#2d1b69",
            "fg": "#ffffff",
            "accent": "#8b5cf6",
            "secondary": "#4c1d95",
            "text": "#ffffff",
            "success": "#10b981",
            "warning": "#f59e0b",
            "danger": "#ef4444",
            "info": "#06b6d4"
        }
    }
    
    @classmethod
    def get_theme(cls, theme_name: str) -> Dict[str, str]:
        return cls._themes.get(theme_name, cls._themes["dark"])
    
    @classmethod
    def apply_theme(cls, theme_name: str):
        """Apply theme to customtkinter"""
        theme = cls.get_theme(theme_name)
        
        # Set appearance mode
        ctk.set_appearance_mode("dark" if theme_name != "light" else "light")
        
        # Set default color theme
        ctk.set_default_color_theme("blue")  # This will use customtkinter's built-in themes
        
        return theme
    
    @classmethod
    def get_available_themes(cls):
        return list(cls._themes.keys())

class StyledFrame(ctk.CTkFrame):
    def __init__(self, master, style="default", **kwargs):
        self.style = style
        super().__init__(master, **kwargs)
        self.apply_style()
    
    def apply_style(self):
        if self.style == "card":
            self.configure(corner_radius=10, border_width=1, border_color="#444")
        elif self.style == "header":
            self.configure(corner_radius=0, fg_color="#2b2b2b")
        elif self.style == "sidebar":
            self.configure(corner_radius=0, fg_color="#1e1e1e")

class GradientFrame(ctk.CTkFrame):
    def __init__(self, master, color1, color2, **kwargs):
        super().__init__(master, **kwargs)
        self.color1 = color1
        self.color2 = color2
        
    def apply_gradient(self):
        # This would require custom canvas drawing for gradient effects
        # For now, we'll use solid colors
        self.configure(fg_color=self.color1)

class AnimatedWidget:
    def __init__(self, widget):
        self.widget = widget
    
    def fade_in(self, duration=300):
        # Simple animation - could be enhanced with more complex animations
        self.widget.configure(state="normal")
    
    def fade_out(self, duration=300):
        self.widget.configure(state="disabled")

# Custom widgets with enhanced styling
class PrimaryButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color="#3b82f6",
            hover_color="#2563eb",
            text_color="white",
            font=ctk.CTkFont(weight="bold")
        )

class SuccessButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color="#10b981",
            hover_color="#059669",
            text_color="white"
        )

class DangerButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color="#ef4444",
            hover_color="#dc2626",
            text_color="white"
        )

class OutlineButton(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "gray90")
        )