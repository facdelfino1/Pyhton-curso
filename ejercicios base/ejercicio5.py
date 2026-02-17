# # # # 1. Definir la tupla y la lista inicial
# # # producto_base = (101, "Monitor Gamer", "Hardware")
# # # precios = [1500, 1550, 1600]

# # # # 2. Desempaquetado (Unpacking) de la tupla
# # # # TU CODIGO AQUI: id_prod, nombre, rubro = ...

# # # print(f"--- Sistema de Auditoría: {nombre} ---")

# # # # 3. Agregar nuevo precio y eliminar el más antiguo
# # # nuevo_precio = float(input("Ingrese el precio actual de mercado: "))
# # # # TU CODIGO AQUI (usa append y pop)

# # # # 4. Mostrar estado actual de la lista de precios
# # # print(f"Historial de precios actualizado: {precios}")

# # # # 5. Prueba de seguridad (Tupla)
# # # print("\nIntentando modificar datos fijos...")
# # # try:
# # #     # Intenta cambiar el ID o el nombre aquí
# # #     producto_base[0] = 999 
# # # except TypeError:
# # #     print("Resultado: La tupla protegió los datos. No se puede modificar el ID.")

# # producto_base = (101, "Monitor Gamer", "Hardware")
# # precios = [1500, 1550, 1600]
# # id_prod, nombre, rubro = producto_base
# # print(f"--- Sistema de Auditoría: {nombre} ---")

# # nuevo_precio = float(input("Ingrese el precio actual del mercado: "))

# # precios.append(nuevo_precio)
# # precios.pop(0)
# # print(f"Historial de precios actualizado: {precios}")

# # print("\nIntentando modificar datos fijos...")
# # try:
# #      # Intenta cambiar el ID o el nombre aquí
# #     producto_base[0] = 999 
# # except TypeError:
# #     print("Resultado: La tupla protegió los datos. No se puede modificar el ID.")


# registro_base= ( 1001, 55, "2026-02-04")

# estados_pedidos= ["Pendiente", "Procesando", "Enviado"]

# id_pedido, id_cliente, fecha_pedido = registro_base

# nuevo_Estado= str(input("Ingrese un nuevos estado: "))

# estados_pedidos.append(nuevo_Estado) and estados_pedidos.pop(0)

# print(f"El pedido {id_pedido} del cliente {id_cliente} realizado el {fecha_pedido} se encuentra en estado: {estados_pedidos[-1]}. Todos los estados anteriores fueron {estados_pedidos[:-1]}")