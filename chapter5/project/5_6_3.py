dragon_loot = ["金貨", "手裏剣", "金貨", "金貨", "ルビー"]

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1


stuff = {"ロープ": 1, "たいまつ": 6, "金貨": 42, "手裏剣": 1, "矢": 12}

def display_inventory(inventory):
    counter = 0
    print("持ち物リスト:")
    for k, v in inventory.items():
        print(str(v) + " " + k)
        counter += v

    print("アイテム総数: " + str(counter))

display_inventory(stuff)
print()
add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)