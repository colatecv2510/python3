edad = int(input("Introduce tu edad: "))
ingresos = int(input("Introduce tus ingresos mensuales: "))

if edad > 16 and ingresos >= 1000:
    print("Si que tiene que tributar.")
else:
    print("No tiene que tributar.")