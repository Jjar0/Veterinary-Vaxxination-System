import sys
import os

# ✅ Use a raw string to prevent escape sequence errors
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), r'C:\Users\Peter\Dev\College\Veterinary-Vaxxination-System'))

# ✅ Add the project root and models directory to sys.path
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "models"))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "utils"))

# Debugging: Uncomment this to check paths
# print(sys.path)