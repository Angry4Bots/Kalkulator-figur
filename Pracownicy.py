from time import sleep
class Pracownicy:
    pracownicy = 0
    def __init__(self, imie, wiek, zarobki, lata_pracy):
        self.imie = imie
        self.wiek = wiek
        self.zarobki = zarobki
        self.lata_pracy = lata_pracy
        Pracownicy.pracownicy += 1


    def przedstaw_sie(self):
        return f"Jestem {self.imie}, mam {self.wiek} lat. Zarabiam {self.zarobki} i pracuje {self.lata_pracy}.\n"
   
class Sprzedawca(Pracownicy):
    def __init__(self, imie, wiek, kasa, zarobki, lata_pracy):
        super().__init__(imie, wiek, zarobki, lata_pracy)
        self.kasa = kasa

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f"Pracuje na kasie {self.kasa}."
   


class Zatrudniający(Pracownicy):
    def __init__(self, imie, wiek, zarobki, lata_pracy, ilosc_osob_ktore_zatrudnil):
        super().__init__(imie, wiek, zarobki, lata_pracy)
        self.ilosc_osob_ktore_zatrudnil = ilosc_osob_ktore_zatrudnil


    def przedstaw_sie(self):
        return super().przedstaw_sie() + f"Zatrudniłem {self.ilosc_osob_ktore_zatrudnil}."
    
    def zatrudnianie(self):
        print("napisz swoje cv")
        print("wybierz swoją zalete")
        print("Co wybierzesz?\n1.Umiem dogadać się z osobami\n2.Jestem dobrym sprzedawcą\n3.Często nie choruje")
        sum = 0
        odpowiedzi = ["1","2","3","sans granie"]
        while True:
            zalety = input()
            if zalety == "1":
                sum += 1
            elif zalety == "2":
                sum += 2
            elif zalety == "3":
                sum += 3
            elif zalety == "sans granie":
                sum += 4
                print("he he sans granie")
            if not zalety in odpowiedzi:
                print("Nie możesz tak")
            if zalety in odpowiedzi:
                break
        print("wybierz swoje wady")
        print("Co wybierzesz?\n1.Często się spóźniam\n2.Często puszczają mi nerwy\n3.Mam fobie społeczną")
        while True:
            wady = input()
            wady = wady
            if wady == "1":
                sum += 1
            elif wady == "2":
                sum += 2
            elif wady == "3":
                sum += 3
            elif wady == "sans granie":
                sum += 4
                print("ej co ty robisz")
            if not wady in odpowiedzi:
                print("Nie możesz tak")
            if wady in odpowiedzi:
                break
        print('wybierz swoje doświadczenie')
        print("Co wybierzesz?\n1.Zdałem mature\n2.Skończyłem studia informatyczne\n3.Napisałem Egzamin Ósmoklasity")
        # exp to doświadczenie tak jakby co bo wiecie exp w grach to doświadczenie
        while True:
            exp = input()
            if not exp in odpowiedzi:
                print("Nie możesz tego wybrać")
            if exp in odpowiedzi:
                # ta odpowiedz na nic nie wpływa to taka podpucha po co masz coś umieć do sklepu z anime jakby imagine lol🤣🤣🤣
                break
        if sum > 6:
            print("JAK TY TU DOTARŁEŚ, masz bana")
            print("SECRET ENDING")
            exit()
        print("Widziałem twoje cv\n")
        if sum < 4:
            print("Pasujesz do nas od jutra pracujesz *uściśnięcie ręki*")
            return "GOOD ENDING"
        if wady and zalety == "3":
            print("Nie nadajesz się do tej pracy, do widzenia")
            return "BAD ENDING"
    
class Dostawca(Pracownicy):
    def __init__(self, imie, wiek, auto_dostawcze, zarobki, lata_pracy):
        super().__init__(imie, wiek, zarobki, lata_pracy)
        self.auto_dostawcze = auto_dostawcze

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f"Jeżdżę {self.auto_dostawcze}."

class Figurek(Sprzedawca):
    def __init__(self, imie, wiek, kasa, zarobki, lata_pracy):
        super().__init__(imie, wiek, zarobki, lata_pracy, kasa)

    def przedstaw_sie(self):
        print(super().przedstaw_sie() + " Sprzedaje figurki z serii.\nDragon Ball")
        sleep(1)
        print("Hunter x Hunter")
        sleep(1)
        print("Dr.Stone")
        sleep(1)
        print("Nie drocz się ze mną, Nagatoro!")
        sleep(1)
        return("Szczególnie Polecam figurke Mistrzunia z produkcji, którą wymieniłem podkoniec")
class Koszulek(Sprzedawca):
    def __init__(self, imie, wiek, kasa, zarobki, lata_pracy):
        super().__init__(imie, wiek, zarobki, lata_pracy, kasa)

    def przedstaw_sie(self):
        print(super().przedstaw_sie() + " Sprzedaje koszulki z twoimi ULUBIONYMI SERIAMI takimi jak.\nDragon Ball, Hunter x Hunter, Dr.Stone, Nie drocz się ze mną, Nagatoro!")
class Mangi(Sprzedawca):
    def __init__(self, imie, wiek, kasa, zarobki, lata_pracy):
        super().__init__(imie, wiek, zarobki, lata_pracy, kasa)

    def przedstaw_sie(self):
        print(super().przedstaw_sie() + " Sprzedaje mangi, które nie są hentaiami, nie ma tam nagości nic wiecej nie obiecuje ze nie bedzie tam półnagości.\nDragon Ball, Hunter x Hunter, Dr.Stone, Nie drocz się ze mną, Nagatoro!")
class Poduszki(Sprzedawca):
    def __init__(self, imie, wiek, kasa, zarobki, lata_pracy):
        super().__init__(imie, wiek, zarobki, lata_pracy, kasa)

    def przedstaw_sie(self):
        print(super().przedstaw_sie() + " Sprzedaje poduszki z twoimi waifu")
    

u = Figurek(10, 10 , 10, 10, 10)
print(u.przedstaw_sie())