# Example: app_prep.py (optional, for automation)
import os
import shutil
import subprocess

# Clean previous build artifacts
if os.path.exists("dist"):
    shutil.rmtree("dist")
if os.path.exists("build"):
    shutil.rmtree("build")
if os.path.exists("H20.spec"):
    os.remove("H20.spec")

# Run PyInstaller
# Using --onedir for easier packaging with mpdev
subprocess.run([
    "pyinstaller",
    "--name", "H20",
    "--onedir",
    # "--windowed", # or --noconsole for GUI apps
    # "--add-data", "assets;assets", # Example: include assets folder
    "src/main.py"
], check=True)

# Clean up and prepare 'app' folder for mpdev
if os.path.exists("app"):
    shutil.rmtree("app")
shutil.copytree("dist/H20", "app") # Copy PyInstaller's output folder to 'app'
shutil.copyfile("waveIcon.ico", "app/waveIcon.ico")

print("Python app packaged and ready in 'app' folder.")