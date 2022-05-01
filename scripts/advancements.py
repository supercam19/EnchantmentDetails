import pandas as pd
import os
from shutil import rmtree


def main(output_directory='/output'):
    """
        :param output_directory: either '/output' or '/output/data/enchdetails/advancements'
    """
    df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')  # Creates a DataFrame from the spreadsheet
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
    main()
