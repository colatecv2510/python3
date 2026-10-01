n = int(input("Introduce un número: "))
m = int(input("Introduce otro número: "))
c = n//m
r = n%m
print("La división ", n ,"entre", m, " da un cociente", c, " y un resto", r,) 
# Otra manera de hacerlo es con print(f)
# De esta manera: print(f"La división {n} entre {m} da un cociente {c} y un resto {r}")
