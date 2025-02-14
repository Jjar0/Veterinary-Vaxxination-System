import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), r'C:\Users\Peter\Dev\College\Veterinary-Vaxxination-System'))

sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "models"))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "utils"))

# Debugging: Uncomment this to check paths
# print(sys.path)
