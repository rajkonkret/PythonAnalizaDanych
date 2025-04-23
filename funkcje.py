# funkcja -  fragment kodu , można wykonać w dowolnym momencie, może przyjac argumenty

# deklaracja funkcji
def witaj():
    print("Witaj!!")


# wykonannie funkcji
witaj()  # Witaj!!


# funkcja zwraca wynik
def ksero(tekst: str, ile: int):
    """
    Ta funkcja zwraca string pomnożony zadaną ilośc razy
    :param tekst:
    :param ile:
    :return:
    """
    return str(tekst) * ile


wynik = ksero("Radek", 5)
print(wynik)  # RadekRadekRadekRadekRadek
print(ksero(5, 5))  # 55555


def ksero2(tekst: str, ile=1):  # parametr z wartością domyślną
    """
    Ta funkcja zwraca string pomnożony zadaną ilośc razy
    :param tekst:
    :param ile:
    :return:
    """
    return str(tekst) * ile


print(ksero2("Radek"))  # Radek
print(ksero2("Radek", 3))


# RadekRadekRadek

def ksero3(tekst: str = "treść", ile=1):  # parametr z wartością domyślną
    """
    Ta funkcja zwraca string pomnożony zadaną ilośc razy
    :param tekst:
    :param ile:
    :return:
    """
    return str(tekst) * ile


print(ksero3())  # treść
print(ksero3("Radek", 3))  # pozycyjne argumenty
print(ksero3(tekst="Radek", ile=3))  # nazwane argumenty


# RadekRadekRadek
# RadekRadekRadek


def ile_razy(*ile, **co):
    print(ile)
    print(co)


ile_razy(4, 5, 6)  # (4, 5, 6)
ile_razy(4, 5, 6, name="Radek", status="OK")


# (4, 5, 6)
# {'name': 'Radek', 'status': 'OK'}


def multi(a, b):
    try:
        return a * b
    except TypeError:
        return "nieprawidłowe dane"
    except ValueError:
        return 0


def multi2(a, b):
    try:
        return a * b
    except Exception as e:
        return "nieprawidłowe dane:", e.args


print(multi(4, 4))  # 16
print(multi("4", 4))  # 4444
print(multi("4", None))  # nieprawidłowe dane

print(multi2(4, 4))  # 16
print(multi2("4", 4))  # 4444
print(multi2("4", None))
# 16
# 4444
# ('nieprawidłowe dane:', ("can't multiply sequence by non-int of type 'NoneType'",))
