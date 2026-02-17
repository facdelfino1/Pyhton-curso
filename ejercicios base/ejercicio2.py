    # 1. Solicitar NOMBRE del aspirante por teclado.
    
    # 2. Validar si el nombre es "ADMIN":
    #    - Usar un operador de comparación que ignore mayúsculas/minúsculas.
    #    - Si es verdadero, terminar el ciclo principal inmediatamente (BREAK).

    # 3. Iniciar un ciclo WHILE para validar la EDAD:
    #    - Condición: El ciclo se repite si la edad es menor a 13 O mayor a 90.
    #    - Dentro: Pedir edad, convertir a entero y manejar posibles errores de entrada.

    # 4. Solicitar CORREO electrónico por teclado.
    
    # 5. Definir la CATEGORÍA usando una estructura condicional y operadores lógicos:
    #    - REGLA 1 (AND): Si tiene 18 años o más Y el correo termina en ".edu".
    #    - REGLA 2: Para todos los demás casos.
    #    - TIP: No olvides usar paréntesis si decides combinar más condiciones.

    # 6. Imprimir un mensaje final para este aspirante con su NOMBRE y CATEGORÍA.

# 7. Al terminar el ciclo FOR (fuera del bucle), imprimir "Fin del proceso".}


print("### Sistema de welcome ###")


edad_estudiante = 0

for i in range(3):
    nombre= str(input("Ingrese su nombre de pila:")).strip()

    if nombre.lower() == "admin":
        print("acceso denegado")
        break

    while edad_estudiante < 13 or edad_estudiante > 90:
        try:
            edad_estudiante = int(input(f"Ingrese la edad de {nombre}: "))
            if edad_estudiante < 13 or edad_estudiante > 90:
                print("Edad no permitida (debe ser entre 13 y 90).")
        except ValueError:
            print("Error: Ingrese un número entero para la edad.")
       
    correo_electronico = str(input("Ingrese su correo electronico:")).strip()
    if edad_estudiante >= 18 and correo_electronico.endswith(".edu"):
            categoria = "Categoria A"
    else:
            categoria = "Categoria B"
    print(f"El aspirante {nombre} pertenece a la {categoria}.")
    
print("Fin del proceso.")



