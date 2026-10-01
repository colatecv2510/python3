cantidad = float(input("Introduce la cantidad que quieres invertir: "))
interes = float(input("Introduce el interés anual que quieres tener: "))
años = float(input("Introduce el número de años que quieres invertir: "))
capital = (cantidad*(interes/100)*años) #Hecho con la formula interes simple
print(f"La cantidad del capital obtenido en la inversión es {capital}€.") 