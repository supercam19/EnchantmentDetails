import pandas as pd

<<<<<<< HEAD
df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')  # Creates a DataFrame from the spreadsheet

# Creates a list out of the three columns so they can be indexed later
=======
df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')
>>>>>>> 0fe34e1b33316b2e9d345f43865cf02c12ea2fff
enchantments = df['Enchantment'].tolist()
descriptions = df['Description'].tolist()
applications = df['Applications'].tolist()


<<<<<<< HEAD
for enchant in range(len(enchantments)):  # Loop through each enchantment file
    new_file = open(f'output/{enchantments[enchant]}.json', 'w')  # Opens the file or creates one if it doesn't exist
    new_file.truncate()  # Removes the contents of the file
=======
for enchant in range(len(enchantments)):
    new_file = open(f'output/{enchantments[enchant]}.json', 'w')
    new_file.truncate()
>>>>>>> 0fe34e1b33316b2e9d345f43865cf02c12ea2fff
    new_file.write(f'{{\n\t\"function\": \"set_lore\",\n\t\"lore\": [{{\"text\":\"{descriptions[enchant]}\",\"italic\":false,\"color\":\"#e699e6\"}},{{\"text\":\"For: {applications[enchant]}\",\"italic\":true,\"color\":\"#bfbfbf\"}}],\n\t\"replace\": \"true\"\n}}')
    new_file.close()