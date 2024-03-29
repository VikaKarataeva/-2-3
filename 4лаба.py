def div_by_3(a):
    if a % 3 == 0:
        return True
    else:
        return False

a = int(input("Введите число: "))
if div_by_3(a):
    print(f"{a} делится на 3")
else:
    print(f"{a} не делится на 3")

def div_by_100():
    number = input("Введите число: ")

    if number.isdigit():
        number = int(number)
        if number != 0:
            result = 100 / number
            print(f"Результат деления 100 на {number} равен {result}")
        else:
            print("Ошибка: деление на ноль.")
    else:
        print("Ошибка: введено не число.")

div_by_100()

def magic_date(date):
    day, month, year = map(int, date.split('.'))
    if day * month == year % 100:
        return True
    else:
        return False

user_date = input("Введите дату в формате 'дд.мм.гггг': ")
if magic_date(user_date):
    print("Это магическая дата!")
else:
    print("Это не магическая дата.")


    def ticket(ticket_number):
        if len(ticket_number) % 2 != 0:
            return False

        a = len(ticket_number) // 2
        first_half_sum = sum(map(int, ticket_number[:a]))
        second_half_sum = sum(map(int, ticket_number[a:]))

        if first_half_sum == second_half_sum:
            return True
        else:
            return False

    ticket_num = input("Введите номер билета: ")
    if ticket(ticket_num):
        print("Это счастливый билет!")
    else:
        print("Это не счастливый билет.")




