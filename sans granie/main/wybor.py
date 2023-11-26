import pygame
pygame.init()
def sans_granie():
    pygame.mixer.init()
    pygame.mixer.music.load('sans.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
def wybor_postaci():
    global postac
    print("Wybierz postać")
    print("Wpisz numer (Pamiętaj nie możesz wybrać innej postaci niż te pokazane na ekranie)")
    print("1. Barbarzyńca (otruwa przeciwników zadając 5 hp)")
    print("2. Tank (dostaje 50% mniejsze obrażenia)")
    print("3. Ninja (ma zwiększony unik)")
    
    while True:
        inp = input("Twój wybór: ")
        if inp in ["1", "2", "3"]:
            postac = inp
            return inp
        if inp == "sans granie":
            sans_granie()
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
