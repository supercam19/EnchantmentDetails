from time import time
import os

start_time = time()

try: os.mkdir('output')
except FileExistsError: pass

try:
    import advancements
except ImportError:
    print("[Error] The file 'advancements.py' is missing! Make sure it is placed in the same folder as this script.")
    exit()
finally: import advancements
try:
    import functions
except ImportError:
    print("[Error] The file 'functions.py' is missing! Make sure it is placed in the same folder as this script.")
    exit()
finally: import functions
try:
    import item_modifiers
except ImportError:
    print("[Error] The file 'item_modifiers.py' is missing! Make sure it is placed in the same folder as this script.")
    exit()
finally: import item_modifiers
from shutil import rmtree
print("[Info] All necessary files found!")

# Empty the directory 'output'
rmtree(os.path.dirname(__file__) + '/output')
os.mkdir('output')

# Create the directories that hold the other directories
os.mkdir('output/data')
os.mkdir('output/data/enchdetails')

# Create the directories that hold the files
os.mkdir('output/data/enchdetails/functions')
os.mkdir('output/data/enchdetails/advancements')
os.mkdir('output/data/enchdetails/item_modifiers')

# Run the 'functions.py', 'advancements.py' and 'item_modifiers.py' scripts with a custom output directory
functions.main('/output/data/enchdetails/functions')
advancements.main('/output/data/enchdetails/advancements')
item_modifiers.main('/output/data/enchdetails/item_modifiers')

print(f"[Info] Generated the datapack (117 files) in {round(time() - start_time, 3)} seconds")
