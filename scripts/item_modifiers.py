import pandas as pd

df = pd.read_excel('Enchantment Details.xlsx', sheet_name='Sheet1')
enchantments = df['Enchantment'].tolist()
descriptions = df['Description'].tolist()
applications = df['Applications'].tolist()


for enchant in range(len(enchantments)):
    new_file = open(f'output/{enchantments[enchant]}.json', 'w')
    new_file.truncate()
    new_file.write(f'{{\n\t\"function\": \"set_lore\",\n\t\"lore\": [{{\"text\":\"{descriptions[enchant]}\",\"italic\":false,\"color\":\"#e699e6\"}},{{\"text\":\"For: {applications[enchant]}\",\"italic\":true,\"color\":\"#bfbfbf\"}}],\n\t\"replace\": \"true\"\n}}')
    new_file.close()