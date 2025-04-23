import sys

print()  # wypisz/wydrukuj
print("Radek")
print('Radek')
# Radek
# Radek
# print("Radek')
# ctrl / - komentarz
#         File "C:\Users\CSComarch\PycharmProjects\PythonAnalizaDanych\pierwszy.py", line 6
#     print("Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 6)

# type() - sprawdzenie typu danych
print(type("Radek"))  # tekstowe, str <class 'str'>

print("39" + "14")  # konkatenacja, łączenie stringów 3914

print(39 + 14)  # 53, operacja matematyczna

# print(39 + "14") #           ~~~^~~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# # silne typowanie

print(type(39))  # <class 'int'>, liczby calkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# zmienna - pudełko na dane
# snake_case
# kebab-case

# typowanie dynamiczne
name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>

name = 67
print(name)
print(type(name))  # <class 'int'>

age = 48
print(age)
print(type(age))  # <class 'int'>


# podpowiedzi typów
name: str = 90
print(type(name))
print(name) # 90
name = "Radek"
# mypy
# pip install mypy
# (.venv) radoslawjaniak@mac PythonAnalizaDanych % mypy pierwszy.py
# pierwszy.py:42: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:52: error: Name "name" already defined on line 38  [no-redef]
# Found 2 errors in 1 file (checked 1 source file)