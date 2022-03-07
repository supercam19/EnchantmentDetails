import pandas as pd

df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')  # Creates a DataFrame from the spreadsheet
enchantments = df['Enchantment'].tolist()  # Converts the spreadsheet column "Enchantment" to a list so it can be indexed later

for enchant in enchantments:  # Loop through each enchantment file
    new_file = open(f'output/{enchant}.json', 'w')  # Opens the file or creates one if it doesn't exist
    new_file.truncate()  # Removes contents of the file
    new_file.write(f'{{"criteria": {{"requirement": {{"trigger": "minecraft:inventory_changed", "conditions": {{"items": [ {{"items": [ "minecraft:enchanted_book" ], "nbt": "{{StoredEnchantments:[{{id:\\"minecraft:{enchant}\\"}}]}}" }}]}}}}}}, "rewards": {{"function": "enchdetails:{enchant}" }}}}')
    new_file.close()
