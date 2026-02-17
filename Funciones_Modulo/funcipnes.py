def procesar_pago(precio,porcentaje_descuento):
    if precio <= 0:
        return "Error: Precio invalido"
    

    precio_final = precio - (precio * porcentaje_descuento / 100)
    return precio_final
    
precio =  int(input("Ingrese el precio del producto: "))
porcentaje_descuento = int(input("Ingrese el porcentaje de descuento: "))

resultado_desucento = procesar_pago(precio,porcentaje_descuento)
print(f"El precio final con descuento es: {resultado_desucento}")
