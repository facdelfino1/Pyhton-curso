inventario = []

productos= int(input("Ingrese la cantidad de productos a agregar al inventario: "))


for indice in range(productos):
    print(f"\nIngresando datos del producto {indice + 1}:")
    nombre_prod= str(input("Nombre: ")).strip()
    precio_prod = float(input("Precio: "))
    cantidad_prod = int(input("Cantidad: "))
    

    dict_producto = {"id": indice,
                      "Nombre": nombre_prod,
                      "Precio": precio_prod,
                      "Cantidad": cantidad_prod
                    }
    inventario.append(dict_producto)

print(f"\nInventario registrado: {inventario}")


id_search = int(input("\nIngrese el ID a buscar: "))
producto_encontrado = None
for producto in inventario:
        if producto.get('id') == id_search:
            producto_encontrado = producto
            break

if producto_encontrado is not None:
        print(f" Producto encontrado:")
        print(f"  ID : {producto_encontrado.get('id')}")
        print(f"  Nombre : {producto_encontrado.get('Nombre')}") # Usamos la llave fija entre comillas
        print(f"  Precio : {producto_encontrado.get('Precio')}")
        print(f"  Cantidad : {producto_encontrado.get('Cantidad')}")
else:
        print("ID no encontrado.")