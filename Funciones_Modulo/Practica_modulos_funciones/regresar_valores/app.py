from Practica_modulos_funciones.regresar_valores.validaciones import validar_usuario, validar_Contraseña

def iniciar_usuario():
    nombre= str(input("Ingrese su nombre de usuario: "))

    while not validar_usuario(nombre):
        print("Error: El nombre de usuario debe tener al menos 3 caracteres.")
        nombre= str(input("Ingrese su nombre de usuario: "))
        
    print("Nombre de usuario válido.")
    

    contraseña= str(input("Ingrese su contraseña: "))
    while not validar_Contraseña(contraseña):
        print("Error: La contraseña debe tener al menos 8 caracteres, incluyendo al menos un número.")
        contraseña= str(input("Ingrese su contraseña: "))
    
    print("Contraseña válida.") 
    print(f"Bienvenido al sistema {nombre}!")
iniciar_usuario()


