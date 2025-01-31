import sys
import os

# Get the absolute path of the project root (one level up from tests/)
'C:\Users\Peter\Dev\College\Veterinary-Vaxxination-System' = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# ✅ Add the project root directory (so Python recognizes models & utils)
sys.path.insert(0, 'C:\Users\Peter\Dev\College\Veterinary-Vaxxination-System')

# ✅ Add the models directory explicitly
sys.path.insert(0, os.path.join('C:\Users\Peter\Dev\College\Veterinary-Vaxxination-System\models', 'models'))

# ✅ Add the utils directory explicitly (if needed)
sys.path.insert(0, os.path.join('C:\Users\Peter\Dev\College\Veterinary-Vaxxination-System\utils', 'utils'))

# Debugging: Uncomment this line to print sys.path and check if paths are correct
#print(sys.path)