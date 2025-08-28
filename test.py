def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_result
def say_hello(name):
    return f"Hello, {name}"

print(say_hello("Alice"))  # Должно вывести "HELLO, ALICE"