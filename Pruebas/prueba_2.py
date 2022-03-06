#
# lista_1 = "WBWBWWWB"
# lista_2 = "BWBWWWWW"
# lista_1C = []
# lista_2C = []
#
# volteo = 2
# intercambio = 1
#
# fila = 2
# columna = 4
#
# cont = 0
# for f in range(1, int(fila) + 1):
#     for c in range(1, int(columna) + 1):
#         l = lista_1[cont]
#         lista_1C.append([l,f,c])
#         cont = cont + 1
# print(lista_1C)
# cont = 0
# for f in range(1, int(fila) + 1):
#     for c in range(1, int(columna) + 1):
#         l = lista_2[cont]
#         lista_2C.append([l,f,c])
#         cont = cont + 1
#
# print(lista_2C)
#
# # [['W', 1, 1], ['B', 1, 2], ['B', 1, 3], ['B', 2, 1], ['W', 2, 2], ['B', 2, 3], ['W', 3, 1], ['W', 3, 2], ['W', 3, 3]]
# # [['W', 1, 1], ['W', 1, 2], ['W', 1, 3], ['W', 2, 1], ['B', 2, 2], ['W', 2, 3], ['W', 3, 1], ['W', 3, 2], ['B', 3, 3]]
#
#
# if volteo == intercambio:
#
#     pass
# elif volteo < intercambio:
#     # tiene prioridad el volteo
#     print(volteo)
# elif volteo > intercambio:
#     # tiene prioridad el intercambio
#     # print(intercambio)
#     print(intercambio)


# cadena = ''
#
# intercambio = 1
# inter = 0
# for l in range(1,3):
#     for j in range(1,3):
#         print(l,j)
#         cadena = cadena + "Hola,"
#         inter = inter + intercambio
#         print(inter)


# A = ["a", "b", "c"]
# StrA = "".join(A)
# print(StrA)

import math as ma
import numpy as no



#intercambiar > voltear
# 6     mayor      3
#intercambiar < voltear
# 6     menor      3

intercambiar = 65
voltear = 2

if intercambiar <= (voltear*2) or voltear <= (intercambiar*2):
    print(voltear)
elif intercambiar == voltear:
    print("Somos Iguales")
elif intercambiar > (voltear*2) or voltear > (intercambiar*2):
    print("Tegano")