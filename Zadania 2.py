# Wyświetl wszystkie liczby z listy "numbers" w odwrotnej kolejności.
# numbers = [0,10,53,89,12,423]
# undo_numeros = []
# i = len(numbers)
# while i >= 0:
#    undo_numeros.append(numbers[i - 1])
#    i -= 1 
#    if i <= 0:
#        print(undo_numeros)
#        break
# Poproś użytkownika o podanie liczby. Sprawdź, czy liczba ta znajduje się w liście "numbers".
# numbers = [0,10,53,89,12,423]
# inp = float(input())
# i = 0 
# while i <= len(numbers) - 1:
#     if inp == numbers[i]:
#         print ("tak")
#         break
#     elif inp != numbers[i]:
#         i += 1
# else:
#     print("nie")

    
    
# Wyświetl indeks pierwszego wystąpienia danej liczby w liście "numbers".
# numbers = [0,10,53,89,12,423]
# i = 0 
# x = numbers.index(i)
# while i <= len(numbers):
#     print("indeks",numbers[i],"w numbers jest równy ",x)
#     i += 1
#     if i == len(numbers):   
#         break



# Znajdź ilość liczb większych niż 10 w liście "numbers".
# numbers = [0,10,53,89,12,423]
# numberswiekszeoddziesiec = []
# i = 0 
# while i <= len(numbers):
#     if numbers[i] > 10:
#         numberswiekszeoddziesiec.append(numbers[i])
#     i += 1
#     if i == len(numbers): 
#         print(numberswiekszeoddziesiec)  
#         break

# Posortuj listę "numbers" w kolejności malejącej.
# numbers = [0,10,53,89,12,423]
# numbers.sort(reverse=True)
# print(numbers)  
# Znajdź drugą największą liczbę w liście "numbers".
# numbers = [0,10,53,89,12,423]
# numbers.remove(max(numbers))
# print(max(numbers))

# Stwórz nową listę o nazwie "doubled_numbers" zawierającą podwojoną wartość każdej liczby z listy "numbers".
# numbers = [0,10,53,89,12,423]
# doubled_numbers = []
# i = 0 
# while i <= len(numbers):
#     doubled_numbers.append(numbers[i]*2)
#     i += 1
#     if i == len(numbers): 
#         print(doubled_numbers)  
#         break

# Zlicz ilość wystąpień danej liczby w liście "numbers".
# numbers = [0,10,53,89,12,423]
# i = 0 
# x = numbers.count(i)
# while i <= len(numbers):
#     print("ilość wystąpień",numbers[i],"w liście numbers jest równa",x)
#     i += 1
#     if i == len(numbers): 
#         break

# Wyświetl wszystkie liczby z listy "numbers" z ich indeks
# numbers = [0,10,53,89,12,423]
# i = 0 
# while i <= len(numbers):
#     print("indeks",numbers[i],"w liście numbers jest równa",numbers.index(numbers[i]))
#     i += 1
#     if i == len(numbers): 
#         break