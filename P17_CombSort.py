# Areli Sarai García Medina | 20310380

# Importamos un Método de la biblioteca random para generar listas aleatorias

from random import sample

lista = list(range(100))  # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample (10 elementos aleatorios de la lista base)
vectorcomb = sample(lista, 10)


def combsort(vectorcomb):
    # Esta función ordenará el vector que le pases como argumento con el Método de Comb Sort

    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con CombSort es:", vectorcomb)

    largo = 0  # Establecemos un contador del largo del vector

    for _ in vectorcomb:
        largo += 1

    # Comenzamos con la diferencia o distancia igual al largo del vector
    diferencia = largo

    # Establecemos la variable que define si es necesario o no
    #  intercambiar los numeros que se están comparando
    cambiar = True

    while diferencia > 1 or cambiar:
        diferencia = max(1, int(diferencia / 1.25))
        # La diferencia minima es 1
        # En cada iteración vamos bajando la diferencia
        cambiar = False
        for i in range(largo - diferencia):
            j = i + diferencia
            # Ubicamos el número que está a la distancia x de i
            if vectorcomb[i] > vectorcomb[j]:
                vectorcomb[i], vectorcomb[j] = vectorcomb[j], vectorcomb[i]
                # Hacemos el intercambio de los numeros
                cambiar = True

    print("El vector ordenado con CombSort es: ", vectorcomb)


combsort(vectorcomb)