edadclientes = int(input("Introduce tu edad: "))
if edadclientes < 4:
    print ("Puede entrar gratis.")
elif edadclientes <= 18:
    print ("El precio es de 5€.")
else:
    print ("El precio es de 10€.")