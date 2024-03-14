words = []

while True:
    word = input("Введите слово (для остановки введите 'stop'): ")
    if word.lower() == 'stop':
        break
    words.append(word)

result = ' '.join(words)
print("Результат:", result)