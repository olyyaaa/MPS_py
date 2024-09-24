from const_GlobalVariables.operators import OPERATORS
import math

# Основна функція обчислень
def calculate(num1, operator, num2=None):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Помилка: ділення на нуль!")
        return num1 / num2
    elif operator == '^':
        return num1 ** num2
    elif operator == '%':
        return num1 % num2
    elif operator == '√':
        if num1 < 0:
            raise ValueError("Помилка: не можна знайти квадратний корінь з від'ємного числа!")
        return math.sqrt(num1)
    else:
        raise ValueError("Неправильний оператор")

# Перевірка правильності оператора
def is_valid_operator(operator):
    return operator in OPERATORS
