numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))
if numero2 == 0:
    print("ERROR: No se puede dividir entre cero.")
else:
    division = numero1 / numero2
    print(f"El resultado de la división es: {division}.")
