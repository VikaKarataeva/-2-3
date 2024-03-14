import random

correct_ans = 0
mistakes = 0

while mistakes < 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    ans = int(input(f"{num1} + {num2} = "))

    if ans == num1 + num2:
        print("Правильно!")
        correct_answers += 1
    else:
        print("Ответ неверный")
        mistakes += 1

print(f"Игра окончена. Правильных ответов: {correct_ans}")