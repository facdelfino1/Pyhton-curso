# agenda = {}

# numero_usuarios= 3

# for usuarios in range(numero_usuarios):
#     print(f"\nIngresando datos del usuario {usuarios + 1}:")

#     nombre = input("Ingrese el nombre del contacto: ")

#     while nombre in agenda:
        
#         print("El nombre ya existe. Pruebe con otro.")
#         nombre= input("Ingrese el nombre del contacto: ")
    
#     agenda[nombre]= {"telefono": int(input("Ingrese el número de teléfono: ")),
#                      "email": str(input("Ingrese el correo electrónico: ").strip()),
#                      "direccion": str(input("Ingrese la dirección: ").strip())
#                      }

# print("\n--- Agenda de Contactos ---")
# for nombre, datos in agenda.items():
#     print(f"\nContacto: {nombre}")
#     print(f"  Teléfono: {datos['telefono']}")
#     print(f"  Email: {datos['email']}")
#     print(f"  Dirección: {datos['direccion']}")
    
    
inventario = {}

productos = int(input("Ingrese la cantidad de productos a registrar: "))

for producto in range (productos):
    print(f"\ningresando los datos del producto {producto + 1}:")
    nombre_prod = str(input("Ingrese el nombre del producto: ").strip())

    while nombre_prod in inventario:
        print("El nombre del producto ya existe. Pruebe con otro.")
        nombre_prod =str(input("Ingrese el nombre del producto: ").strip())
    
    inventario[nombre_prod] = {
        "precio": float(input("Ingrese el precio del producto: ")),
        "cantidad": int(input("Ingrese la cantidad en stock: ")),
        "categoria": str(input("Ingrese la categoría del producto: ").strip())
    }

print(f"El inventario quedo configurado de la siguiente manera:\n {inventario[nombre_prod]}, con un total de {productos} productos registrados. ")