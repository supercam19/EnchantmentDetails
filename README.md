# EnchantmentDetails

A small datapack that adds descriptions to enchantment books

This datapack will have nearly no effect on performance - There is no code that runs every tick.

 ![Preview image](example.png)

## Compatibility

Use this table to check if your minecraft version will be compatible with the datapack.
Date format is mm/dd/yyyy

|   | MC Version | Datapack Version | Date       |
|---|------------|------------------|------------|
| ✅ | 1.17.*     | 1.2.0            | 05/02/2022 |
| ✅ | 1.18.*     | 1.2.0            | 05/01/2022 |
| ✅ | 22w17a     | 1.2.0            | 05/02/2022 |

 ## Modifications
 If you wish to modify this datapack, feel free to use the python scripts found inside of the scripts/ directory. They are used to generate all the files for advancements, functions and item_modifiers.

Theses scripts require the pandas library to read the spreadsheet file.
```
pip install pandas
```

The enchantment names (as given in Minecraft's code), the descriptions and what items the enchants apply to can be edited in the spreadsheet "Enchantment Details.xlsx".
