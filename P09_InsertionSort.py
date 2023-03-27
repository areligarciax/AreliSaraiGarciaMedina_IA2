# Areli Sarai García Medina | 20310380
# La función insertion_sort recibe una lista y utiliza el algoritmo de ordenamiento por inserción para ordenarla en orden ascendente.
#  El algoritmo recorre la lista desde el segundo elemento hasta el final y en cada iteración, mueve los elementos mayores que
    # el elemento actual una posición hacia adelante, para finalmente colocar el elemento actual en su posición correcta.

def insertion_sort(lista):
    # Recorrer la lista desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        # Guardar el elemento actual en una variable temporal
        actual = lista[i]
        # Guardar el índice anterior al elemento actual
        j = i - 1
        # Mover los elementos mayores al elemento actual una posición hacia adelante
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        # Colocar el elemento actual en su posición correcta
        lista[j + 1] = actual

# Ejemplo de uso
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 13, 15, 6, 2]
insertion_sort(lista)
print(lista)