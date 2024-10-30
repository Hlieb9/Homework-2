a = float(input("Введіть перше число : "))
b = float(input("Введіть друге число : "))

operation = input("Введіть математичну дію : ")

if operation == '+':
    result = a + b
    print(f"Результат: {a} + {b} = {result}")
elif operation == '-':
    result = a - b
    print(f"Результат: {a} - {b} = {result}")
elif operation == '*':
    result = a * b
    print(f"Результат: {a} * {b} = {result}")
elif operation == '/':
    if b != 0:
        result = a / b
        print(f"Результат: {a} / {b} = {result}")
    else:
        print("Помилка, ділення на нуль")