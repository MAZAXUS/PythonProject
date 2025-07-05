# Арифметические операции
a = 10
b = 2

sum_result = a + b
diff_result = a - b
mult_result = a * b
div_result = a / b

print(sum_result)
print(diff_result)
print(mult_result)
print(div_result)


# Типы данных

num = 15
text = "Python"
is_active = False

print(type(num))
print(type(text))
print(type(is_active))


# Преобразование типов данных

number_str = "123"
float_num = 45.8

number_int = int(number_str)
print("Строку в число:", number_int)

float_str = str(float_num)
print("Строка:", f'"{float_str}"')


# Операции сравнения

x = 10
y = 5

print("10 > 5", x > y)
print("10 < 5",x < y)
print("10 == 5", x == y)
print("10 != 5", x != y)


# Именование переменных

first_number = 10
my_variable = "text"
yazik = "Python"

print(first_number)
print(my_variable)
print(yazik)


# Переопределение переменных

price = 100
discount = 20
price = price - discount
final_price = price

print(final_price)


# Операции сравнения и логика

age = 18
is_student = True

access_allowed = age >= 18 and is_student
print("Доступ разрешён:", access_allowed)