# kolekcje - przechowuje wiele elemntów, różnego typu na raz

# lista  - zachowuje kolejnosc przy dodawaniu elementów
lista = []
lista_pusta = list()
print(lista)
print(type(lista))
# []
# <class 'list'>
lista_pusta.append("andrzej")
lista_pusta.append("tomek")
lista_pusta.append("zenek")
lista_pusta.append("paulina")
lista_pusta.append("jakub")
print(lista_pusta)  # ['andrzej', 'tomek', 'zenek', 'paulina', 'jakub']
lista_pusta.sort()
print(lista_pusta)  # ['andrzej', 'jakub', 'paulina', 'tomek', 'zenek']
lista_pusta.append(345)
print(lista_pusta)  # ['andrzej', 'tomek', 'zenek', 'paulina', 'jakub', 345]
# lista_pusta.sort()  # TypeError: '<' not supported between instances of 'int' and 'str'

lista_pusta.insert(1, "Magda")
print(lista_pusta)
# ['andrzej', 'Magda', 'jakub', 'paulina', 'tomek', 'zenek', 345]
# indeksy od 0
print(lista_pusta[0])  # andrzej
# print(lista_pusta[23])  # IndexError: list index out of range
print(lista_pusta[-1])  # 345, ostatni eleemnt z listy

# slicowanie
print(lista_pusta[0:2])  # 0,1 ['andrzej', 'Magda']
print(lista_pusta[:2])  # ['andrzej', 'Magda']
print(lista_pusta[1:])  # ['Magda', 'jakub', 'paulina', 'tomek', 'zenek', 345]

print(len(lista_pusta))  # długosc 7
print(lista_pusta[1:-1])  # ['Magda', 'jakub', 'paulina', 'tomek', 'zenek']
print(lista_pusta[0:4:2])  # start:stop:krok, ['andrzej', 'jakub']
print(lista_pusta[::-1])
# [345, 'zenek', 'tomek', 'paulina', 'jakub', 'Magda', 'andrzej']

print(lista_pusta)  # ['andrzej', 'Magda', 'jakub', 'paulina', 'tomek', 'zenek', 345]
print(lista_pusta[45:90])  # []

print(lista_pusta.pop())  # usunie ostatni element 345
print(lista_pusta)  # ['andrzej', 'Magda', 'jakub', 'paulina', 'tomek', 'zenek']
print(lista_pusta.pop(4))  # tomek, usunięcie po indeksie

lista_pusta.remove("Magda")
print(lista_pusta)  # ['andrzej', 'jakub', 'paulina', 'tomek', 'zenek']

osoby = ['Tomek', 'Ewa', "Adam"]
print(osoby)
osoby.extend(lista_pusta)
print(osoby)
# ['Tomek', 'Ewa', 'Adam', 'andrzej', 'jakub', 'paulina', 'zenek']
nowa_lista = osoby + lista_pusta
print(nowa_lista)
# ['Tomek', 'Ewa', 'Adam', 'andrzej', 'jakub', 'paulina', 'zenek', 'andrzej', 'jakub', 'paulina', 'zenek']

nnn_lista = nowa_lista  # kopia referencji, adresu
list_copy = nowa_lista.copy()  # kopia eleemntów listy
print(nnn_lista)
print(nowa_lista)
nowa_lista.clear()  # usunięcie elementów  listy
print(nnn_lista)
print(nowa_lista)
print(list_copy)
# []
# []
# ['Tomek', 'Ewa', 'Adam', 'andrzej', 'jakub', 'paulina', 'zenek', 'andrzej', 'jakub', 'paulina', 'zenek']
print(id(nnn_lista))  # 4377891328
print(id(nowa_lista))  # 4377891328
print(id(list_copy))  # 4381276288

