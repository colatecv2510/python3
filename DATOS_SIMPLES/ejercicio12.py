panfresco = 3.49
descuento = 0.60
panantiguosvendidos = float(input("Introduce la cantidad de pan vendidos: "))
panantiguo = panfresco * (1- descuento)
costetotal = panantiguo * panantiguosvendidos
print(f"El precio habitual de una barrra de pan es {panfresco}€.")
print(f"El descuento que se le hace por no ser fresca es de {descuento}%.")
print(f"El coste del pan que no es del dia es de{panantiguo:.2f}€.")