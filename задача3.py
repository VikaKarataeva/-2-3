a = int(input("введите год"))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print(f" год {a} високосный")
else:
        print("год не високосный")