# # **KWargs - keyword arguments**:
# #son argumentos que se pasan a una función utilizando un nombre específico para cada argumento. 
# #Esto permite que los argumentos se pasen en cualquier orden y hace que el código sea más legible.

# print("### Ejemplo de uso de kwargs ###")

# def superheroe_superpoderes(nombre,*args, **kwargs):
#     print(f"Superheroe: {nombre} - {args} - Mas info: {kwargs}")

# #Llamamos a la funcion
# superheroe_superpoderes("Superman", "volar", Velocidad = "super rápida", Fuerza = "super fuerte")
# superheroe_superpoderes("Superman", "volar", "Pegar" ,Velocidad = "super rápida", Fuerza = "super fuerte")

# #Es opcional enviar argumentos variables, pero si se envian, deben ser enviados con el formato correcto.
# superheroe_superpoderes("Mi vecino", velocidad = "Lenta")
# # o sin argumentos variables
# superheroe_superpoderes("Mi vecino") 

# def crear_cv(nombre, *lenguajes, **otros_datos):
#     print("### Creando CV ###")
#     datos_formateados = '\n'.join([f'{key}: {value}' for key, value in otros_datos.items()])
#     print(f"Nombre: {nombre}\nLenguajes: {', '.join(lenguajes)}\n{'-'*30}\nDatos Adicionales:\n{datos_formateados}")



# crear_cv("Facundo", "Python", "Java", "SQL", Edad = 30, Ciudad = "Cordoba", posicion = "Desarrollador")


def construir_query(tabla, **filtros):
    for key, value in filtros.items():
        if isinstance(value, int):
                tipo = "Filtrado por rango"
        else:
                tipo = "Filtrado por categoria"
            
        print(f"Filtro: {key} - Valor: {value} - Tipo: {tipo}")

construir_query("usuarios", edad=30, ciudad="Cordoba", activo=True)
construir_query("productos", precio=100, categoria="Electronica", stock=50)
