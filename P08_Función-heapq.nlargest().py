# Areli Sarai García Medina | 20310380

# Importamos la libreria
import heapq

lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 10, 13, 6, 2, 15]

# Obtener los 5 elementos más grandes de la lista
n_elementos = 5
nlargest = heapq.nlargest(n_elementos, lista)
print(nlargest)