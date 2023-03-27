# Areli Sarai García Medina | 20310380

objetos = [
    {"Nombre": "Areli", "edad": 25},
    {"Nombre": "Sarai", "edad": 18},
    {"Nombre": "Cecille", "edad": 30}
]

# Ordenar los objetos por edad en orden ascendente
objetos.sort(key=lambda x: x["edad"])
print(objetos)