# Areli Sarai García Medina | 20310380

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    # Dividir la lista en dos mitades
    mitad = len(lista) // 2
    izq = lista[:mitad]
    der = lista[mitad:]

    # Ordenar recursivamente cada mitad
    izq_ordenada = merge_sort(izq)
    der_ordenada = merge_sort(der)

    # Combinar las mitades ordenadas en una sola lista ordenada
    return merge(izq_ordenada, der_ordenada)


def merge(izq, der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    # Agregar los elementos restantes de la lista izquierda
    resultado += izq[i:]

    # Agregar los elementos restantes de la lista derecha
    resultado += der[j:]

    return resultado


# Ejemplo de uso
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
ordenada = merge_sort(lista)
print(ordenada)