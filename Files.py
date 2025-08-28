#Задача 1 (Работа с файлами)
#Напиши код, который создает текстовый файл numbers.txt и записывает в него числа от 1 до 10, каждое с новой строки.

chisla = open("numbers.txt", "w", encoding='utf-8')

for num in range(1,11):
    chisla.write(f"{num}\n")

chisla.close()

#Создай файл greeting.txt с помощью контекстного менеджера with и запиши в него одну строку: "Hello, Python!".
#Условия:
#Используй только конструкцию with (без ручного закрытия файла).
#Укажи кодировку utf-8

with open("greeting.txt", "w", encoding='utf-8') as hello:
    hello.write("Hello, Python!")

#Допиши в конец файла greeting.txt (который мы создали ранее) строку: "I'm learning files!"
#Условия:
#Используй режим 'a' (append) вместо 'w', чтобы не перезаписать файл.
#Не забудь добавить перенос строки (\n), если хочешь, чтобы новая строка была с новой линии.
#Примени контекстный менеджер with.

with open("greeting.txt", "a", encoding='utf-8') as hello:
    hello.write("\nI'm learning files!")