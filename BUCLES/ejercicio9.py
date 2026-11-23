intento = input("Introduzca la contraseña: ")
contraseñacorrecta = "contraseña"
while intento != contraseñacorrecta:
    print("La contraseña es incorrecta.")
    intento = input("Introduzca de nuevo la contraseña: ")
if intento == contraseñacorrecta:
    print("La contraseña es correcta.")
