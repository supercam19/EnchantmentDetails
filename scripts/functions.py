import pandas as pd

df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')  # Creates a DataFrame from the spreadsheet
enchantments = df['Enchantment'].tolist()  # Converts the spreadsheet column "Enchantment" to a list so it can be indexed later

for enchant in enchantments:  # Loop through each enchantment file
    new_file = open(f'output/{enchant}.mcfunction', 'w')  # Opens the file or creates one if it doesn't
    new_file.truncate()  # Removes contents of the file
    for slot in range(36):  # Writes the following string 36 times (for each inventory slot)
        new_file.write(f'execute if entity @s[nbt={{Inventory:[{{Slot:{slot}b, id:"minecraft:enchanted_book", tag:{{StoredEnchantments: [{{id: "minecraft:{enchant}"}}]}}}}]}}] run item modify entity @s container.{slot} enchdetails:{enchant}\n')
    new_file.write(f'advancement revoke @s only enchdetails:{enchant}')
    new_file.close()
