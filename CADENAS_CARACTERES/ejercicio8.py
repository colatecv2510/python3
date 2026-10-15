#precioproducto = float(input("Introduce el precio de un producto en euros: "))
precioproducto = input("Introduce el precio de un producto en euros: ")
parte = precioproducto.split(".")
euros = parte[0]
centimos = parte[1][:2]
print(f"El es precio de un producto de {euros} euros y {centimos} céntimos." )