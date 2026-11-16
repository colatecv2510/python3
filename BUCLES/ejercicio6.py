numeroentero = int(input("Introduce un número entero: "))
for i in range(numeroentero):
    for j in range(i + 1):
        print("*", end="")
    print("")

# Otra forma
# numeroentero = int(input("Introduce la altura del triángulo (entero positivo): "))
# for i in range(numeroentero):
#    print("*"*(i+1))