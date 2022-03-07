import pandas as pd

df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')
enchantments = df['Enchantment'].tolist()

for enchant in enchantments:
    new_file = open(f'output/{enchant}.mcfunction', 'w')
    new_file.truncate()
    for slot in range(36):
        new_file.write(f'execute if entity @s[nbt={{Inventory:[{{Slot:{slot}b, id:"minecraft:enchanted_book", tag:{{StoredEnchantments: [{{id: "minecraft:{enchant}"}}]}}}}]}}] run item modify entity @s container.{slot} enchdetails:{enchant}\n')
    new_file.write(f'advancement revoke @s only enchdetails:{enchant}')
    new_file.close()
