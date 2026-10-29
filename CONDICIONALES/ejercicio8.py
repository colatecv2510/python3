puntuación = float(input("Introduce tu puntuación: "))
sueldobase = 2400
if puntuación == 0.0:
    print("Nivel: Inaceptable")
    print("Tu sueldo es: ", sueldobase * puntuación, "€")
elif puntuación == 0.4:
    print("Nivel: Aceptable")
    print("Tu sueldo es: ", sueldobase * puntuación, "€")
elif puntuación >= 0.6:
    print("Nivel: Meritorio")
    print("Tu sueldo es: ", sueldobase * puntuación, "€")
else:
    print("Puntuación no válida. Los valores permitidos son 0.0, 0.4 o 0.6 en adelante.")
