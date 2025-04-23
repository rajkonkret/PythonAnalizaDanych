# klasy - szablon, przepis
# obiekt - instancja klasy

# CamelCase
class Osoba:
    """
    Dokumentacja
    """
    imie = ''
    wzrost = 0

    def przedstaw_sie(self):
        print('Nazywam się:', self.imie)

    def wypisz_wzrost(self):
        print("Mam", self.wzrost, "cm wzrostu")


czlowiek1 = Osoba()
czlowiek2 = Osoba()

czlowiek1.imie = "Radek"
czlowiek1.przedstaw_sie()  # Nazywam się: Radek

czlowiek2.imie = "Magda"
czlowiek2.przedstaw_sie()  # Nazywam się: Magda

czlowiek2.wypisz_wzrost()
czlowiek1.wypisz_wzrost()
# Mam 0 cm wzrostu
# Mam 0 cm wzrostu
print(Osoba.__doc__)  # Dokumentacja


class Osoba2:
    def __init__(self, imie: str, wzrost=177, oczy='niebieskie'):
        """
        Metoda inicjalizująca - konstruktor
        :param imie:
        :param wzrost:
        :param oczy:
        """
        self.imie = imie
        self.wzrost = wzrost
        self.oczy = oczy

    def przedstaw_sie(self):
        print('Nazywam się:', self.imie)

    def wypisz_wzrost(self):
        print("Mam", self.wzrost, "cm wzrostu")

    def ustaw_kolor_oczu(self):
        self.oczy = input("Podaj kolor oczu: ")
        return self.oczy


# czlowiek3 = Osoba2() # TypeError: Osoba2.__init__() missing 1 required positional argument: 'imie'
czlowiek3 = Osoba2("Adam", 180)
czlowiek3.wypisz_wzrost()
czlowiek3.przedstaw_sie()
# Mam 180 cm wzrostu
# Nazywam się: Adam
print(czlowiek3.ustaw_kolor_oczu())
# Podaj kolor oczu: szare
# szare
