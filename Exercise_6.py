import random

# Создаем два списка со случайными элементами
list1 = [random.randint(1, 10) for _ in range(5)]  # пример: случайные числа от 1 до 10, 5 элементов
list2 = [random.choice("abcdefghij") for _ in range(5)]  # пример: случайные буквы a-j, 5 элементов

# Создаем словарь, используя в качестве ключей элементы из list2 и в качестве значений элементы из list1
dictionary = dict(zip(list2, list1))

# Выводим списки и словарь
print("Список 1:", list1)
print("Список 2:", list2)
print("Словарь:", dictionary)
