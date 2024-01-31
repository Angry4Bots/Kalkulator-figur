import math

class torus:
    def __init__(self, r, R):
        self.r = r
        self.R = R
    def pole(self):
        pole = 4*math.pi**2*self.r*self.R
        print(pole)
    def zmiana(r, R):
        pole_zmiana = 4*math.pi**2*r*R
        print(pole_zmiana)
class Graniastoslup_prawidlowy_trojkatny:
    def __init__(self, Pp, Pb):
        self.Pp = Pp
        self.Pb = Pb
    def pole(self):
        pole = 2*self.Pp + self.Pb
        print(pole)
    def zmiana(Pp, Pb):
        pole_zmiana = 2*Pp + Pb
        print(pole_zmiana)
class kula:
    def __init__(self, r):
        self.r = r
    def pole(self):
        pole = 4*math.pi*self.r
        print(pole)
    def zmiana(r):
        pole_zmiana = 4*math.pi*r
        print(pole_zmiana)
Siusiak = torus(10, 10)
Siusiak.pole()
torus.zmiana(5, 10)