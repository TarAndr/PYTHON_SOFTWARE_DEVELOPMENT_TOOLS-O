class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Создаем объекты класса "Товар"
product1 = Product("Ноутбук", 1200.0)
product2 = Product("Смартфон", 600.0)
product3 = Product("Наушники", 80.0)

# Выводим информацию о товарах
print("Товар 1:")
print("Название:", product1.name)
print("Цена:", product1.price)

print("\nТовар 2:")
print("Название:", product2.name)
print("Цена:", product2.price)

print("\nТовар 3:")
print("Название:", product3.name)
print("Цена:", product3.price)
