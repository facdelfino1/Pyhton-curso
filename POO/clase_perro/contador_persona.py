class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        Persona.contador_personas += 1
        self.id_persona = Persona.contador_personas 

    def mostrar_info(self):
        print(f"ID: {self.id_persona} - Nombre: {self.nombre} {self.apellido}")

    @staticmethod
    def get_contador_personas(): #Primer metodo estatico
        print("Metodo estatico")
        return Persona.contador_personas


    @classmethod
    def get_contador_personas_class(cls): #Segundo metodo estatico usando decorador
        print("Metodo de clase")
        return cls.contador_personas
# Programa principal
if __name__ == "__main__":
    persona1 = Persona("Facu", "Delfino")
    persona2 = Persona("Fabian", "Delfino")
    persona3 = Persona("Maria", "Gomez")
    persona1.mostrar_info()
    persona2.mostrar_info() 
    persona3.mostrar_info()
    print(f"Total de personas creadas: {Persona.contador_personas}")
    print(f"Total de personas creadas usando el metodo estatico: {Persona.get_contador_personas()}")
    print(f"Total de personas creadas usando el metodo de clase: {Persona.get_contador_personas_class()}")