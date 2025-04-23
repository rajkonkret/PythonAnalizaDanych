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
