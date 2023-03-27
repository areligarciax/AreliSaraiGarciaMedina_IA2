# Areli Sarai García Medina | 20310380

# Importamos un Método de la biblioteca random para generar listas aleatorias
from random import sample

lista = list(range(100))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample
# (10 elementos aleatorios de la lista base)
vectorshell = sample(lista, 10)


def shellsort(vectorshell):
    # Esta función ordenara el vector que le pases como argumento con el Método Shell Sort

    print("El vector a ordenar con shell es:", vectorshell)

    largo = 0

    for i in vectorshell:
        largo += 1

    distancia = largo // 2

    # Creamos un bucle según las distancias
    while distancia > 0:
        # Utilizamos el Insertionsort
        for i in range(distancia, largo):
            valor = vectorshell[i]
            j = i
            while j >= distancia and vectorshell[j - distancia] > valor:
                vectorshell[j] = vectorshell[j - distancia]
                j -= distancia
            vectorshell[j] = valor
            # Acotamos/Disminuimos la distancia nuevamente y continua el ciclo
        distancia //= 2
    print("El vector ordenado con shell es: ", vectorshell)

shellsort(vectorshell)