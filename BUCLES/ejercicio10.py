numero = int(input("Introduce un número entero: "))
for i in range(2, numero):
    if numero % i == 0:
        break
if (i + 1) == numero:
    print("El número es primo")
else: 
    print("El número no es primo")