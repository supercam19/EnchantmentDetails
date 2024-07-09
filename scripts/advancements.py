import os
from shutil import rmtree
from time import time
import json

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
        if os.path.exists(os.path.dirname(__file__) + output_directory):
            rmtree(os.path.dirname(__file__) + output_directory)
        os.mkdir('output')

    for enchant in enchantments:  # Loop through each enchantment file
        new_file = open(f'{output_directory.strip("/")}/{enchant}.json', 'w')
        new_file.truncate()
        json.dump(json.loads('{"criteria":{"requirement":{"trigger":"minecraft:inventory_changed","conditions":{"items":[{"items":"minecraft:enchanted_book","predicates":{"minecraft:stored_enchantments":[{"enchantments":"' + enchant + '","levels":{"min":0,"max":5}}]}}]}}},"rewards":{"function":"enchdetails:enchantments/' + enchant + '"}}'), new_file, indent=2)
        new_file.close()

    if __name__ == '__main__':
        print(f'[Info] Generated {len(enchantments)} files in {round(time() - start_time, 3)} seconds')


if __name__ == '__main__':
    main()
