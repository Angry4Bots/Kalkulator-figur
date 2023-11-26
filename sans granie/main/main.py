import time
import sys
import pygame
import random
from wybor import wybor_postaci
from średni_przeciwnik import średni_przeciwnik1
from średni_przeciwnik import średni_przeciwnik2
from bandzior import Bandzior1
from bandzior import bandzior2
from boss import mocny_przeciwnik1
from boss import mocny_przeciwnik2
from boss import mocny_przeciwnik3
from boss import mocny_przeciwnik4
import skrzynie
while True:
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Powolne Wyświetlanie Napisu")

    font = pygame.font.Font(None, 36)
    opoznienie = 0.1

    def ez(napis, opoznienie=0.1):
        pygame.init()

        for znak in napis:
            sys.stdout.write(znak)
            sys.stdout.flush()
            time.sleep(opoznienie)
    magiczny_artefakt = 0
    leczniczymi_ziołami = 0
    postac = wybor_postaci()
    ez("Przeszedłeś przez magiczny portal byłeś zdezorientowany"),print("")
    ez("zobaczyłeś dwie ścieżki musisz zdecydować, którą iść."),print("")
    ez("Lewo czy Prawo"),print("")
    ez("")
    inp = input()
    if inp == "Lewo":
        skrzynie.skrzynia1()
        ez("Odnalazłeś tajemniczy artefakt podobno osoba, która go posiądzie zdobywa moc ognia"),print("")
        ez("Akurat jest tu manekin przetestuj")
        from manekin import manekin
        manekin()
        ez("Dotarłeś do krainy strachu zauważyłeś że prawa ścieżka prowadziła do tego samego miejsca "),print("")
        ez("Zauważasz kolejne rozwidlenie drug"),print("")
        ez("Lewo czy Prawo"),print("")
        inp = input()
        if inp == "Lewo":
            ez("Napotkałeś na bandziorów")
            Bandzior1()
            ez("Po zakończeniu walki widzisz dalszą ścieżke, ale nic więcej")
            ez("Wychodząc z krainy strachu widzisz Królestwo Zagubionych Przeznaczeń dochodząc do muru zauważasz dziure w płocie więc przez nią wchodzisz"),print("")
            ez("Wchodzisz do zamku i napotykasz Króla jest nim wampir, więc stajesz z nim w szranki"),print("")
            wynik = 0
            mocny_przeciwnik2()
            if wynik == 2:
                ez("Możesz zabić Króla lub zostawić go przy życiu")
                ez("Zabij czy Zostaw przy życiu")
                inp = input()
                if inp == "Zabij":
                    ez("Zostajesz uznany za morderce i nikt nie chce cię widzieć nawet ludzie w wiosce")
                if inp == "Zostaw przy życiu":
                    ez("Król oddaje ci władzę nad królestwem, uważa że nie obronił by swojego kraju")
            break
        if inp == "Prawo":
            ez("Napotkałeś na Golemy"),print("")
            magiczny_artefakt = skrzynie.skrzynia1
            średni_przeciwnik1()
            ez("Po zakończeniu walki widzisz skrzynie"),print("")
            ez("Otwierasz ją i znajdujesz lecznicze zioła przypominasz sobie że jeśli dobrze je rozdzielisz będziesz mógł się leczyć więcej niż 20hp"),print("")
            skrzynie.skrzynia2()
            ez("Wychodząc z krainy strachu widzisz Królestwo Zagubionych Przeznaczeń dochodząc do bramy pokazujesz dokument, który znalazłeś idąc tu"),print("")
            ez("Wchodzisz do zamku i napotykasz Króla jest nim wampir, więc stajesz z nim w szranki"),print("")
            wynik = 0
            mocny_przeciwnik1()
            if wynik == 2:
                ez("Możesz zabić Króla lub zostawić go przy życiu")
                ez("Zabij czy Zostaw przy życiu")
                inp = input()
                if inp == "Zabij":
                    ez("Zostajesz uznany za morderce i nikt nie chce cię widzieć nawet ludzie w wiosce")
                if inp == "Zostaw przy życiu":
                    ez("Król oddaje ci władzę nad królestwem, uważa że nie obronił by swojego kraju")
            break
    elif inp == "Prawo":
        ez("Jest tu manekin może przetestujemy na nim twoje umiejętnośći")
        from manekin import manekin_dla_osoby_bez_artefaktu
        manekin_dla_osoby_bez_artefaktu()
        ez("Dotarłeś do krainy strachu zauważyłeś że prawa ścieżka prowadziła do tego samego miejsca "),print("")
        ez("Zauważasz kolejne rozwidlenie drug"),print("")
        ez("Lewo czy Prawo"),print("")
        if inp == "Lewo":
            ez("Napotkałeś na bandziorów")
            bandzior2()
            ez("Po zakończeniu walki widzisz dalszą ścieżke, ale nic więcej")
            ez("Wychodząc z krainy strachu widzisz Królestwo Zagubionych Przeznaczeń dochodząc do muru zauważasz dziure w płocie więc przez nią wchodzisz"),print("")
            ez("Wchodzisz do zamku i napotykasz Króla jest nim wampir, więc stajesz z nim w szranki"),print("")
            wynik = 0
            mocny_przeciwnik4()
            if wynik == 2:
                ez("Możesz zabić Króla lub zostawić go przy życiu")
                ez("Zabij czy Zostaw przy życiu")
                inp = input()
                if inp == "Zabij":
                    ez("Zostajesz uznany za morderce i nikt nie chce cię widzieć nawet ludzie w wiosce")
                if inp == "Zostaw przy życiu":
                    ez("Król oddaje ci władzę nad królestwem, uważa że nie obronił by swojego kraju")
            break
        if inp == "Prawo":
            ez("Napotkałeś na Golemy"),print("")
            magiczny_artefakt = skrzynie.skrzynia1
            średni_przeciwnik1()
            ez("Po zakończeniu walki widzisz skrzynie"),print("")
            ez("Otwierasz ją i znajdujesz lecznicze zioła przypominasz sobie że jeśli dobrze je rozdzielisz będziesz mógł się leczyć więcej niż 20hp"),print("")
            skrzynie.skrzynia2()
            ez("Wychodząc z krainy strachu widzisz Królestwo Zagubionych Przeznaczeń dochodząc do bramy pokazuje dokument, który znalazłem idąc tu"),print("")
            ez("Wchodzisz do zamku i napotykasz Króla jest nim wampir, więc stajesz z nim w szranki"),print("")
            wynik = 0
            mocny_przeciwnik3()
            if wynik == 2:
                ez("Możesz zabić Króla lub zostawić go przy życiu")
                ez("Zabij czy Zostaw przy życiu")
                inp = input()
                if inp == "Zabij":
                    ez("Zostajesz uznany za morderce i nikt nie chce cię widzieć nawet ludzie w wiosce")
                if inp == "Zostaw przy życiu":
                    ez("Król oddaje ci władzę nad królestwem, uważa że nie obronił by swojego kraju")
            break