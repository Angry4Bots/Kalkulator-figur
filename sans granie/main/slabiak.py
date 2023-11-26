import random
from wybor import wybor_postaci
###########################################
def słaby_przeciwnik():
    your_hp = 100
    minion_hp = 50
    minions = random.randint(1,5)
    minion_hp = minion_hp * minions
    time_poison = 0
    poison = 0
    time_fire = 0
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
        print("Hp słabiaków",minion_hp)
        print("Ilość słabiaków",minions)
        print("Twój atak", your_attack)
        print("Atak słabiaków", minion_attack)
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
        if inp == "Leczenie" and leczniczymi_ziołami != 1:
            your_hp += 20
        if inp == "Leczenie" and leczniczymi_ziołami == 1:
            your_hp += 40
        if inp == "Ochrona":
            minion_attack = 8/10 * minion_attack
        if inp == "Atak":
            minion_hp -= your_attack
        if inp == "Atak" and double_attack == 4:
            minion_hp -= your_attack
            print("Zadałeś podwójne obrażenia")
        if minions == 1:
            your_hp -= minion_attack
        elif minions == 2:
            your_hp -= (minion_attack * 2)
        elif minions == 3:
            your_hp -= (minion_attack * 3)
        elif minions == 4:
            your_hp -= (minion_attack * 4)
        elif minions == 5:
            your_hp -= (minion_attack * 5)
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
