class zwierzeta:
    nazwa = None
    mieso = None
    rasa = None
    przedmiot = None
    klasa = None    
    def __init__(self,nazwa,mieso,rasa,przedmiot,klasa):
        self.nazwa = nazwa
        self.mieso = mieso
        self.rasa = rasa 
        self.przedmiot = przedmiot
        self.klasa = klasa
Pani_od_Matmy = zwierzeta(input(),"ludzkie","Człowiek","Matematyka","1a")
Świnia = zwierzeta("Świnia","Wieprzowina","Świnia", "Świnia","Zwierzęta")
print(Pani_od_Matmy.nazwa, Pani_od_Matmy.mieso, Pani_od_Matmy.rasa, Pani_od_Matmy.przedmiot, Pani_od_Matmy.klasa)