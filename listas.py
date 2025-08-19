listas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(listas)

lista_vacia = []

lista_vacia.append("Hola")
print(lista_vacia)

lista_vacia.insert(1, True)
print(lista_vacia)
print(lista_vacia[-1])

print(len(lista_vacia))

lista_vacia.remove(1)
lista_vacia.pop()
print(lista_vacia)

#lista_vacia[0] = "Modificado"
#print(lista_vacia)

lista_vacia.extend([1, 2, 3])
print(lista_vacia)


lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista_de_listas)

print(lista_de_listas[1][2])

import random

lista_aletoria = [random.randint(1, 100) for _ in range(10)]
print(lista_aletoria)

import numpy as np
lista_numpy = np.random.randint(1, 100, size=10).tolist()
print(lista_numpy)

lista_numpy.sort() # Ordenar la lista

lista_numpy.reverse() # Invertir el orden de la lista

lista_numpy.count(50) # Buscar el número 50

lista_copiada = lista_numpy.copy()
print(lista_copiada)

listacopia = lista_numpy[:] #copia la de numpy
print(listacopia)

lista_numpy.clear()
print(lista_numpy)

lista_concatenada = lista_numpy + lista_copiada
print(len(lista_concatenada))