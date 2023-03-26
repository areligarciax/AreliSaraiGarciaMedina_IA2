# Areli Sarai García Medina | 20310380

# Importamos la libreria
import heapq

# Creamos la lista
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Obtener los 4 elementos más pequeños de la lista
n_elementos = 4
nsmallest = heapq.nsmallest(n_elementos, lista)

# Imprimimos los 4 elementos más pequeños
print(nsmallest)