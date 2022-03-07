<<<<<<< HEAD
<<<<<<< Updated upstream
enchantments = ("sharpness", "smite", "bane_of_arthropods", "knockback", "fire_aspect",
                "sweeping_edge", "protection", "fire_protection", "feather_falling", "blast_protection",
                "projectile_protection", "respiration", "aqua_affinity", "depth_strider",
                "frost_walker", "soul_speed", "efficiency", "silk_touch", "unbreaking",
                "looting", "fortune", "luck_of_the_sea", "lure", "power", "flame", "punch",
                "infinity", "thorns", "mending", "binding_curse", "vanishing_curse", "loyalty",
                "impaling", "riptide", "channeling", "multishot", "quick_charge", "piercing")
=======
import pandas as pd
=======
import pandas as pd

df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')
enchantments = df['Enchantment'].tolist()
>>>>>>> 0fe34e1b33316b2e9d345f43865cf02c12ea2fff

df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')  # Creates a DataFrame from the spreadsheet
enchantments = df['Enchantment'].tolist()  # Converts the spreadsheet column "Enchantment" to a list so it can be indexed later
>>>>>>> Stashed changes

for enchant in enchantments:  # Loop through each enchantment file
    new_file = open(f'output/{enchant}.json', 'w')  # Opens the file or creates one if it doesn't exist
    new_file.truncate()  # Removes contents of the file
    new_file.write(f'{{"criteria": {{"requirement": {{"trigger": "minecraft:inventory_changed", "conditions": {{"items": [ {{"items": [ "minecraft:enchanted_book" ], "nbt": "{{StoredEnchantments:[{{id:\\"minecraft:{enchant}\\"}}]}}" }}]}}}}}}, "rewards": {{"function": "enchdetails:{enchant}" }}}}')
    new_file.close()
