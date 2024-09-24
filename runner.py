from functions import calculate, is_valid_operator
from AppSettings import decimal_places
from logs.logger import log_operation, log_history, show_history

# Пам'ять для збереження результатів
memory = None

def get_input():
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /, ^, %, √): ")
        num2 = None
        if operator != '√':
            num2 = float(input("Введіть друге число: "))
        return num1, operator, num2
    except ValueError:
        print("Неправильний ввід. Спробуйте знову.")
        return get_input()

def store_in_memory(result):
    global memory
    memory = result
    print(f"Результат {result} збережений у пам'яті.")

def recall_memory():
    if memory is not None:
        print(f"Збережене значення: {memory}")
        return memory
    else:
        print("Пам'ять порожня.")
        return None

def ask_to_continue():
    return input("Бажаєте виконати ще одне обчислення? (так/ні): ").lower() == 'так'

# Основна функція
def calculator():
    print(f"Результати будуть відображатися з {decimal_places} десятковими знаками.")
    while True:
        num1, operator, num2 = get_input()

        if not is_valid_operator(operator):
            print("Неправильний оператор. Спробуйте ще раз.")
            continue

        try:
            result = calculate(num1, operator, num2)
            result = round(result, decimal_places)
            print(f"Результат: {result}")
            store_in_memory(result)

            # Логування операції в файл історії
            expression = f"{num1} {operator} {num2 if num2 is not None else ''}"
            log_operation(f"{expression} = {result}")
            log_history(expression, result)  # Додати в історію

        except (ZeroDivisionError, ValueError) as e:
            print(e)

        if input("Хочете переглянути історію обчислень? (так/ні): ").lower() == 'так':
            show_history()

        if not ask_to_continue():
            break

if __name__ == "__main__":
    calculator()

