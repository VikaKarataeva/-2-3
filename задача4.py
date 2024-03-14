color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")

if color1 != "красный" and color1 != "синий" and color1 != "желтый":
    print("используйте другой первый цвет: красный, синий или желтый")
elif color2 != "красный" and color2 != "синий" and color2 != "желтый":
    print("Используйте другой второй цвет: красный, синий или желтый")
elif color1 == "красный" and color2 == "синий" or color2 == "красный" and color1 == "синий":
    print("фиолетовый")
elif color1 == "красный" and color2 == "желтый" or color2 == "красный" and color1 == "желтый":
    print("оранжевый")
elif color1 == "синий" and color2 == "желтый" or color2 == "синий" and color1 == "желтый":
    print("зеленый")
else:
    print('получится', color1)
