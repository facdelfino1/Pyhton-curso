class Dog:
    """intento de modelar un perro con una clase""" 
    def __init__(self, name, age):
        "Inicializar atributos de nombre y edad"
        self.name = name
        self.age = age

    def sit(self):
        "Simular que el perro se sienta"
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        "Simular que el perro se da vuelta"
        print(f"{self.name} rolled over!")

mi_perro = Dog("Willie", 6) ##INSTANCIA 1
print(f"Mi perro se llama {mi_perro.name} y tiene {mi_perro.age} años.")

mi_perro.sit()
mi_perro.roll_over()
print(mi_perro.name)   

tu_perro = Dog("Drogo", 5) ##INSTANCIA 2
print(f"Tu perro se llama {tu_perro.name} y tiene {tu_perro.age} años.")
tu_perro.sit()
tu_perro.roll_over()
print(tu_perro.name)