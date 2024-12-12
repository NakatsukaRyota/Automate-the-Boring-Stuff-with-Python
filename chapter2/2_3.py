name = ""
while not name:
    print("名前を入力してください: ")
    name = input()
print("同伴者は何人ですか？")
num_of_guests = int(input())
if num_of_guests:
    print("同伴者用の場所があるか確認してください。")
print("受け付けました。")
