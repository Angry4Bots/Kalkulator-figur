class Matematyka:
    def __init__(self, imie, nazwisko, przedmiot, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot 
        self.klasa = klasa
Pani_od_Matmy = Matematyka("Joanna", "Paciorek", "Matematyka", "1a")
print(Pani_od_Matmy.imie, Pani_od_Matmy.nazwisko, Pani_od_Matmy.przedmiot, Pani_od_Matmy.klasa)