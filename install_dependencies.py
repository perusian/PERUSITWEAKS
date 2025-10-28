import subprocess, sys

print("📦 Installing dependencies...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
print("✅ All dependencies installed!")
