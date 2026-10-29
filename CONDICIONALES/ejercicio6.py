nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (F o M): ")
sexo_mayus = sexo.upper()
nombre_mayus = nombre.upper()
if sexo_mayus == "F" and nombre_mayus < "M" or sexo_mayus == "M" and nombre_mayus > "N":
    print("Tu clase es la A.")
else:
    print("Tu clase es la B.")