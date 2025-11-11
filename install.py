import subprocess
import sys
import os

def install_requirements():
    """Install all required packages"""
    print("🚀 Installing Business Suite Dependencies...")
    
    requirements = [
        "customtkinter==5.2.0",
        "tkinterweb==3.1.0", 
        "matplotlib==3.7.0",
        "pandas==2.0.0",
        "numpy==1.24.0",
        "pillow==10.0.0",
        "requests==2.31.0",
        "faker==18.0.0"
    ]
    
    for package in requirements:
        try:
            print(f"📦 Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
    
    print("✅ All dependencies installed successfully!")
    print("\n🎉 Installation complete! Run 'python main.py' to start the Business Suite.")

if __name__ == "__main__":
    install_requirements()