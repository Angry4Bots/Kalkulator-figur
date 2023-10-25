import math
def kwadrat_pole():
    print("Podaj a")
    a = float(input("a = "))
    print("Pole kwadratu wynosi:")
    print(a*a)
def koło_pole():
    print("Podaj r")
    r = float(input("r = "))
    print("Pole koła wynosi:")
    print((r*math.pi)**2)
def trapez_pole():
    print("Podaj a,b i h")
    a = float(input("a = "))
    b = float(input("b = "))
    h = float(input("h = "))
    print("Pole trapezu wynosi:")
    print((a+b)*h/2)
def trójkąt_pole():
    print("Podaj a i h")
    a = float(input("a = "))
    h = float(input("h = "))
    print("Pole trójkąta wynosi:")
    print(a*h/2)
def kwadrat_obwód():
    print("Podaj a")
    a = float(input("a = "))
    print("Obwód kwadratu wynosi:")
    print(a*4)
def koło_obwód():
    print("Podaj r")
    r = float(input("r = "))
    print("Obwód koła wynosi:")
    print(2*r*math.pi)
def trapez_obwód():
    print("Podaj a,b i h")
    a = float(input("a = "))
    b = float(input("b = "))
    h = float(input("h = "))
    print("Obwód trapezu wynosi:")
    print((a+b)*h/2)
def trójkąt_obwód():
    print("Podaj a,b i c")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print("Obwód trójkąta wynosi:")
    print(a+b+c)
def sześcian_powierzchni():
    print("Podaj a")
    a = float(input("a = "))
    print("Pole powierzchni sześcianu wynosi:")
    print(6*a*a)
def kula_powierzchni():
    print("Podaj r")
    r = float(input("r = "))
    print("Pole powierzchni kuli wynosi:")
    print(4*math.pi*r**2)
def graniastosłup_powierzchni():
    print("Podaj Pole podstawy i Pole boczne")
    pole_podstawy = float(input("Pole podstawy = "))
    pole_boczne = float(input("Pole boczne = "))
    print("Pole powierzchni graniastosłupa wynosi:")
    print(2*pole_podstawy+pole_boczne)
def ostrosłup_powierzchni():
    print("Podaj a,b,h ścian bocznych oraz ilość ścian")
    pole_podstawy = float(input("Pole podstawy = "))
    pole_boczne = float(input("Pole boczne = "))
    print("Pole powierzchni ostrosłupa wynosi:")
    print(pole_podstawy+pole_boczne)
def sześcian_objętość():
    print("Podaj a")
    a = float(input("a = "))
    print("Objętość sześcianu wynosi:")
    print(a**3)
def kula_objętość():
    print("Podaj r")
    r = float(input("r = "))
    print("Objętość kuli wynosi:")
    print((4/3)*math.pi*r**3)
def graniastosłup_objętość():
    print("Podaj Pole podstawy oraz wysokość")
    pole_podstawy = float(input("Pole podstawy = "))
    h = float(input("h = "))
    print("Objętość graniastosłupa wynosi:")
    print(pole_podstawy*h)
def ostrosłup_objętość():
    print("Podaj Pole podstawy oraz wysokość")
    pole_podstawy = float(input("Pole podstawy = "))
    h = float(input("h = "))
    print("Objętość ostrosłupa wynosi:")
    print(pole_podstawy*h)            
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
    kwadrat_pole()
if co_mam_zrobic == "B":
    koło_pole()
if co_mam_zrobic == "C":
    trapez_pole()
if co_mam_zrobic == "D":
    trójkąt_pole()
if co_mam_zrobic == "E":
    kwadrat_obwód()
if co_mam_zrobic == "F":
    koło_obwód()
if co_mam_zrobic == "G":
    trapez_obwód()
if co_mam_zrobic == "H":
    trójkąt_obwód()
if co_mam_zrobic == "I":
    sześcian_powierzchni()
if co_mam_zrobic == "J":
    kula_powierzchni()
if co_mam_zrobic == "K":
    graniastosłup_powierzchni()
if co_mam_zrobic == "L":
    ostrosłup_powierzchni()
if co_mam_zrobic == "M":
    sześcian_objętość()
if co_mam_zrobic == "N":
    kula_objętość()
if co_mam_zrobic == "O":
    graniastosłup_objętość()
if co_mam_zrobic == "P":
    ostrosłup_objętość()
                

