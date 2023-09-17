import math
print("A - Pole Kwadratu")
print("B - Pole Koła")
print("C - Pole Trapezu")
print("D - Pole Trójkąta")
print("E - Obwód Kwadratu")
print("F - Obwód Koła")
print("G - Obwód Trapezu")
print("H - Obwód Trójkąta")
print("I - Pole Powierzchni Sześcianu")
print("J - Pole Powierzchni Kuli")
print("K - Pole Powierzchni Graniastosłupa")
print("L - Pole Powierzchni Ostrosłupa")
print("M - Objętość Sześcianu")
print("N - Objętość Kuli")
print("O - Objętość Graniastosłupa")
print("P - Objętość Ostrosłupa")


co_mam_zrobic = input("co mam zrobić? ")

if co_mam_zrobic == "A":
    print("Podaj a")
    a = float(input("a = "))
    print("Pole kwadratu wynosi:")
    print(a*a)
if co_mam_zrobic == "B":
    print("Podaj r")
    r = float(input("r = "))
    print("Pole koła wynosi:")
    print((r*math.pi)**2)
if co_mam_zrobic == "C":
    print("Podaj a,b i h")
    a = float(input("a = "))
    b = float(input("b = "))
    h = float(input("h = "))
    print("Pole trapezu wynosi:")
    print((a+b)*h/2)
if co_mam_zrobic == "D":
    print("Podaj a i h")
    a = float(input("a = "))
    h = float(input("h = "))
    print("Pole trójkąta wynosi:")
    print(a*h/2)
if co_mam_zrobic == "E":
    print("Podaj a")
    a = float(input("a = "))
    print("Obwód kwadratu wynosi:")
    print(a*4)
if co_mam_zrobic == "F":
    print("Podaj r")
    r = float(input("r = "))
    print("Obwód koła wynosi:")
    print(2*r*math.pi)
if co_mam_zrobic == "G":
    print("Podaj a,b i h")
    a = float(input("a = "))
    b = float(input("b = "))
    h = float(input("h = "))
    print("Obwód trapezu wynosi:")
    print((a+b)*h/2)
if co_mam_zrobic == "H":
    print("Podaj a,b i c")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print("Obwód trójkąta wynosi:")
    print(a+b+c)
if co_mam_zrobic == "I":
    print("Podaj a")
    a = float(input("a = "))
    print("Pole powierzchni sześcianu wynosi:")
    print(6*a*a)
if co_mam_zrobic == "J":
    print("Podaj r")
    r = float(input("r = "))
    print("Pole powierzchni kuli wynosi:")
    print(4*math.pi*r**2)
if co_mam_zrobic == "K":
    print("Podaj Pole podstawy i Pole boczne")
    pole_podstawy = float(input("Pole podstawy = "))
    pole_boczne = float(input("Pole boczne = "))
    print("Pole powierzchni graniastosłupa wynosi:")
    print(2*pole_podstawy+pole_boczne)
if co_mam_zrobic == "L":
    print("Podaj a,b,h ścian bocznych oraz ilość ścian")
    pole_podstawy = float(input("Pole podstawy = "))
    pole_boczne = float(input("Pole boczne = "))
    print("Pole powierzchni ostrosłipa wynosi:")
    print(pole_podstawy+pole_boczne)
if co_mam_zrobic == "M":
    print("Podaj a")
    a = float(input("a = "))
    print("Objętość sześcianu wynosi:")
    print(a**3)
if co_mam_zrobic == "N":
    print("Podaj r")
    r = float(input("r = "))
    print("Objętość kuli wynosi:")
    print((4/3)*math.pi*r**3)
if co_mam_zrobic == "O":
    print("Podaj Pole podstawy oraz wysokość")
    pole_podstawy = float(input("Pole podstawy = "))
    h = float(input("h = "))
    print("Objętość graniastosłupa wynosi:")
    print(pole_podstawy*h)
if co_mam_zrobic == "P":
    print("Podaj Pole podstawy oraz wysokość")
    pole_podstawy = float(input("Pole podstawy = "))
    h = float(input("h = "))
    print("Objętość ostrosłupa wynosi:")
    print(pole_podstawy*h)

    