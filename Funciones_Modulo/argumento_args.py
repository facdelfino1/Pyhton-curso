# from datetime import datetime   
# print(" ### Registrar eventos ###")

# def registrar_eventos(nivel,*eventos):
#     ahora = datetime.now().strftime(" %H:%M:%S")
       
#     evento_str = ' '.join(eventos) # Si lo hacia ' '.join(eventos) no hacia falta el replace del if.
    
#     prefijo = "⚠️" if nivel.lower() == "error" else " "
#     print(f"{prefijo} [{nivel.upper()}] [{ahora}] - {evento_str}")

# registrar_eventos("error","el","usuario","no","ingresó","al","sistema")
# registrar_eventos("Info","el","usuario","ingresó","al","sistema")


# def analizar_precios(categoria, *precios):
#     print(f"La categoria es: {categoria.upper()}")
    
#     try:
#         cantidad_prod = len(precios)
#         precio_max = max(precios) if precios else 0
#         precio_prom = sum(precios) / len(precios) if precios else 0
#         print(f"""\tAnlizando Categoria: {categoria.upper()}\n\t{'-'*30}\n\tProductos: {cantidad_prod}\n\tPrecio Maximo: ${precio_max}\n\tPromedio: ${precio_prom:.2f}""")
#     except TypeError:
#         print("Error: Se proporcionaron valores no numéricos en los precios.")


# analizar_precios("Electronica", 1000, 1500, 2000)
# analizar_precios("Ropa", 500, 700, 'HOLA', 400)


def formatear_etiquetas(prefijo, *palabras):

    simbolos= ['#', '@', '$', '%', '&']
    if prefijo not in simbolos:
        print("Error: El prefijo debe ser uno de los siguientes símbolos: #, @, $, %, &")
        return None
    resultado = []
    for p in palabras:
        etiqueta = prefijo + p.lower()
        resultado.append(etiqueta)
    resultado_str = ','.join(resultado) 
    return resultado_str 

formatear_etiquetas("-","Soy","Facu","Como estas vos? Yo estoy bien")
print(formatear_etiquetas("#","Soy","Facu","Como estas vos? Yo estoy bien"))