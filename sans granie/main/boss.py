import random
import pygame
from wybor import wybor_postaci
def victory():
    pygame.mixer.init()
    pygame.mixer.music.load('victory.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
wynik = 0
def mocny_przeciwnik1():
    global wynik
    your_hp = 100
    minion_hp = 300
    boss = 1
    runda = 1
    time_poison = 0
    time_fire = 0
    poison = 0
    magiczny_artefakt = 1
    leczniczymi_ziołami = 1
    while your_hp > 0 and minion_hp > 0:
        your_attack = int(random.randint(1,50))
        minion_attack = random.randint(1,50)
        double_attack = int(random.randint(1,4))
        double_attack_boss = int(random.randint(1,4))
        unik = int(random.randint(1,4))
        if postac == "1":
            poison = int(random.randint(1,4))
        if postac == "3":
            unik = int(random.randint(0,1))
        if postac == "2":
            minion_attack = round(minion_attack/2)
        print("Runda",runda)
        if runda % 2 == 0:
            minion_hp += 5
            your_hp -= 5
            print("Przeciwnik zabrał ci 5 hp i dał je sobie")
        if postac == "1":
            poison = int(random.randint(1,4))
        if postac == "3":
            unik = int(random.randint(0,1))
        if postac == "2":
            minion_attack = round(minion_attack/2)
        print("Twoje hp ", your_hp)
        print("Hp bossa",minion_hp)
        print("Twój atak", your_attack)
        print("Atak bossa", minion_attack)
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
            minion_attack = round(minion_attack * 8/10)
        if inp == "Atak":
            minion_hp -= your_attack
        if inp == "Atak" and double_attack == 4:
            minion_hp -= your_attack
            print("Zadałeś podwójne obrażenia")
        if boss == 1 and double_attack_boss != 4:
            your_hp -= minion_attack
        elif boss == 1 and double_attack_boss == 4:
            your_hp -= (minion_attack * 2)
            print("Boss zadał podwójne obrażenia")
        elif boss == 1 and double_attack_boss == 4 and unik == 1:
            print("Boss zadał podwójne obrażenia ale ich uniknąłeś")
            minion_attack = 0
        if time_poison != 0:
            minion_hp -= 5
            time_poison -= 1
        if inp == "Atak" and poison == 4 and time_poison == 0:
            print("Otrułeś przeciwnika")
            time_poison += 3
        if inp == "Atak Ognia":
            print("Podpaliłeś przeciwnika")
            time_fire += 3
        if time_fire != 0:
            minion_hp -= 5
            time_fire -= 5
        runda += 1
        print("")
    if your_hp <= 0 and minion_hp > 0:
        print("Twoje hp",your_hp)
        print("Hp Bossa",minion_hp)
        print("Przegrałeś")
        wynik += 1
    if minion_hp <= 0 and your_hp > 0:
        print("Twoje hp",your_hp)
        print("Hp Bossa",minion_hp)
        print("Wygrałeś")
        wynik += 2
        print("Gratulacje za przejście gry")
        victory()
    if minion_hp <= 0 and your_hp <= 0:
        print("Twoje hp",your_hp)
        print("Hp Bossa",minion_hp)
        print("Remis obaj umarliście")
        wynik += 3
def mocny_przeciwnik2():
    your_hp = 100
    minion_hp = 300
    boss = 1
    runda = 1
    time_poison = 0
    time_fire = 0
    poison = 0
    magiczny_artefakt = 1
    leczniczymi_ziołami = 0
    while your_hp > 0 and minion_hp > 0:
        global wynik
        your_attack = int(random.randint(1,50))
        minion_attack = random.randint(1,50)
        double_attack = int(random.randint(1,4))
        double_attack_boss = int(random.randint(1,4))
        unik = int(random.randint(1,4))
        print("Runda",runda)
        if runda % 2 == 0:
            minion_hp += 5
            your_hp -= 5
            print("Przeciwnik zabrał ci 5 hp i dał je sobie")
        if postac == "1":
            poison = int(random.randint(1,4))
        if postac == "3":
            unik = int(random.randint(0,1))
        if postac == "2":
            minion_attack = round(minion_attack/2)
        print("Twoje hp ", your_hp)
        print("Hp bossa",minion_hp)
        print("Twój atak", your_attack)
        print("Atak bossa", minion_attack)
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
            minion_attack = round(minion_attack * 8/10)
        if inp == "Atak":
            minion_hp -= your_attack
        if inp == "Atak" and double_attack == 4:
            minion_hp -= your_attack
            print("Zadałeś podwójne obrażenia")
        if boss == 1 and double_attack_boss != 4:
            your_hp -= minion_attack
        elif boss == 1 and double_attack_boss == 4:
            your_hp -= (minion_attack * 2)
            print("Boss zadał podwójne obrażenia")
        elif boss == 1 and double_attack_boss == 4 and unik == 1:
            print("Boss zadał podwójne obrażenia ale ich uniknąłeś")
            minion_attack = 0
        if time_poison != 0:
            minion_hp -= 5
            time_poison -= 1
        if inp == "Atak" and poison == 4 and time_poison == 0:
            print("Otrułeś przeciwnika")
            time_poison += 3
        if inp == "Atak Ognia":
            print("Podpaliłeś przeciwnika")
            time_fire += 3
        if time_fire != 0:
            minion_hp -= 5
            time_fire -= 5
        runda += 1
        print("")
    if your_hp <= 0 and minion_hp > 0:
        print("Twoje hp",your_hp)
        print("Hp Bossa",minion_hp)
        print("Przegrałeś")
        wynik += 1
    if minion_hp <= 0 and your_hp > 0:
        print("Twoje hp",your_hp)
        print("Hp Bossa",minion_hp)
        print("Wygrałeś")
        wynik += 2
        print("Gratulacje za przejście gry")
        victory()
    if minion_hp <= 0 and your_hp <= 0:
        print("Twoje hp",your_hp)
        print("Hp Bossa",minion_hp)
        print("Remis obaj umarliście")
        wynik += 3
def mocny_przeciwnik3():
    your_hp = 100
    minion_hp = 300
    boss = 1
    runda = 1
    time_poison = 0
    time_fire = 0
    poison = 0
    magiczny_artefakt = 0
    leczniczymi_ziołami = 1
    while your_hp > 0 and minion_hp > 0:
        global wynik
        your_attack = int(random.randint(1,50))
        minion_attack = random.randint(1,50)
        double_attack = int(random.randint(1,4))
        double_attack_boss = int(random.randint(1,4))
        unik = int(random.randint(1,4))
        print("Runda",runda)
        if runda % 2 == 0:
            minion_hp += 5
            your_hp -= 5
            print("Przeciwnik zabrał ci 5 hp i dał je sobie")
        if postac == "1":
            poison = int(random.randint(1,4))
        if postac == "3":
            unik = int(random.randint(0,1))
        if postac == "2":
            minion_attack = round(minion_attack/2)
        print("Twoje hp ", your_hp)
        print("Hp bossa",minion_hp)
        print("Twój atak", your_attack)
        print("Atak bossa", minion_attack)
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
            minion_attack = round(minion_attack * 8/10)
        if inp == "Atak":
            minion_hp -= your_attack
        if inp == "Atak" and double_attack == 4:
            minion_hp -= your_attack
            print("Zadałeś podwójne obrażenia")
        if boss == 1 and double_attack_boss != 4:
            your_hp -= minion_attack
        elif boss == 1 and double_attack_boss == 4:
            your_hp -= (minion_attack * 2)
            print("Boss zadał podwójne obrażenia")
        elif boss == 1 and double_attack_boss == 4 and unik == 1:
            print("Boss zadał podwójne obrażenia ale ich uniknąłeś")
            minion_attack = 0
        if time_poison != 0:
            minion_hp -= 5
            time_poison -= 1
        if inp == "Atak" and poison == 4 and time_poison == 0:
            print("Otrułeś przeciwnika")
            time_poison += 3
        if inp == "Atak Ognia":
            print("Podpaliłeś przeciwnika")
            time_fire += 3
        if time_fire != 0:
            minion_hp -= 5
            time_fire -= 5
        runda += 1
        print("")
    if your_hp <= 0 and minion_hp > 0:
        print("Twoje hp",your_hp)
        print("Hp Bossa",minion_hp)
        print("Przegrałeś")
        wynik += 1
    if minion_hp <= 0 and your_hp > 0:
        print("Twoje hp",your_hp)
        print("Hp Bossa",minion_hp)
        print("Wygrałeś")
        wynik += 2
        print("Gratulacje za przejście gry")
        victory()
    if minion_hp <= 0 and your_hp <= 0:
        print("Twoje hp",your_hp)
        print("Hp Bossa",minion_hp)
        print("Remis obaj umarliście")
        wynik += 3
def mocny_przeciwnik4():
    global wynik
    your_hp = 100
    minion_hp = 300
    boss = 1
    runda = 1
    time_poison = 0
    time_fire = 0
    poison = 0
    magiczny_artefakt = 0
    leczniczymi_ziołami = 0
    while your_hp > 0 and minion_hp > 0:
        your_attack = int(random.randint(1,50))
        minion_attack = random.randint(1,50)
        double_attack = int(random.randint(1,4))
        double_attack_boss = int(random.randint(1,4))
        unik = int(random.randint(1,4))
        print("Runda",runda)
        if runda % 2 == 0:
            minion_hp += 5
            your_hp -= 5
            print("Przeciwnik zabrał ci 5 hp i dał je sobie")
        if postac == "1":
            poison = int(random.randint(1,4))
        if postac == "3":
            unik = int(random.randint(0,1))
        if postac == "2":
            minion_attack = round(minion_attack/2)
        print("Twoje hp ", your_hp)
        print("Hp bossa",minion_hp)
        print("Twój atak", your_attack)
        print("Atak bossa", minion_attack)
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
            minion_attack = round(minion_attack * 8/10)
        if inp == "Atak":
            minion_hp -= your_attack
        if inp == "Atak" and double_attack == 4:
            minion_hp -= your_attack
            print("Zadałeś podwójne obrażenia")
        if boss == 1 and double_attack_boss != 4:
            your_hp -= minion_attack
        elif boss == 1 and double_attack_boss == 4:
            your_hp -= (minion_attack * 2)
            print("Boss zadał podwójne obrażenia")
        elif boss == 1 and double_attack_boss == 4 and unik == 1:
            print("Boss zadał podwójne obrażenia ale ich uniknąłeś")
            minion_attack = 0
        if time_poison != 0:
            minion_hp -= 5
            time_poison -= 1
        if inp == "Atak" and poison == 4 and time_poison == 0:
            print("Otrułeś przeciwnika")
            time_poison += 3
        if inp == "Atak Ognia":
            print("Podpaliłeś przeciwnika")
            time_fire += 3
        if time_fire != 0:
            minion_hp -= 5
            time_fire -= 5
        runda += 1
        print("")
    if your_hp <= 0 and minion_hp > 0:
        print("Twoje hp",your_hp)
        print("Hp Bossa",minion_hp)
        print("Przegrałeś")
        wynik += 1
    if minion_hp <= 0 and your_hp > 0:
        print("Twoje hp",your_hp)
        print("Hp Bossa",minion_hp)
        print("Wygrałeś")
        wynik += 2
        print("Gratulacje za przejście gry")
        victory()
    if minion_hp <= 0 and your_hp <= 0:
        print("Twoje hp",your_hp)
        print("Hp Bossa",minion_hp)
        print("Remis obaj umarliście")
        wynik += 3
postac = wybor_postaci
