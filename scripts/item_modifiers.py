import pandas as pd
import os
from shutil import rmtree


def main(output_directory='/output'):
    """
        :param output_directory: either '/output' or '/output/data/enchdetails/item_modifiers'
    """
    df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')  # Creates a DataFrame from the spreadsheet
    # Creates a list out of the three columns so they can be indexed later
    enchantments = df['Enchantment'].tolist()
    descriptions = df['Description'].tolist()
    applications = df['Applications'].tolist()

    if output_directory == '/output':
        rmtree(os.path.dirname(__file__) + output_directory)
        os.mkdir('output')

    for enchant in range(len(enchantments)):  # Loop through each enchantment file
        new_file = open(f'{output_directory.strip("/")}/{enchantments[enchant]}.json', 'w')
        new_file.truncate()  # Removes the contents of the file
        new_file.write(f'{{\n\t\"function\": \"set_lore\",\n\t\"lore\": [{{\"text\":\"{descriptions[enchant]}\",\"italic\":false,\"color\":\"#e699e6\"}},{{\"text\":\"For: {applications[enchant]}\",\"italic\":true,\"color\":\"#bfbfbf\"}}],\n\t\"replace\": \"true\"\n}}')
        new_file.close()


if __name__ == '__main__':
    main()

