tipo = input("¿Quieres una pizza vegetariana (v) o no vegetariana (n)?: ").lower()

if tipo == "v":
    ingrediente = int(input("Ingredientes vegetarianos disponibles:\n0. Pimiento\n1. Tofu\nElige un número: "))
    
    if ingrediente == 0:
        print("Tu pizza es vegetariana, por lo tanto, tu pizza llevará Mozzarella, Tomate y Pimiento.")
    elif ingrediente == 1:
        print("Tu pizza es vegetariana, por lo tanto, tu pizza llevará Mozzarella, Tomate y Tofu.")
    else:
        print("Opción no válida.")
        
else:
    ingrediente = int(input("Ingredientes no vegetarianos disponibles:\n0. Peperoni\n1. Jamón\n2. Salmón\nElige un número: "))
    
    if ingrediente == 0:    
        print("Tu pizza no es vegetariana, por lo tanto, tu pizza llevará Mozzarella, Tomate y Peperoni.")
    elif ingrediente == 1:
        print("Tu pizza no es vegetariana, por lo tanto, tu pizza llevará Mozzarella, Tomate y Jamón.")
    elif ingrediente == 2:
        print("Tu pizza no es vegetariana, por lo tanto, tu pizza llevará Mozzarella, Tomate y Salmón.")
    else:
        print("Opción no válida.")

