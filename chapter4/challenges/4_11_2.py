import random
number_of_streaks = 0
for experiment_number in range(10000):
    lst = []
    string_num = ""
    for i in range(100):
        num = random.randint(0, 1)
        lst.append(num)

    for i in lst:
        string_num += str(i)

    if "111111" in string_num:
        number_of_streaks += 1
    elif "000000" in string_num:
        number_of_streaks += 1

print(f"同じ面が6連続出現する確率: {number_of_streaks / 100}%")


