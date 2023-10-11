# 6.Napisz funkcję która z przyjmuje jako argument powyższą listę i zwrócić mi ile jest większych lub równych 0. 
# list = [-1,-50,0,10,25,15,13]
# list_wieksze_0 = []
# i = 0
# while i <= len(list):
#     if list[i] >= 0 or list[i] == 0:
#         list_wieksze_0.append(list[i])
#     i += 1
#     if i >= len(list):
#         print(list_wieksze_0)
#         break


# 7.Napisz program która z przyjmuje jako argument powyższą listę i zwrócić mi sumę wszystkich elementów parzystych. 
# list = [-1,-50,0,10,25,15,13]
# list_wieksze_0 = []
# i = 0
# suma = 0
# while i <= len(list):
#     if list[i] % 2 == 0:
#         list_wieksze_0.append(list[i])
#         suma += list[i]
#     i += 1
#     if i >= len(list):
#         print(list_wieksze_0)
#         print(suma)
#         break


# 8.Napisz program która z przyjmuje jako argument powyższą listę i zwrócić mi sumę wszystkich elementów nieparzystych .
# list = [-1,-50,0,10,25,15,13]
# list_wieksze_0 = []
# i = 0
# suma = 0
# while i <= len(list):
#     if list[i] % 2 != 0:
#         list_wieksze_0.append(list[i])
#         suma += list[i]
#     i += 1
#     if i >= len(list):
#         print(list_wieksze_0)
#         print(suma)
#         break
 

# 9.Napisz funkcję która przyjmuje jako argument powyższą listę i zwrócić mi sumę wszystkich elementów podzielnych przez 5 i 7. 
# list = [-1,-50,0,10,25,15,13]
# list_wieksze_0 = []
# suma = 0
# for el in list:
#     if el % 5 == 0 or el % 7 == 0:
#          list_wieksze_0.append(el)
#          suma += el
# print(list_wieksze_0)
# print(suma)


# 10.Napisz program która z przyjmuje jako argument powyższą listę poprosi o podanie liczby przez użytkownika i powie ile takich liczb występuje na tej liście. 
list = [-1,-50,0,10,25,15,13]
list_wieksze_0 = []
inp = int(input())
suma = 0
for el in list:
    if el == inp:
         suma += 1
print(suma)






