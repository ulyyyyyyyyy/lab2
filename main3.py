y = int(input("введите год"))

if (y % 4 == 0) and (y % 100 != 0):
    print("Это високосный год")
else:
    print("Это обычный год")