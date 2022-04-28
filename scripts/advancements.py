import pandas as pd
import os
from shutil import rmtree

df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')  # Creates a DataFrame from the spreadsheet
enchantments = df['Enchantment'].tolist()  # Converts the spreadsheet column "Enchantment" to a list so it can be indexed later

rmtree(os.path.dirname(__file__) + '/output')
os.mkdir('output')

for enchant in enchantments:  # Loop through each enchantment file
    new_file = open(f'output/{enchant}.json', 'w')
    new_file.truncate()  # Removes contents of the file
    new_file.write(f'{{"criteria": {{"requirement": {{"trigger": "minecraft:inventory_changed", "conditions": {{"items": [ {{"items": [ "minecraft:enchanted_book" ], "nbt": "{{StoredEnchantments:[{{id:\\"minecraft:{enchant}\\"}}]}}" }}]}}}}}}, "rewards": {{"function": "enchdetails:{enchant}" }}}}')
    new_file.close()
