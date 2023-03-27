# Areli Sarai García Medina | 20310380

# la función bubble_sort recibe una lista y utiliza el algoritmo de ordenamiento por intercambio (Bubble Sort)
# para ordenarla en orden ascendente. El algoritmo recorre la lista desde el primer elemento hasta el penúltimo,
# y en cada iteración, recorre la lista desde el primer elemento hasta el último elemento no ordenado,
# intercambiando elementos adyacentes si están en orden incorrecto.

def bubble_sort(lista):
    # Recorrer la lista desde el primer elemento hasta el penúltimo
    for i in range(len(lista) - 1):
        # Recorrer la lista desde el primer elemento hasta el último elemento no ordenado
        for j in range(len(lista) - 1 - i):
            # Intercambiar elementos adyacentes si están en orden incorrecto
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Ejemplo de uso
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 13, 12, 2, 15]
bubble_sort(lista)
print(lista)