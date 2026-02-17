print("### Sistema de Menu ###")

salir = False
while not salir:


    print("1. Crear Cuenta")
    print("2. Eliminar cuenta")
    print("3. Salir")

    ingreso_opcion =  int(input("ingrese una opcion:")) 

    if ingreso_opcion == 1:
        print("Creando su cuenta .... \n")
    elif ingreso_opcion == 2:
        print("Se esta eliminando su cuenta ....\n ")
    elif ingreso_opcion == 3:
        print("Saliendo ....\n")
        salir = True
    else: 
        print("Opcion invalida, vuelva a ingresar una opcion valida.") 