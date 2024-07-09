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
    :param output_directory: either '/output' or '/output/data/enchdetails/functions'
    """
    start_time = time()

    try:
        df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')  # Creates a DataFrame from the spreadsheet
    except FileNotFoundError:
        print("[Error] Could not find the spreadsheet 'EnchantmentDetails.xlsx', please make sure it is downloaded and in the same folder as the scripts!")
        exit()
    enchantments = df['Enchantment'].tolist()  # Converts the spreadsheet column "Enchantment" to a list so it can be indexed later

    if output_directory == '/output':
        rmtree(os.path.dirname(__file__) + '/output')
        os.mkdir('output')

    for enchant in enchantments:  # Loop through each enchantment file
        new_file = open(f'{output_directory.strip("/")}/{enchant}.mcfunction', 'w')  # Opens the file or creates one if it doesn't
        new_file.write(f'data merge storage ench {{details:{{"itter":0,"name":{enchant}}}}}\n')
        new_file.write('function enchdetails:find with storage ench details\n')
        new_file.write(f'advancement revoke @s only enchdetails:{enchant}')
        new_file.close()

    if __name__ == '__main__':
        print(f'[Info] Generated {len(enchantments)} files in {round(time() - start_time, 3)} seconds')


if __name__ == '__main__':
    main()

