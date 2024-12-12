def add_comma(lists):
    for item in lists:
        if item != lists[-1]:
            print(item, end = ", ")
        else:
            print("and " + item)

spam = ["apples", "bananas", "tofu", "cats"]
lists = []

add_comma(spam)
add_comma(lists)