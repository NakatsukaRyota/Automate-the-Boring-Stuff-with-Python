def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1

while True:
    try:
        print("数字を入力してください")
        num = int(input())
        break
    except ValueError:
        print("不正な値です。")

while True:
    num = collatz(num)
    print(num)
    if num == 1:
        break
