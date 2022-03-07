import pandas as pd

df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')
enchantments = df['Enchantment'].tolist()

for enchant in enchantments:
    new_file = open(f'output/{enchant}.json', 'w')
    new_file.truncate()
    new_file.write(f'{{"criteria": {{"requirement": {{"trigger": "minecraft:inventory_changed", "conditions": {{"items": [ {{"items": [ "minecraft:enchanted_book" ], "nbt": "{{StoredEnchantments:[{{id:\\"minecraft:{enchant}\\"}}]}}" }}]}}}}}}, "rewards": {{"function": "enchdetails:{enchant}" }}}}')
    new_file.close()
