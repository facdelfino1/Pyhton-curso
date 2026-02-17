from Practica_modulos_funciones.finanzas.finanzas import calcular_percepcion, convertir_a_pesos, calcular_impuesto_pais

VALOR_DOLAR = 1450


def iniciar_conversion():
    precio_producto_dolares = float(input("Ingrese el precio del producto en dólares: "))

    while precio_producto_dolares <= 0:
        print("Error: La tasa de cambio debe ser un número positivo.")
        precio_producto_dolares = float(input("Ingrese el precio del producto en dólares: "))

    base_pesos = convertir_a_pesos(precio_producto_dolares, VALOR_DOLAR)
    impuesto = calcular_impuesto_pais(base_pesos)
    percepcion = calcular_percepcion(base_pesos)
    total_pesos = base_pesos + impuesto + percepcion

    print("\n" + "="*20)
    print("      Ticket" )
    print("="*20)
    print(f"Precio base: ${base_pesos:.2f} pesos")
    print(f"Impuesto PAIS: ${impuesto:.2f} pesos")
    print(f"Total a pagar: ${total_pesos:.2f} pesos")
    print(f"Precio con percepción: ${percepcion:.2f} pesos")


iniciar_conversion()


        

