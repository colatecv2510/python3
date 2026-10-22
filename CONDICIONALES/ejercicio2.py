contraseña1 = "contraseña"
contraseña2 = input("Introduce una contraseña: ")
if contraseña1.lower() == contraseña2.lower():
    print("La contraseña introducida por el usuario coincide con la guardada.")
else:
    print("La contraseña introducida por el usuario no coincide con la guardada.")