def z1(numbers):
    user_number = int(input("введите число: "))
    if user_number in numbers:
        print("поздравляю, Вы угадали число!")
    else:
        print("нет такого числа!")

    print("исходный список:", numbers)
    print("число пользователя:", user_number)


numbers = [3, 7, 12, 5, 9]
z1(numbers)


def z2(lst):
    a = set()
    for item in lst:
        if lst.count(item) > 1:
            a.add(item)

    if a:
        print("Найдены повторяющиеся элементы:", a)
    else:
        print("Повторяющихся элементов нет.")

my_list = [3, 5, 3, 8, 2, 6, 5]
z2(my_list)

def days(day_names):
    weekends = int(input("сколько выходных на неделе вы хотите? "))
    weekend_list = day_names[:weekends]
    workdays_list = day_names[weekends:]

    print("ваши выходные дни:")
    for day in weekend_list:
        print("-", day)

    print("ваши рабочие дни:")
    for day in workdays_list:
        print("-", day)

days_of_week = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
days(days_of_week)


def z5(group1, group2):
    team = tuple(group1[:5] + group2[:5])

    print("исходные списки групп:")
    print("группа 1:", group1)
    print("группа 2:", group2)
    print("\nновый полученный кортеж:")
    print(team)

    print("\nдлина кортежа:", len(team))

    team_sorted = tuple(sorted(team))
    print("\nотсортированный кортеж:")
    print(team_sorted)

    if "Иванов" in team:
        count_ivanov = team.count("Иванов")
        print("\nФамилия 'Иванов' входит в команду.")
        print("количество вхождений фамилии 'Иванов':", count_ivanov)
    else:
        print("\nФамилия 'Иванов' не входит в команду.")


group1 = ["Иванов", "Петров", "Сидоров", "Козлов", "Смирнов", "Васильев", "Морозов", "Никитин", "Зайцев", "Белов"]
group2 = ["Соколов", "Лебедев", "Кузнецов", "Козлов", "Попов", "Козлова", "Иванова", "Смирнова", "Никитина", "Петрова"]

z5(group1, group2)
