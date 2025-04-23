# liczba = int(input("Podaj liczbę"))
# if liczba < 5:
#     print("Przegrałeś")
# elif liczba > 5:
#     print("Spróbuj ponownie")
# elif liczba == 5:
#     print("Wygrałeś")
# else: # wartość domyślna
#     print("Nieznany bład")
# # wcięcia oddzielają bloki programu

# od python 3.10
lang = input("Podaj znany ci język programowania")

match lang.casefold().strip():  # strip() - usuniecie białych znaków
    case "python":
        print("Możesz zostac data scientist")
    case "php":
        print("Możesz zostać backend developerem")
    case "solidity":
        print("Możesz zostać blockchain developerem")
    case _:
        print("inny przypadek")
