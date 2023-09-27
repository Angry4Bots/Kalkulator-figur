# Utwórz pustą listę o nazwie "numbers".
# numbers = []
# print(numbers)
# Poproś użytkownika o podanie 5 liczb i dodaj je do listy.
#print("Podaj pięć liczb")
#a = float(input())
#b = float(input())
#c = float(input())
#d = float(input())
#e = float(input())
#numbers = [a,b,c,d,e]
#print(numbers)
# Oblicz sumę liczb znajdujących się w liście "numbers"
#numbers = [0,1,3,4,5,7,8,9]
#suma = 0
#i = 0
#while len(numbers) > i:
#    suma += numbers[i]
#    i += 1
#    if i >= len(numbers):
#        print(suma)
#        break
# Znajdź największą liczbę w liście "numbers".
#numbers = [0,10,53,89,12,423]
#najwyzsza = numbers[0]
#i = 0
#while len(numbers) > i:
#    if najwyzsza < numbers[i]:
#        najwyzsza = numbers[i]
#    i += 1
#    if i >= len(numbers):
#        print(najwyzsza)
#        break
# Znajdź najmniejszą liczbę w liście "numbers".
#numbers = [0,10,53,89,12,423]
#najnizsza = numbers[0]
#i = 0
#while len(numbers) > i:
#    if najnizsza > numbers[i]:
#        najnizsza = numbers[i]
#    i += 1
#    if i >= len(numbers):
#        print(najnizsza)
#        break
# Policz średnią arytmetyczną liczb w liście "numbers".
#numbers = [0,10,53,89,12,423]
#suma = 0
#i = 0
#while len(numbers) > i:
#   suma += numbers[i]
#    i += 1
#    if i >= len(numbers):
#        print(suma/len(numbers))
#        break
# Znajdź ilość liczb parzystych w liście "numbers".
#numbers = [0,10,53,89,12,423]
#parzyste = 0
#i = 0
#while len(numbers) > i:
#    if (numbers[i] % 2) == 0 and (numbers[i] == 0) == False:
#        parzyste += 1
#    i += 1
#   if i >= len(numbers):
#        print(parzyste)
#       break
# Stwórz nową listę o nazwie "duplicates" zawierającą powtarzające się elementy z listy "numbers".
# duplicates = [0,0,0,10,10,53,53,89,12,12,423]
# Usuń wszystkie powtarzające się elementy z listy "numbers".
#duplicates = [0,0,0,10,10,53,53,89,12,12,423]
#numbers = []




#i = 0
#while i < len(duplicates):
#    if duplicates[i] not in numbers:
#        numbers.append(duplicates[i])
#    i += 1



#print(numbers)
# Stwórz nową listę o nazwie "squares" zawierającą kwadraty liczb z listy "numbers".
numbers = [0, 10, 53, 89, 12, 423]
squares = []
i = 0
while i < len(numbers):
    squares.append(numbers[i]**2)
    i += 1

print(squares)




