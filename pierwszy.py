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

print(type(39)) # <class 'int'>, liczby calkowite
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)