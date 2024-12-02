# Калькулятор v1

num = input ("Выберете действие (+, -, *, /): ")

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if num == "+":
    c = a + b
    print("Результат: " + str(c))

elif num == "-":
    c = a - b
    print("Результат: " + str(c))

elif num == "*":
    c = a * b
    print("Результат: " + str(c))

elif num == "/":
    c = a / b
    print("Результат: " + str(c))

else:
    print("Выбрана неверная операция")