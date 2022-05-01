import advancements
import functions
import item_modifiers
import os
from shutil import rmtree

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
