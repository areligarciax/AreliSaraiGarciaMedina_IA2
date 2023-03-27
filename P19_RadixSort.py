# Areli Sarai García Medina | 20310380

# Importamos un Método de la biblioteca random
from random import randint

# Generamos una lista de 10 números aleatorios entre 0 y 100
lista = [randint(0, 100) for _ in range(10)]
print("Lista desordenada:", lista)


# Definimos la función de ordenamiento radixsort
def radixsort(lista):
    # Obtenemos el número máximo de dígitos en los elementos de la lista
    max_num = max(lista)
    num_digits = len(str(max_num))

    # Realizamos el ordenamiento según cada dígito, desde el menos significativo al más significativo
    for i in range(num_digits):
        listasb = [[] for _ in range(10)]  # Creamos 10 listas vacías para almacenar los elementos
        for num in lista:
            digit = (num // 10 ** i) % 10  # Obtenemos el dígito correspondiente al paso actual
            listasb[digit].append(num)  # Agregamos el número al bucket correspondiente

        lista = [num for bucket in listasb for num in bucket]  # Unimos los buckets en una sola lista

    return lista


# Ordenamos la lista con radixsort
lista_ordenada = radixsort(lista)
print("Lista ordenada:", lista_ordenada)