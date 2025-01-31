import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'c:\Users\Peter\Dev\College\Veterinary-Vaxxination-System'))

sys.path.insert(0, PROJECT_ROOT)

sys.path.insert(0, os.path.join(PROJECT_ROOT, "models"))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "utils"))

# Debugging: Uncomment this line to print sys.path and check if paths are correct
# print(sys.path)