# krotka (tuple) - niemutowalna lista
# pozwala lepiej zarządzać pamięcią
krotka = (23, 34, 54, "Radek")
print(krotka)  # (23, 34, 54, 'Radek')
print(krotka[:2])  # (23, 34)
krotka1 = "radek", "Tomek", "Zenek"
print(type(krotka1))  # <class 'tuple'>

krotka2 = ("Radek",)
krotka3 = "Radek",
krotka4 = "Radek"
print(type(krotka2), type(krotka3), type(krotka4))  # <class 'tuple'> <class 'tuple'> <class 'str'>
print(type(()))  # <class 'tuple'>

print(len(krotka))
# a, b, c = krotka # ValueError: too many values to unpack (expected 3)
a, b, *c = krotka  # * worek na pozostałe dane
print(a, b, c)  # 23 34 [54, 'Radek']
a, *b, c = krotka
print(a, b, c)  # 23 [34, 54] Radek
# krotka[5] = 4 # TypeError: 'tuple' object does not support item assignment

# słownik
# odpowiednik jsona
oceny = {"Tomek": 4,
         "Radek": 5,
         "Agata": 5,
         "Jacek": 4}
print(oceny)  # {'Tomek': 4, 'Radek': 5, 'Agata': 5, 'Jacek': 4}
print(type(oceny))  # <class 'dict'>
# null -> None
print(oceny["Tomek"])  # 4
print(oceny.get("Tomek"))  # 4
print(oceny.get("tomek"))  # None
print(oceny.values())
print(oceny.keys())
print(oceny.items())
# dict_values([4, 5, 5, 4])
# dict_keys(['Tomek', 'Radek', 'Agata', 'Jacek'])
# dict_items([('Tomek', 4), ('Radek', 5), ('Agata', 5), ('Jacek', 4)])
oceny["Agata"] = 6
print(oceny)  # {'Tomek': 4, 'Radek': 5, 'Agata': 6, 'Jacek': 4}
oceny["Tomek"] = lista_pusta
print(oceny["Tomek"])  # ['andrzej', 'jakub', 'paulina', 'zenek']
print(oceny["Tomek"][1])  # jakub
oceny["Jacek"] = krotka3
print(oceny)
# {'Tomek': ['andrzej', 'jakub', 'paulina', 'zenek'], 'Radek': 5, 'Agata': 6, 'Jacek': ('Radek',)}
print(oceny.pop("Jacek"))  # usunie element Jacek
print(oceny)  # {'Tomek': ['andrzej', 'jakub', 'paulina', 'zenek'], 'Radek': 5, 'Agata': 6}
print(oceny.popitem())  # ('Agata', 6) - ostatni

dictionary = {}
dict_pusty = dict()
print(dictionary)
print(type(dict_pusty))
# {}
# <class 'dict'>

# set() - zbiór
# przechowuje uniklne wartości
# nie posiada indeksu
zbior1 = {45, 55, 66, 77}
zbior2 = {45, 55, 166, 177}
zbior1.add(101)
zbior1.add(102)
zbior1.add(105)
zbior1.add(77)
zbior1.add(55)
zbior1.add("55")
print(zbior1)  # {66, 101, 102, 105, '55', 45, 77, 55}

print(zbior1.difference(zbior2))
print(zbior2.difference(zbior1))
# {66, 101, 102, 105, 77, '55'}
# {177, 166}

print(zbior1.intersection(zbior2))  # {45, 55}

pusty_zbior = set()
print(pusty_zbior)
print(type(pusty_zbior))
# set()
# <class 'set'>

lista_ze_zbioru = list(zbior1)
print(lista_ze_zbioru)
print(type(lista_ze_zbioru))
# [66, 101, 102, 105, 45, 77, 55, '55']
# <class 'list'>
lista_do_zbioru = [66, 101, 102, 105, 45, 77, 77, 55, '55', 102]
zbior_z_listy = set(lista_do_zbioru)
print(zbior_z_listy)  # {66, 101, 102, 105, 45, 77, 55, '55'}
