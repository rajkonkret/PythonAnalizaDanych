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
print(name)  # 90
name = "Radek"
# mypy
# pip install mypy
# (.venv) radoslawjaniak@mac PythonAnalizaDanych % mypy pierwszy.py
# pierwszy.py:42: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:52: error: Name "name" already defined on line 38  [no-redef]
# Found 2 errors in 1 file (checked 1 source file)

tekst = "Witaj Świecie"

print(tekst)
print(type(tekst))

# teksty są niemutowalne
# """ Return a copy of the string converted to uppercase. """
tekst.upper()
print(tekst)
print(tekst.upper())
zmienna = tekst.upper()
print(zmienna)
# WIATJ ŚWIECIE
# WIATJ ŚWIECIE

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie

zmienna1 = "GROSS"
zmienna2 = "groẞ"

print(zmienna1.lower() == zmienna2.lower())  # False
print(zmienna1.casefold() == zmienna2.casefold())  # True

print(1 != 8)  # różne # True
# zmienne logiczne True, False, boolean
print(int("39"))  # 39 int
print(str(39))  # 39 str

print(int(True))  # 1
print(int(False))  # 0

print(bool(100))  # True
print(bool("radek"))  # True

print(bool(0))  # False
print(bool(""))  # False

# None - odpowiednik null, stan nieokreslony, nie wiem

temp = 36.6
print(type(temp))  # <class 'float'>
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(0.1 + 0.9)  # 1.0
print(0.1 + 0.2)  # 0.30000000000000004 bład zaokraglenia
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345

# f - string format
print(f"Nazywam się {name}")
print("Nazywam się {}".format(name))
# Nazywam się Radek
# Nazywam się Radek

liczba = 3.900001
print(f"Wersja pythona: {liczba:.2f}")  # Wersja pythona: 3.90
print(f"""
Tekst
    wielolinijkowych""")
# "Tekst
#     wielolinijkowych"
"""Komentarz
    wielolinijkowy"""

print(print.__doc__)

starszy = "Mam  na imię %s"  # %s - str
print(starszy % name)  # Mam  na imię Radek
print("Wynik:", liczba)  # Wynik: 3.900001
#  sep=' ', end='\n'
print("Wynik:", liczba, sep="....")  # Wynik:....3.900001

print(100 / 2)  # 50.0 float
print(100 // 3)  # cześć całkowita dzielenia 33
print(100 % 3)  # modulo - reszta z dzielenia, 1 bo 33 * 3 + 1 = 100

zysk = 34567890123
print(f"Nasza duża liczba: {zysk}")  # Nasza duża liczba: 34567890123
print(f"Nasza duża liczba: {zysk:,}")  # Nasza duża liczba: 34,567,890,123
zysk = 34567899.987
print(f"Nasza duża liczba: {zysk:,}")  # Nasza duża liczba: 34,567,899.987
print(f"Nasza duża liczba: {zysk:_}")  # Nasza duża liczba: 34,567,899.987

parametr = 10_000_000_000
print(parametr)
print(type(parametr))
# 10000000000
# <class 'int'>

encoded_text = tekst.encode("utf-8")  # kodujemy do utf-8
print(encoded_text)  # b'Witaj \xc5\x9awiecie'
print(type(encoded_text))  # <class 'bytes'>
print(encoded_text.decode('utf-8'))  # Witaj Świecie
