$data modify storage minecraft:ench details.level set from entity @s Inventory[{Slot:$(itter)}].components."minecraft:stored_enchantments".levels."minecraft:$(name)"
function enchdetails:roman_encode with storage ench details
$item modify entity @s container.$(itter) enchdetails:$(name)