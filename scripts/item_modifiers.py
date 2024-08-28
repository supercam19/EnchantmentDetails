import os
from shutil import rmtree
from time import time
import json

try:
    import pandas as pd
except ImportError:
    print("[Error] The 'pandas' library is not installed! Try 'pip install pandas'")
    exit()


def item_modifier(name, max_level, applications, description):
    return '[{"function": "minecraft:set_lore", "entity": "this", "lore": [[{"text": "' + name + ' ", "color": "gray"}, {"nbt":"details.level","storage":"minecraft:ench", "color":"gray"}, {"text":"/' + max_level + '", "color": "gray"}, {"text": "[' + applications + ']", "color": "dark_gray"}], {"text": "' + description + '", "color": "light_purple"}], "mode": "insert"}]'

def main(output_directory='/output'):
    """
        :param output_directory: either '/output' or '/output/data/enchdetails/item_modifiers'
    """

    start_time = time()

    try:
        df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')  # Creates a DataFrame from the spreadsheet
    except FileNotFoundError:
        print(
            "[Error] Could not find the spreadsheet 'EnchantmentDetails.xlsx', please make sure it is downloaded and in the same folder as the scripts!")
        exit()
    # Creates a list out of the three columns so they can be indexed later
    enchantments = df['Enchantment'].tolist()
    descriptions = df['Description'].tolist()
    applications = df['Applications'].tolist()
    maxLVL = df['MaxLVL'].tolist()

    if output_directory == '/output':
        if os.path.exists(os.path.dirname(__file__) + output_directory):
            rmtree(os.path.dirname(__file__) + output_directory)
        os.mkdir('output')

    for enchant in range(len(enchantments)):  # Loop through each enchantment file
        new_file = open(f'{output_directory.strip("/")}/{enchantments[enchant]}.json', 'w')
        new_file.truncate()  # Removes the contents of the file
        json.dump(json.loads(item_modifier(enchantments[enchant], maxLVL[enchant], applications[enchant], descriptions[enchant])), new_file, indent=4)
        new_file.close()

    if __name__ == '__main__':
        print(f'[Info] Generated {len(enchantments)} files in {round(time() - start_time, 3)} seconds')

if __name__ == '__main__':
    main()

