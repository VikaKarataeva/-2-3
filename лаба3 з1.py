N = int(input("Введите количество слов: "))
words = []

for i in range(N):
    word = input(f"Введите {i+1}-е слово: ")
    words.append(word)

result = ' '.join(words)
print("Результат:", result)
