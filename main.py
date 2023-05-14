# biblioteki
import pandas as pd
import matplotlib.pyplot as plt

# klasa
class SprzedażSamochodów:
    # inicjalizacja
    def __init__(self, nazwa_pliku):
        self.nazwa_pliku = ('dane2.csv')
        self.data = None

    # wczytywanie danych
    def wczytaj_dane(self):
        try:
            self.data = pd.read_csv(self.nazwa_pliku)
            print("Pomyślnie wczytano plik.")
        except FileNotFoundError:
            print("Nie znaleziono pliku.")
        except pd.errors.EmptyDataError:
            print("Plik jest pusty.")
        except pd.errors.ParserError:
            print("Nieprawidłowy format pliku.")

    # FUNKCJA sumowanie danych
    def sumowanie(self, wybrane_wojewodztwa):
        try:
            suma_aut = []
            for wojewodztwo in wybrane_wojewodztwa:
                dane_wojewodztwo = self.data[self.data['Wojewodztwo'] == wojewodztwo]
                suma = dane_wojewodztwo['Ilosc sprzedanych aut'].sum()
                suma_aut.append(suma)
            return suma_aut
        except KeyError:
            print("Nieprawidłowa nazwa kolumny w danych.")


    # FUNKCJA generowanie wykresu dla pojedynczego wojewodztwa
    def generuj_wykres_dla_wojewodztwa(self, wojewodztwo, suma_aut):
        try:
            plt.bar(wojewodztwo, suma_aut)
            plt.xlabel('Województwo')
            plt.ylabel('Suma sprzedanych aut')
            plt.title(f'Suma sprzedanych aut dla województwa: {wojewodztwo}')
            self.pokaz_liczby_nad_slupkami(suma_aut)
            plt.show()
        except ValueError:
            print("Nieprawidłowe dane do wygenerowania wykresu.")

    # FUNKCJA generowanie wykresu dla wszystkich wojewodztw
    def generuj_wykres_dla_wszystkich(self, wybrane_wojewodztwa, suma_aut):
        try:
            plt.bar(wybrane_wojewodztwa, suma_aut)
            plt.xlabel('Województwo')
            plt.ylabel('Suma sprzedanych aut')
            plt.title('Suma sprzedanych aut dla wszystkich województw')
            self.pokaz_liczby_nad_slupkami(suma_aut)
            plt.show()
        except ValueError:
            print("Nieprawidłowe dane do wygenerowania wykresu.")

    # pokazywanie liczb nad slupkami
    def pokaz_liczby_nad_slupkami(self, suma_aut):
        for i, suma in enumerate(suma_aut):
            plt.text(i, suma, str(suma), ha='center', va='bottom')

    # zapisywanie wynikow dla 3 i 4
    def zapisz_wyniki(self, nazwa_pliku, wybrane_wojewodztwa, suma_aut):
        df = pd.DataFrame({'Wojewodztwo': wybrane_wojewodztwa, 'Suma_sprzedanych_aut': suma_aut})
        df.to_csv(nazwa_pliku, index=False)
        print(f"Wyniki dla województwa {wybrane_wojewodztwa} zostały zapisane w pliku: {nazwa_pliku}")


#################################################################

# MENU
def menu(sprzedaz):

    while True:
        print("Witaj użytkowniku! - WOJEWÓDZKI SPIS POJAZDÓW")
        print("=============================================")
        print("1. Generuj dane dla danego województwa")
        print("2. Generuj dane dla wszystkich województw")
        print("3. Zsumuj dane dla danego województwa")
        print("4. Zsumuj dane dla wszystkich województw")
        print("5. Wyjście")
        print("=============================================")
        wybor = input("Wybierz opcję: ")
        try:
            if wybor == "1":
                print("WYBIERZ WOJEWÓDZTWO")
                print("dolnośląskie")
                print("kujawsko-pomorskie")
                print("lubelskie")
                print("lubuskie")
                print("łódzkie")
                print("małopolskie")
                print("mazowieckie")
                print("opolskie")
                print("podkarpackie")
                print("podlaskie")
                print("pomorskie")
                print("śląskie")
                print("świętokrzyskie")
                print("warmińsko-mazurskie")
                print("wielkopolskie")
                print("zachodniopomorskie")
                wybrane_wojewodztwo = input("Wybierz województwo: ")
                suma_aut = sprzedaz.sumowanie([wybrane_wojewodztwo])
                sprzedaz.generuj_wykres_dla_wojewodztwa(wybrane_wojewodztwo, suma_aut)


            elif wybor == "2":
                suma_aut = sprzedaz.sumowanie(wybrane_wojewodztwa)
                sprzedaz.generuj_wykres_dla_wszystkich(wybrane_wojewodztwa, suma_aut)


            elif wybor == "3":
                 wybrane_wojewodztwo = input("Podaj nazwę województwa: ")
                 suma_aut = sprzedaz.sumowanie([wybrane_wojewodztwo])  # Przekazuje województwo jako listę
                 print(f"Suma sprzedanych aut dla województwa {wybrane_wojewodztwo}: {suma_aut[0]}")
                 wybor3 = input("Chcesz zapisać? T/N: ")
                 if wybor3 == "T":
                     nazwa_pliku = input("Podaj nazwę pliku do zapisu: ")
                     sprzedaz.zapisz_wyniki(nazwa_pliku, [wybrane_wojewodztwo], [suma_aut[0]])
                 elif  wybor3 == "N":
                     print(" ")
                 else:
                     print("Nieprawidłowy wybór. Wybierz ponownie.")



            elif wybor == "4":
                suma_aut = sprzedaz.sumowanie(wybrane_wojewodztwa)
                suma_calosciowa = sum(suma_aut)
                print(f"Suma sprzedanych aut dla wszystkich województw: {suma_calosciowa}")
                wybor4 = input("Chcesz zapisać? T/N: ")
                if wybor4 == "T":
                    nazwa_pliku = input("Podaj nazwę pliku do zapisu: ")
                    sprzedaz.zapisz_wyniki(nazwa_pliku, wybrane_wojewodztwa, suma_aut)
                elif wybor4 == "N":
                    print(" ")
                else:
                    print("Nieprawidłowy wybór. Wybierz ponownie.")


            elif wybor == "5":
                print("Wyjście z programu.")
                break

            else:
                print("Nieprawidłowy wybór. Wybierz ponownie.")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")


# ODWOŁANIA
nazwa_pliku = 'dane2.csv'
wybrane_wojewodztwa = ['dolnośląskie', 'kujawsko-pomorskie', 'lubelskie', 'lubuskie', 'łódzkie', 'małopolskie',
                           'mazowieckie', 'opolskie', 'podkarpackie', 'podlaskie', 'pomorskie', 'śląskie',
                           'świętokrzyskie','warmińsko-mazurskie', 'wielkopolskie', 'zachodniopomorskie']

sprzedaz = SprzedażSamochodów(nazwa_pliku)
sprzedaz.wczytaj_dane()

menu(sprzedaz)

