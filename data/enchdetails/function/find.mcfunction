execute store result score $ench ench.temp run data get storage ench details.itter
execute if score $ench ench.temp matches 36.. run return 1

$execute if items entity @s container.$(itter) enchanted_book[minecraft:stored_enchantments~[{enchantments:"minecraft:$(name)"}]] run function enchdetails:subfind
execute store result storage ench details.itter int 1 run scoreboard players add $ench ench.temp 1
function enchdetails:find with storage ench details