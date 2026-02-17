from validaciones import validar_precio
from persistencia import guardar_productos
from finanzas import calcular_precio_final, convertir_a_pesos, calcular_impuesto_pais, calcular_percepcion

valor_dolar= 1450

inventario = {}

# Bucle para asegurar que el PRECIO sea válido
# ... (importaciones y constantes igual)

while True:
    # 1. Primero pedimos el nombre (para poder salir del programa)
    nombre_producto = input("\nIngrese el nombre del producto (o deje vacío para salir): ").strip().lower()
    if not nombre_producto:
        print("Carga finalizada.")
        break

    # 2. AHORA entramos al bucle de validación de precio para este producto
    while True:
        try:
            entrada = input(f"Ingrese el precio de '{nombre_producto}' en dólares: ")
            precio_dolar = float(entrada)
            
            if validar_precio(precio_dolar):
                break  # Salimos SOLO del bucle de validación
            else:
                print("Error: El precio debe ser mayor a cero.")
        except ValueError:
            print("Error: Ingrese un número válido.")

    # 3. Una vez validado, seguimos con el flujo normal
    precios_ars = convertir_a_pesos(precio_dolar, valor_dolar)
    impuesto = calcular_impuesto_pais(precios_ars)
    percepcion = calcular_percepcion(precios_ars)
    precio_final = calcular_precio_final(precios_ars, impuesto, percepcion)

    tags_list = [t.strip() for t in input("Etiquetas (comas): ").split(',') if t]
    # 4. Guardado
    guardar_productos(nombre_producto, precio_final, *tags_list)
    inventario[nombre_producto] = {
        "precio_dolar": precio_dolar,
        "precio_final": precio_final,
        "etiquetas": tags_list

        # ... podés guardar los otros datos acá también
    }
    
    print(f"✅ Producto '{nombre_producto}' se encuentra en la categoria {', '.join(tags_list)} procesado con éxito.")

# 5. El reporte final va AFUERA de los bucles
print("\n--- RESUMEN DEL INVENTARIO ---")
for producto, detalles in inventario.items():
    tags = ','.join(detalles["etiquetas"])
    print(f"Producto: {producto.capitalize()} | Categoria: {tags} | Final: ${detalles['precio_final']:.2f} ARS")