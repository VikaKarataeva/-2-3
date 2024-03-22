a = int(input(" введите номер места "))
if a > 54:
    print("неверный номер места")
elif a % 2 == 0 and a <= 36:
    print("верхнее место")
elif a % 2 != 0 and a <=54:
    print("нижнее место")
elif a % 2 == 0 and a >= 36:
    print("верхнее боковое место")
else:
    print("нижнее боковое место")
