# Z1 Napisz skrypt w Pythonie, który wyznaczy sumę zbiorów A, B i C.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {5, 6, 9, 10}

def zad1(a,b,c):
    return a,b,c  
print(zad1(A,B,C))
# Z2 Napisz funkcję w Pythonie, która zwróci przecięcie zbiorów A i B.
def zad2(a,b):
    return a & b  
print(zad2(A,B))

# Z3 Napisz skrypt, który usunie wszystkie elementy ze zbioru C.
def zad3(c):
    c.clear()
c_copy = C.copy()
print(zad3(c_copy))
# Z4 Napisz funkcję, która sprawdzi, czy zbiór A jest podzbiorem zbioru B.
def zad4(a,b):
    if a & b == a:
        return "Tak jest"
    else:
        return "Nie nie jest"
print(zad4(A,B))
# Z5 Utwórz zbiór D zawierający elementy od 1 do 10 za pomocą funkcji range/set i porównaj go ze zbiorem A. Napisz funkcję, która zwróci elementy, które są w D, ale nie ma ich w A.
D = set(range(1,11))
def zad5(a,d):
    return d - a

print(zad5(A,D))

# Z6 Napisz funkcję, która zwróci symetryczną różnicę zbiorów B i C.
def zad6(b,c):
    return b ^ c
print(zad5(B,C))
# Z7 Utwórz skrypt, który doda element 11 do wszystkich trzech zbiorów A, B i C.
def zad7(a,b,c):
    a.add(11)
    b.add(11)
    c.add(11)
    return a,b,c
print(zad7(A,B,C))
# Z8 Napisz funkcję, która zwróci różnicę między zbiorem B a zbiorem A.
def zad8(a,b):
    return b - a  
print(zad8(A,B))
# Z9 Napisz skrypt, który utworzy zbiór E zawierający wszystkie parzyste liczby zawarte w zbiorach A, B i C.
def zad9(a,b,c):
    E = set()
    for el in a:
        if el % 2 == 0:
            E.add(el)
    for el in b:
        if el % 2 == 0:
            E.add(el)
    for el in c:
        if el % 2 == 0:
            E.add(el)
    return E
print(zad9(A,B,C))


