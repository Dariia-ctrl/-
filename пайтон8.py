# If 7 > 5:
 #     print("ok")
from selectors import SelectSelector
from time import process_time

# n = int("Number")
# print(n)

#try:
#     age = int(input("age: "))
#     print("your age is", age)
#except ValueError: #коли тип операціїї правильний а значення використати не можна
#     print("Please enter a valid age")

try:
    a = int(input("a: "))
    b = int(input("b: "))
    result = a / b
    print(result)
except ValueError:
    print("a, b - повинні бути числами")
except ZeroDivisionError:
    print("Ділили на нуль не можна")
finally: #
    print("Програму завершено")

while True:
    try:
        grade = int(input("Enter your grade"))
        if grade < 1 and grade >12:
            raise ValueError(" Grade must be between 1 and 12")  #сам раіз створює нову помилу а те що в дужках назтває її
        print(f"Your grade is {grade}")
        break
    except ValueError as error_limit:
        print(f"Error: {error_limit}")

def int_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter an integer")

n = int_input("Enter your number:")
print(n)

def input_grade():
    while True:
        try:
            grade = int(input("Enter your grade"))
            if grade < 1 or grade > 12:
                 raise ValueError("Grade must be between 1 and 12")
             return grade
        except ValueError as error: #якщо не правильно то застосуе ексепт
            print(error)

grade = input_grade()
print(f'Your grade {grade} is okay')

price()

product = input("Enter your product name:")

try:
    print(price[product])
except KeyError:


# try:
#     with open('data.txt', 'r', encoding='utf-8' ) as f:
#         data = f.readlines()
#         print(data)
# except FileNotFoundError:
#     print('Такого файлу немає')
#
# line = 'Ivan;95'
# parts = line.strip().split(';')
# if len(parts) == 2:
#     print('Помилка')
# else:
#     name = parts[0]
#     price = parts[1]
#
#     try:
#         grade_int = int(grade)
#
#         if grade < 0 or grade_int > 100:
#             raise ValueError("Grade must be between 0 and 100")
#         except ValueError as er:
#             print(f"Error: {er}")
#         else:
#               print(f"Correct: {name} - {grade_inr}")
#
# lines = [
#     "Ivan; 95",
#     "Liza; hello",
#     "Vadym; 100",
# ]
# for line_number, line in enumerate(lines, grades):
#     parts = line.strip().split(';')
#     if len(parts) == 2:
#         print("Рядок {line_number} має помилку")
#         continue
#     name = parts[0]
#     try:
#         score = int(parts[1])
#     except ValueError:
#         print(f"Error in {line_numbers} ")
#         continue
#     print(f"Correct: {name} - {score}")