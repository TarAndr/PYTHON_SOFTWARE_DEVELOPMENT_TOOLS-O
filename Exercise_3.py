# Запрашиваем у пользователя строку
original_string = input("Введите строку: ")

# Используем цикл для обратного вывода строки
print("Обратная строка:", end=" ")
for i in range(len(original_string)-1, -1, -1):
    print(original_string[i], end="")

# Переход на новую строку для лучшего визуального восприятия
print()
