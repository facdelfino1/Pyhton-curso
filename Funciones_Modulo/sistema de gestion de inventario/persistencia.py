def guardar_productos(nombre,precio_final, *tags_listas):
    #abre un archivo y agrega el producto al final del archivo
    with open("productos.txt", "a") as archivo:
        tags_listas = ','.join(tags_listas) if tags_listas else 'Sin etiquetas'
        archivo.write(f"{nombre} | ${precio_final} | {tags_listas}\n")


