# Areli Sarai García Medina | 20310380

# la función selection_sort recibe una lista y utiliza el algoritmo de ordenamiento por selección para ordenarla en orden ascendente.
# El algoritmo recorre la lista desde el primer elemento hasta el penúltimo y en cada iteración,
    # busca el elemento más pequeño en el resto de la lista y lo intercambia con el elemento actual.

def selection_sort(lista):
    # Recorrer la lista desde el primer elemento hasta el penúltimo
    for i in range(len(lista) - 1):
        # Guardar el índice del elemento más pequeño
        min_indice = i
        # Buscar el elemento más pequeño en el resto de la lista
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_indice]:
                min_indice = j
        # Intercambiar el elemento actual con el más pequeño
        lista[i], lista[min_indice] = lista[min_indice], lista[i]

# Ejemplo de uso
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 13, 12, 2, 15]
selection_sort(lista)
print(lista)