# while

i = 0
while i < 3:
    print(i)
    i += 1

while True:
    print("Na jakim kursie jesteś:")
    wybor = input()
    if wybor == 'java':
        break

    print("Jesteś na kursie Pythona")
# Na jakim kursie jesteś:
# python
# Jesteś na kursie Pythona
# Na jakim kursie jesteś:
# python
# Jesteś na kursie Pythona
# Na jakim kursie jesteś:
# v
# Jesteś na kursie Pythona
# Na jakim kursie jesteś:
# assembler
# Jesteś na kursie Pythona
# Na jakim kursie jesteś:
# java

for liczba in range(3):  # 0,1,2
    print(liczba)

lista_liczb = [9, 99, 999]
nowa = []
for i in lista_liczb:
    nowa.append(i + 1)
print(nowa)  # [10, 100, 1000]

# list comprehension
lista_liczb = [9, 99, 999]
nowa2 = [i + 1 for i in lista_liczb]
print(nowa2)  # [10, 100, 1000]

print(list(range(15)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(tuple(enumerate(nowa2)))
# ((0, 10), (1, 100), (2, 1000)) numeruje kolekcje

osoba = ["Radek", 'Tomek', "Anna", "Marek", "Seweryn"]
wiek = [44, 55, 44, 33]

# Radek 44
for i in zip(osoba, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Anna', 44)
# ('Marek', 33)
for o, w in zip(osoba, wiek):
    print(o, w)
# Radek 44
# Tomek 55
# Anna 44
# Marek 33
for o, w in enumerate(zip(osoba, wiek), start=1):
    print(o, w)
# 1 ('Radek', 44)
# 2 ('Tomek', 55)
# 3 ('Anna', 44)
# 4 ('Marek', 33)
for i, (o, w) in enumerate(zip(osoba, wiek), start=1):
    print(i, o, w)
# 1 Radek 44
# 2 Tomek 55
# 3 Anna 44
# 4 Marek 33
