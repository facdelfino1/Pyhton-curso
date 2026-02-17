print(" ### Gestion del Club ### " )

socios = 3
nombres_socios= []
deportes_disponibles = ["1. Futbol", "2. Tenis"]

for i in range(socios):
    nombre = str(input("Ingrese su nombre completo: ")).split()
    edad = int(input("Ingrese su edad: "))
    deporte= int(input(f"Ingrese un deporte de los cuales tenemos disponibles {deportes_disponibles}: "))
    if deporte == 1:
        print("Usted se ha registrado en futbol")
    elif deporte == 2:
        print("Usted se ha registrado en tenis")

    while (nombre in nombres_socios) and (edad >= 5 and edad <= 80) and (deporte == 1 or deporte == 2):

        try: 
            print("El nombre ya esta en nuestro sistema o la edad no es válida, por favor ingrese otro.")
            
            nombre = str(input("Ingrese su nombre completo: ")).split()
            edad = int(input("Ingrese su edad la cual debe ser mayor a 5 años y menor a 80: "))
            nombres_socios.append(nombre)
                      
        except ValueError:
            print("Error: Por favor ingrese los datos correctamente.")
    
            
            


