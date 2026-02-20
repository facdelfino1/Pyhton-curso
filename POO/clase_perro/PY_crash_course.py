# # class Restaurante():
# #     """Una clase que representa un restaurante"""
# #     def __init__(Self,nombre_restaurante,tipo_cocina):
# #         """Inicializa los atributos nombre_restaurante y tipo_cocina"""
# #         Self.nombre_reestaurante = nombre_restaurante
# #         Self.tipo_cocina = tipo_cocina
    
# #     def describe_restaurante(Self):
# #         """Muestra una descripción del restaurante"""
# #         print(f"El restaurante se llama {Self.nombre_reestaurante} y sirve comida {Self.tipo_cocina}.")
    
# #     def open_restaurante(Self):
# #         """Indica que el restaurante está abierto"""
# #         print(f"{Self.nombre_reestaurante} está abierto.")


# # restaurante_italiano = Restaurante("La Trattoria", "italiana")
# # restaurante_italiano.describe_restaurante()
# # restaurante_italiano.open_restaurante()
# # print("\n")
# # restaurante_Español = Restaurante("El Rincón Español", "española")
# # restaurante_Español.describe_restaurante()
# # restaurante_Español.open_restaurante()
# # print("\n")
# # restaurante_argentino = Restaurante("El Asado Argentino", "argentina")
# # restaurante_argentino.describe_restaurante()
# # restaurante_argentino.open_restaurante()


# class usuario:
#     """Clase que representa al usuario"""
#     def __init__(Self,first_name,last_name):
#         Self.first_name = first_name
#         Self.last_name = last_name

#     def describe_user(Self):
#         print(f"El nombre del usuario es {Self.first_name} y su apellido es {Self.last_name}.")
    
#     def greet_user(Self):
#         print(f"Hola! Soy {Self.first_name} {Self.last_name} y queria mandarte un gran saludo!")


# usuario1 = usuario("Facu", "Delfino")
# usuario1.describe_user()
# usuario1.greet_user()
# print("\n")
# usuario2 = usuario("Fabian", "Delfino")
# usuario2.describe_user()
# usuario2.greet_user()


print("TRABAJAR CON INSTANCIAS")

class Auto:

    def __init__(Self,marca,modelo,año): # Metodo __init__ es el constructor de la clase
        Self.marca = marca #Atributos de instancia
        Self.modelo = modelo
        Self.año = año
        Self.kilometraje = 0 #Atributo de instancia con valor por defecto
    
    def descripcion(Self):
        nombre_largo= (f"El auto es un {Self.marca} {Self.modelo} del año {Self.año}.")
        return nombre_largo
    
    def leer_kilometros(Self):
        print(f"Este auto tiene {Self.kilometraje} kilometros recorridos.")


    def update_kilometraje(Self,km): # 2. Metodo para actualizar el valor del atributo kilometraje
        """Establece el kilometraje al valor dado"""

        if km >= Self.kilometraje:
            Self.kilometraje = km
        else: 
            print("No puedes reducir el kilometraje de un auto, ES ILEGAL.")

    def incrementar_kilometraje(Self,km): # 3. Metodo para incrementar el valor del atributo kilometraje
        """Suma la cantidad de kilometros al kilometraje actual"""
        if km >= 0:
             Self.kilometraje += km
        else:
            print("No puedes reducir el kilometraje de un auto, ES ILEGAL.")
            
mi_auto = Auto("Toyota", "Corolla", 2020) #<-- Parametros
mi_auto.descripcion()
mi_auto.leer_kilometros()
print("\n")
mi_auto.kilometraje = 245 # 1. Modificar el valor del atributo kilometraje manuealmente
mi_auto.leer_kilometros() # 2. Verificar que el valor del atributo kilometraje se ha actualizado
print("\n")
mi_auto.update_kilometraje(500) # 3. Usar el metodo update_kilometraje() para actualizar el valor del atributo kilometraje
mi_auto.leer_kilometros() # 4. Verificar que el valor del
print("\n")

mi_auto_usado = Auto("Chevrolet", "Cruze", 2021)
print(mi_auto_usado.descripcion())
mi_auto_usado.update_kilometraje(15000)
mi_auto_usado.leer_kilometros()
print("\n")
mi_auto_usado.incrementar_kilometraje(500)
mi_auto_usado.leer_kilometros()