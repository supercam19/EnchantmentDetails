enchantments = ("sharpness", "smite", "bane_of_arthropods", "knockback", "fire_aspect",
                "sweeping_edge", "protection", "fire_protection", "feather_falling", "blast_protection",
                "projectile_protection", "respiration", "aqua_affinity", "depth_strider",
                "frost_walker", "soul_speed", "efficiency", "silk_touch", "unbreaking",
                "looting", "fortune", "luck_of_the_sea", "lure", "power", "flame", "punch",
                "infinity", "thorns", "mending", "binding_curse", "vanishing_curse", "loyalty",
                "impaling", "riptide", "channeling", "multishot", "quick_charge", "piercing")

for enchant in enchantments:
    new_file = open(f'output/{enchant}.mcfunction', 'w')
    new_file.truncate()
    for slot in range(36):
        new_file.write(f'execute if entity @s[nbt={{Inventory:[{{Slot:{slot}b, id:"minecraft:enchanted_book", tag:{{StoredEnchantments: [{{id: "minecraft:{enchant}"}}]}}}}]}}] run item modify entity @s container.{slot} enchdetails:{enchant}\n')
    new_file.write(f'advancement revoke @s only enchdetails:{enchant}')
    new_file.close()
