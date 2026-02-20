class Persona:
    atributo_clase = 0
    def __init__(self,atributo_instancia):
        self.atributo_instancia = atributo_instancia
        
    

#programa principal
if __name__ == "__main__":
    print("Trabajar con atributos de clase")
    print(f'atributo de clase: {Persona.atributo_clase}')
#modificar el atributo de clase
    Persona.atributo_clase = 10
    print(f'atributo de clase: {Persona.atributo_clase}')

#creamos los objetos de persona 1
persona1 = Persona(15)
print(f'persona1 atributo de clase: {persona1.atributo_clase}')
print(f'persona1 atributo de instancia: {persona1.atributo_instancia}')
persona2 = Persona(19)
print(f'persona2 atributo de clase: {persona2.atributo_clase}')
print(f'persona2 atributo de instancia: {persona2.atributo_instancia}')