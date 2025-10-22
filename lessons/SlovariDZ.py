#Создай словарь fruit_colors, где ключами будут названия фруктов ('apple', 'banana', 'grape'),
#а значениями — их цвета ('red', 'yellow', 'purple'). Выведи словарь на экран

fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}
print(fruit_colors)

#Дан словарь:
#student = {"name": "Alex", "age": 20, "course": "Python"}
#Выведи на экран значение, связанное с ключом "age"

student = {"name": "Alex", "age": 20, "course": "Python"}
print(student["age"])

#Дан словарь:
#car = {"brand": "Toyota", "model": "Corolla"}
#Добавь в него новый ключ "year" со значением 2020.
#Обнови значение ключа "model" на "Camry".
#Выведи итоговый словарь.

car = {"brand": "Toyota", "model": "Corolla"}
car["year"] = 2020
car["model"] = "Camry"
print(car)

#Дан словарь:
#book = {"title": "1984","author": "George Orwell","year": 1949,"genre": "dystopia"}
#Удали ключ "year" с помощью оператора del.
#Удали ключ "genre" с помощью метода .pop().
#Выведи итоговый словарь.
#Как полностью удалять пары "ключ-значение"? Вспомни синтаксис для del и .pop().

book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "genre": "dystopia"
}
del book["year"]
book.pop("genre")
print(book)

#Дан словарь:
#laptop = {
#    "brand": "Dell",
#    "model": "XPS 15"
#    "year": 2023,
#    "OS": "Windows 11"
#}
#Выведи список всех ключей словаря
#Выведи список всех значений словаря
#Выведи список кортежей (ключ, значение)
#Какие методы словаря нужно использовать? Вспомни .keys(), .values() и .items()

laptop = {
    "brand": "Dell",
    "model": "XPS 15",
    "year": 2023,
    "OS": "Windows 11"
}

print(list(laptop.keys()))
print(list(laptop.values()))
print(list(laptop.items()))

#Дан словарь:
#weather = {
#    "city": "Москва",
#    "temperature": "20°C",
#    "humidity": "65%",
#    "wind": "5 м/с"
#}
#Проверь, есть ли в словаре ключ "pressure" (выведи True или False)
#Проверь, есть ли среди значений словаря строка "20°C" (выведи True или False)
#Дополнительно: проверь оба условия через оператор in в одном print()
#Какие методы/операторы помогут? Вспомни in для ключей и комбинацию с .values()

weather = {
    "city": "Москва",
    "temperature": "20°C",
    "humidity": "65%",
    "wind": "5 м/с"
}

print("preassure" in weather)
print("20°C" in weather.values())
print("preassure" in weather, "20°C" in weather.values())

#Дан словарь:

#smartphone = {
#    "brand": "Xiaomi",
#    "model": "Redmi Note 10",
#    "year": 2021,
#    "price": 25000
#}
#Добавь характеристику "color": "black"
#Увеличь цену на 1500 (измени значение "price")
#Проверь, есть ли ключ "OS" (выведи True или False)
#Выведи список всех характеристик в формате:
#"Характеристика: значение" (каждая пара с новой строки)
#Комбинируем методы работы со словарями!

smartphone = {
    "brand": "Xiaomi",
    "model": "Redmi Note 10",
    "year": 2021,
    "price": 25000
}

smartphone["color"] = "black"
smartphone["price"] += 1500
print("OS" in smartphone)
print(list(smartphone.items()))