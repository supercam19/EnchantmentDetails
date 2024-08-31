$execute store success score $descriptions ench.temp run data get entity @s Inventory[{Slot:$(itter)b}].components.minecraft:lore
$execute store result score $descriptions ench.temp run data get entity @s Inventory[{Slot:$(itter)b}].components.minecraft:lore
$execute store result score $enchantments ench.temp run data get entity @s Inventory[{Slot:$(itter)b}].components.minecraft:stored_enchantments.levels
scoreboard players operation $enchantments ench.temp *= $lore-multiplier ench.temp
scoreboard players set $success ench.temp 0
execute if score $descriptions ench.temp < $enchantments ench.temp run scoreboard players set $success ench.temp 1