execute store result score $ench ench.temp run data get storage ench details.itter
execute if score $ench ench.temp matches 36.. run return 1
function enchdetails:checksum with storage ench details
$execute if items entity @s container.$(itter) enchanted_book[minecraft:stored_enchantments~[{enchantments:"minecraft:$(name)"}]] if score $success ench.temp matches 1 run function enchdetails:modify with storage ench details
execute store result storage ench details.itter int 1 run scoreboard players add $ench ench.temp 1
function enchdetails:find with storage ench details