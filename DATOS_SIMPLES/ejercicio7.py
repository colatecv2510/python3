peso = float(input("¿Cual es el tu peso en kg? "))
estatura = float(input("¿Cuál es el tu peso en metros? "))
indice = peso / (estatura ** 2)
print("Tu índice de masa corporal es: ", round(indice, 2))