enchantments = ("sharpness", "smite", "bane_of_arthropods", "knockback", "fire_aspect",
                "sweeping_edge", "protection", "fire_protection", "feather_falling", "blast_protection",
                "projectile_protection", "respiration", "aqua_affinity", "depth_strider",
                "frost_walker", "soul_speed", "efficiency", "silk_touch", "unbreaking",
                "looting", "fortune", "luck_of_the_sea", "lure", "power", "flame", "punch",
                "infinity", "thorns", "mending", "binding_curse", "vanishing_curse", "loyalty",
                "impaling", "riptide", "channeling", "multishot", "quick_charge", "piercing")

for enchant in enchantments:
    new_file = open(f'output/{enchant}.json', 'w')
    new_file.truncate()
    new_file.write(f'{{"criteria": {{"requirement": {{"trigger": "minecraft:inventory_changed", "conditions": {{"items": [ {{"items": [ "minecraft:enchanted_book" ], "nbt": "{{StoredEnchantments:[{{id:\\"minecraft:{enchant}\\"}}]}}" }}]}}}}}}, "rewards": {{"function": "enchdetails:{enchant}" }}}}')
    new_file.close()
