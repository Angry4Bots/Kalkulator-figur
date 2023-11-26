import random
from wybor import wybor_postaci

def Bandzior1():
    your_hp = 100
    minion_hp = 100
    opponent = random.randint(1,3)
    minion_hp = minion_hp * opponent
    time_poison = 0
    poison = 0
    time_fire = 0
    magiczny_artefakt = 1
    while your_hp > 0 and minion_hp > 0:
        your_attack = int(random.randint(1,50))
        minion_attack = int(random.randint(1,20))
        double_attack = int(random.randint(1,4))
        unik = random.randint(1,4)
        poison = 0
        if postac == "1":
            poison = int(random.randint(1,4))
        if postac == "3":
            unik = int(random.randint(0,1))
        if postac == "2":
            minion_attack = round(minion_attack/2)
        print("")
        print("Twoje hp ", your_hp)
        print("Hp bandziorów",minion_hp)
        print("Ilość bandziorów",opponent)
        print("Twój atak", your_attack)
        print("Atak bandziorów", minion_attack)
        print("Podaj jaki typ ataku chcesz użyć:")
        print("Leczenie")
        print("Ochrona")
        print("Atak")
        if magiczny_artefakt == 1:
            print("Atak Ognia")
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
        if opponent == 1:
            your_hp -= minion_attack
        elif opponent == 2:
            your_hp -= (minion_attack * 2)
        elif opponent == 3:
            your_hp -= (minion_attack * 3)
        if time_poison != 0:
            minion_hp -= 5
            time_poison -= 1
        if inp == "Atak" and poison == 4 and time_poison == 0:
            print("Otrułeś przeciwnika")
            time_poison += 3
        if inp == "Atak Ognia":
            print("Podpaliłeś przeciwnika")
            time_fire += 3
        if your_hp <= 0:
            print("Twoje hp",your_hp)
            print("Hp golema",minion_hp)
            print("Przegrałeś")
            break
        if minion_hp <= 0:
            print("Twoje hp",your_hp)
            print("Hp golema",minion_hp)
            print("Wygrałeś")
        if minion_hp <= 0 and your_hp <= 0:
            print("Twoje hp",your_hp)
            print("Hp golema",minion_hp)
            print("Remis obaj umarliście")
def bandzior2():
    your_hp = 100
    minion_hp = 100
    opponent = random.randint(1,3)
    minion_attack = random.randint(1,30)
    minions = random.randint(1,4)
    minion_hp = minion_hp * opponent
    time_poison = 0
    poison = 0
    time_fire = 0
    magiczny_artefakt = 0
    while your_hp > 0 or minion_hp > 0:
        your_attack = int(random.randint(1,50))
        minion_attack = int(random.randint(1,20))
        double_attack = int(random.randint(1,4))
        unik = random.randint(1,4)
        poison = 0
        if postac == "1":
            poison = int(random.randint(1,4))
        if postac == "3":
            unik = int(random.randint(0,1))
        if postac == "2":
            minion_attack = round(minion_attack/2)
        print("")
        print("Twoje hp ", your_hp)
        print("Hp bandziorów",minion_hp)
        print("Ilość bandziorów",opponent)
        print("Twój atak", your_attack)
        print("Atak bandziorów", minion_attack)
        print("Podaj jaki typ ataku chcesz użyć:")
        print("Leczenie")
        print("Ochrona")
        print("Atak")
        if magiczny_artefakt == 1:
            print("Atak Ognia")
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
        if opponent == 1:
            your_hp -= minion_attack
        elif opponent == 2:
            your_hp -= (minion_attack * 2)
        elif opponent == 3:
            your_hp -= (minion_attack * 3)
        if time_poison != 0:
            minion_hp -= 5
            time_poison -= 1
        if inp == "Atak" and poison == 4 and time_poison == 0:
            print("Otrułeś przeciwnika")
            time_poison += 3
        if inp == "Atak Ognia":
            print("Podpaliłeś przeciwnika")
            time_fire += 3
        if your_hp <= 0:
            print("Twoje hp",your_hp)
            print("Hp słabiaków",minion_hp)
            print("Przegrałeś")
            break
        if minion_hp <= 0:
            print("Twoje hp",your_hp)
            print("Hp słabiaków",minion_hp)
            print("Wygrałeś")
        if minion_hp <= 0 and your_hp <= 0:
            print("Twoje hp",your_hp)
            print("Hp Bossa",minion_hp)
            print("Remis obaj umarliście")
postac = wybor_postaci