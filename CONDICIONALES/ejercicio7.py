rentaanual = int(input("Introduce tu renta anual: "))
if rentaanual < 10000:
    print ("Tu tipo impositivo es del 5%.")
elif rentaanual <= 20000:
    print ("Tu tipo impositivo es del 15%.")
elif rentaanual <= 35000:
    print ("Tu tipo impositivo es del 20%.")
elif rentaanual <= 60000:
    print ("Tu tipo impositivo es del 30%.")
else:
    print ("Tu tipo impositivo es del 45%.")