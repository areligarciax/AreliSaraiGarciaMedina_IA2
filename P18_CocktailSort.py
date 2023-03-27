# Areli Sarai García Medina | 20310380

# Importamos un Método de la biblioteca random para generar listas aleatorias
from random import sample

lista = list(range(100))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample (10 elementos aleatorios de la lista base)
vectorcocktail = sample(lista, 10)


def cocktailsort(vectorcocktail):
    # Esta función ordenará el vector que le pases como argumento con el Método de Cocktail Sort

    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con Cocktail es:", vectorcocktail)

    largo = 0  # Establecemos un contador del largo

    for _ in vectorcocktail:
        largo += 1  # Obtenemos el largo del vector

    for i in range(largo // 2):  # Comenzamos desde la mitad aproximadamente
        cambiar = False
        # Declaramos la variable que indica si es necesario intercambiar o no
        for j in range(1 + i, largo - i):
            # Probar si los dos elementos están en el orden incorrecto
            if vectorcocktail[j] < vectorcocktail[j - 1]:
                # Entonces ambos elementos cambian de lugar
                vectorcocktail[j], vectorcocktail[j - 1] = vectorcocktail[j - 1], vectorcocktail[j]
                cambiar = True
        # Si no ocurren cambios, salimos del bucle
        if not cambiar:
            break
        cambiar = False
        for j in range(largo - i - 1, i, -1):
            # Probar si los dos elementos están en el orden incorrecto
            if vectorcocktail[j] < vectorcocktail[j - 1]:
                # Entonces ambos elementos cambian de lugar
                vectorcocktail[j], vectorcocktail[j - 1] = vectorcocktail[j - 1], vectorcocktail[j]
                cambiar = True
        if not cambiar:
            break

    print("El vector ordenado con Cocktail es: ", vectorcocktail)


cocktailsort(vectorcocktail)