cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (%): "))
años = int(input("Introduce el número de años: "))
for i in range(1, años + 1):
    cantidad *= 1 + (interes / 100)
    print(f"Capital tras el año {i}: {cantidad:.2f} €")