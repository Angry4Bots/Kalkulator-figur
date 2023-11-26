import random
from wybor import wybor_postaci
###########################################
def manekin():
    your_hp = 100
    minion_hp = 100
    minions = 1
    minion_hp = minion_hp * minions
    time_poison = 0
    time_fire = 0
    while your_hp > 0 or minion_hp > 0:
        your_attack = int(random.randint(1,50))
        minion_attack = 0
        double_attack = int(random.randint(1,4))
        unik = random.randint(1,4)
        poison = 0
        Runda = 1
        if postac == "1":
            poison = int(random.randint(1,4))
        if postac == "3":
            unik = int(random.randint(0,1))
        if postac == "2":
            minion_attack = round(minion_attack/2)
        print("")
        print("Napisz Koniec, jeśli chcesz skończyć")
        print("Runda",Runda)
        print("Twoje hp ", your_hp)
        print("Hp słabiaków",minion_hp)
        print("Ilość słabiaków",minions)
        print("Twój atak", your_attack)
        print("Atak słabiaków", minion_attack)
        print("Podaj jaki typ ataku chcesz użyć:")
        print("Leczenie","(Leczysz się o 20hp)")
        print("Ochrona","(Otrzymujesz o 20% słabsze obrażenia)")
        print("Atak","(Zadajesz od 1 do 50hp)")
        print("Atak Ognia","(Podpalasz przeciwnika zadając mu 5hp na 3 rundy)")
        inp = input()
        if unik == 1 and postac != "3":
            print("Uniknąłeś ataku")
            minion_attack = 0
        if unik == 1 and postac == "3":
            print("Rzuciłeś smołka")
            minion_attack = 0
        if inp == "Leczenie":
            your_hp += 20
        if inp == "Ochrona":
            minion_attack = 8/10 * minion_attack
        if inp == "Atak":
            minion_hp -= your_attack
        if inp == "Atak" and double_attack == 4:
            minion_hp -= your_attack
            print("Zadałeś podwójne obrażenia")
        if inp == "Atak Ognia":
            print("Podpaliłeś przeciwnika")
            time_fire += 3
        if time_fire != 0:
            minion_hp -= 5
            time_fire -= 5
        if minions == 1:
            your_hp -= minion_attack
        elif minions == 2:
            your_hp -= (minion_attack * 2)
        elif minions == 3:
            your_hp -= (minion_attack * 3)
        elif minions == 4:
            your_hp -= (minion_attack * 4)
        else:
            your_hp -= (minion_attack * 5)
        if time_poison != 0:
            minion_hp -= 5
            time_poison -= 1
        if inp == "Atak" and poison == 4 and time_poison == 0:
            print("Otrułeś przeciwnika")
            time_poison += 3
        if inp == "Koniec":
            your_hp = -999999999999999999999
            break
        Runda += 1
def manekin_dla_osoby_bez_artefaktu():
    your_hp = 100
    minion_hp = 100
    minions = 1
    minion_hp = minion_hp * minions
    time_poison = 0
    time_fire = 0
    Runda = 1
    while your_hp > 0 or minion_hp > 0:
        your_attack = int(random.randint(1,50))
        minion_attack = 0
        double_attack = int(random.randint(1,4))
        unik = random.randint(1,4)
        poison = 0
        if Runda % 2 == 0:
            minion_hp = 100
        if postac == "1":
            poison = int(random.randint(1,4))
        if postac == "3":
            unik = int(random.randint(0,1))
        if postac == "2":
            minion_attack = round(minion_attack/2)
        print("")
        print("Napisz Koniec, jeśli chcesz skończyć")
        print("Runda",Runda)
        print("Twoje hp ", your_hp)
        print("Hp słabiaków",minion_hp)
        print("Ilość słabiaków",minions)
        print("Twój atak", your_attack)
        print("Atak słabiaków", minion_attack)
        print("Podaj jaki typ ataku chcesz użyć:")
        print("Leczenie","(Leczysz się o 20hp)")
        print("Ochrona","(Otrzymujesz o 20% słabsze obrażenia)")
        print("Atak","(Zadajesz od 1 do 50hp)")
        inp = input()
        if unik == 1 and postac != "3":
            print("Uniknąłeś ataku")
            minion_attack = 0
        if unik == 1 and postac == "3":
            print("Rzuciłeś smołka")
            minion_attack = 0
        if inp == "Leczenie":
            your_hp += 20
        if inp == "Ochrona":
            minion_attack = 8/10 * minion_attack
        if inp == "Atak":
            minion_hp -= your_attack
        if inp == "Atak" and double_attack == 4:
            minion_hp -= your_attack
            print("Zadałeś podwójne obrażenia")
            time_fire += 3
        if time_fire != 0:
            minion_hp -= 5
            time_fire -= 5
        if minions == 1:
            your_hp -= minion_attack
        elif minions == 2:
            your_hp -= (minion_attack * 2)
        elif minions == 3:
            your_hp -= (minion_attack * 3)
        elif minions == 4:
            your_hp -= (minion_attack * 4)
        else:
            your_hp -= (minion_attack * 5)
        if time_poison != 0:
            minion_hp -= 5
            time_poison -= 1
        if inp == "Atak" and poison == 4 and time_poison == 0:
            print("Otrułeś przeciwnika")
            time_poison += 3
        if inp == "Koniec":
            your_hp = -999999999999999999999
            break
        Runda += 1

postac = wybor_postaci