producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
unidades = int(input("Introduce el número de unidades: "))
total = precio*unidades
print(f"El nombre del producto es {producto} y el precio producto es {precio:2f} el cual tiene {unidades:03d} unidades y un coste de {total:011.2f}.")
