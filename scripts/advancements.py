import os
from shutil import rmtree
from time import time

try:
    import pandas as pd
except ImportError:
    print("[Error] The 'pandas' library is not installed! Try 'pip install pandas'")
    exit()


def main(output_directory='/output'):
    """
        :param output_directory: either '/output' or '/output/data/enchdetails/advancements'
    """

    start_time = time()

    try:
        df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')  # Creates a DataFrame from the spreadsheet
    except FileNotFoundError:
        print("[Error] Could not find the spreadsheet 'EnchantmentDetails.xlsx', please make sure it is downloaded and in the same folder as the scripts!")
        exit()
    enchantments = df['Enchantment'].tolist()  # Converts the spreadsheet column "Enchantment" to a list so it can be indexed later

    if output_directory == '/output':
        rmtree(os.path.dirname(__file__) + output_directory)
        os.mkdir('output')

    for enchant in enchantments:  # Loop through each enchantment file
        new_file = open(f'{output_directory.strip("/")}/{enchant}.json', 'w')
        new_file.truncate()  # Removes contents of the file
        new_file.write(f'{{\n\t"criteria": {{\n\t\t"requirement": {{\n\t\t\t"trigger": "minecraft:inventory_changed", \n\t\t\t"conditions": {{\n\t\t\t\t"items": [\n\t\t\t\t\t{{\n\t\t\t\t\t\t"items": [ "minecraft:enchanted_book" ], \n\t\t\t\t\t\t"nbt": "{{StoredEnchantments:[{{id:\\"minecraft:{enchant}\\"}}]}}" \n\t\t\t\t\t}}\n\t\t\t\t]\n\t\t\t}}\n\t\t}}\n\t}}, \n\t"rewards": {{\n\t\t"function": "enchdetails:{enchant}" \n\t}}\n}}')
        new_file.close()

    if __name__ == '__main__':
        print(f'[Info] Generated 39 files in {round(time() - start_time, 3)} seconds')


if __name__ == '__main__':
    main()
