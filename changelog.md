## Update - v1.4.0 (July 9, 2024)
This update brings compatibility with the version 1.21 of Minecraft.

### Additions
 - 1.21 compatibility
 - Mace enchantment descriptions

### Changes
 - Improve most enchantment descriptions
 - Improved load times 

### Fixes
 - Fixed script not working if not output folder exists

### Removed
 - Removed generate_pack.py script because the datapack can no longer be generated completely by the provided scripts

## Update - v1.3.0 (August 17, 2022)
### Additions
 - Enchantment descriptions now show the max level the enchant can have

### Changes
 - Updated several descriptions to better reflect their enchantments

### Fixes
 - Fixed the silk touch description not making sense

## Update - v1.2.0 (May 2, 2022)
### Additions
 - New artwork for the datapack
 - Added a pack.png 
 - Added a python script to generate all the files for the datapack
 - Console logs for the python scripts (errors and info)

### Changes
 - Updated most enchantment descriptions to better describe their purpose
 - Python scripts now generate an 'output' folder if none already exist
 - Python scripts now remove all contents from the output folder before creating new files
 - Added proper json formatting to the advancement files

### Fixes
 - Fixed sweeping edge not getting a description
 - Spelling mistakes

## Update - v1.1.0 (March 27, 2022)
### Additions
 - Added the 1.19 Swift Sneak enchantment
 - Added a spreadsheet for item modifiers to make it easier to edit
 - Added an item_modifiers.py script to generate the item_modifier files

### Changes
 - Made the advancements and functions scripts read enchantment names from the spreadsheet instead of being hard-coded

## Hotfix -v1.0.1 (Feb 14, 2022)
### Fixes
 - Fixed each player only being able to change the description of each enchanted book once

## Full Release - v1.0 (Feb 2, 2022)
### Additions
 - New system to detect and update enchanted books - does not use ticking functions
 - Added changelog.md
 - Added scripts used to generate datapack files - you may use these if you wish to modify the datapack.

### Changes
 - Enchanted books can be detected anywhere in the inventory instead of just the main hand.
 - Changed to advancement based book detection - much better performance.
 - Updated README file


## Initial Release - v0.1 (Jan 17, 2022)
- Initial release of the datapack (early beta)
