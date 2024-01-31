

def lobotomia(lst,lstklucz):
    inp = input()
    inp = inp
    lst[lstklucz] = inp
    print(lst[lstklucz]) 
def lobotomia3(lst):
    while True:
        print("s - usuń słownik z listy")
        print("z - zmień wartość w książce")
        print("u - usuń klucz w książce")
        print("w - wyjdź z programu")
        inp = input()
        inp = inp
        while inp.lower() not in ["s","z","u","w"]:
            print("wybierz inną odpowiedź")
            inp = input()
            inp = inp
        if inp.lower() == "s":
            print("jakie miejsce zajmuje twój słownik")
            sl = int(input())
            sl = sl
            lst.pop(sl)
            print(lst)
            break
        if inp.lower() == "z":
            print("wpisz miejsce słownika")
            index = int(input())
            slo = lst[index]
            print("wpisz nazwę klucza w słowniku")
            sloklucz = input()
            print("wpisz co chcesz zmienić")
            zmiana = input()
            zmiana = zmiana
            slo[sloklucz] = zmiana
            print(slo[sloklucz])
            break
        if inp.lower() == "u":
            print("wpisz index słownika")
            index = int(input())
            slo = lst[index]
            print("wpisz nazwę klucza")
            sloklucz = input()
            slo.pop(sloklucz)
            print(lst)
            break
        if inp.lower() == "w":
            break



















def lobotomia2(lst,slo,sloklucz):
    inp = input()
    inp = inp
    lst = [slo]
    slo[sloklucz] == inp
    print(slo[sloklucz])