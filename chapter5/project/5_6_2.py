stuff = {"ロープ": 1, "たいまつ": 6, "金貨": 42, "手裏剣": 1, "矢": 12}

def display_inventory(inventory):
    counter = 0
    print("持ち物リスト:")
    for k, v in inventory.items():
        print(str(v) + " " + k)
        counter += v

    print("アイテム総数: " + str(counter))

display_inventory(stuff)

