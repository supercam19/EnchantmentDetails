# EnchantmentDetails

A small datapack that adds descriptions to enchantment books

This datapack will have nearly no effect on performance - There is no code that runs every tick.

 ![Preview image](example.png)

## Compatibility
Use this table to check if your minecraft version will be compatible with the datapack. These are only officially tested versions, but all after 1.17 should be compatible <br/>
Date format is mm/dd/yyyy <br/>
Note that this datapack will never be ported to pre 1.17 

|   | MC Version | Datapack Version | Date       |
|---|------------|------------------|------------|
| ✅ | 1.17.*     | 1.2.0            | 05/02/2022 |
| ✅ | 1.18.*     | 1.2.0            | 05/01/2022 |
| ✅ | 1.19.*     | 1.3.0            | 08/17/2022 |
| ✅ | 1.21.*     | 1.4.0            | 07/10/2024 |

## How to install
This datapack can be installed like any other datapack, there is nothing extra to do before it works.

1. Download the version you want from here: [Latest](https://github.com/supercam19/EnchantmentDetails/releases/latest) | [All Releases](https://github.com/supercam19/EnchantmentDetails/releases)
2. Press WIN + R and type "%appdata%" (without quotation marks)
3. In the file explorer window that popped up, navigate to ".minecraft/saves"
4. Find the world you wish to add the datapack to
5. Once in the world folder, navigate to the "datapacks" folder and drop the datapack file you downloaded earlier into that folder
6. Start your minecraft world, or if it's already open do "/reload"

 ## Modifications
 If you wish to modify this datapack, feel free to use the python scripts found inside of the scripts/ directory. They are used to generate all the files for advancements, functions and item_modifiers.

Theses scripts require the pandas library to read the spreadsheet file.
```
pip install pandas
```

The enchantment names (as given in Minecraft's code), the descriptions and what items the enchants apply to can be edited in the spreadsheet "Enchantment Details.xlsx".
