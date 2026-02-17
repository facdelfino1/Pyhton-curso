# def funcion_recursiva(n):
#     if n == 1:
#         return 1
#     else:
#         return n + funcion_recursiva(n - 1)

# print(funcion_recursiva(10))

# Conseguir el 5! en recursividad
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n -1)

# print(factorial(5))

# def potencia(base,exponente):
#     if exponente == 0:
#         return 1
#     else: 
#         return base * potencia(base, exponente - 1)

# print(potencia(1000, 3))

def verificar_acceso(nombre, *permisos, **atributos):
    print(f"Verificando acceso para {nombre}...")
    if "admin" in permisos:
        print("Acceso concedido.")
    else:
        print("Acceso denegado. No es admin.")
    if "idiomas" in atributos and atributos["idiomas"] == "español":
        print("Acceso concedido, idioma español.")
    else:
        print("Acceso denegado. No es español")


verificar_acceso("Juan", "admin", "editor", edad=30, ciudad="Buenos Aires", idiomas="español") 
    