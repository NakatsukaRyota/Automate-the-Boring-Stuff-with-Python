def spam():
    global eggs
    eggs = "spam"

def babon():
    eggs = "bacon"

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)