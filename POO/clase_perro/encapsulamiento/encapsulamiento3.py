class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca #Atributo Publico
        self._modelo = modelo #  Atributo Protegido
        self._color = color # Atributo Privado

    def conducir(self):
        print(f"""\t Conduciendo el auto
            Marca: {self._marca}
            Modelo: {self._modelo}
            Color: {self._color}""")
        

    @property
    def marca(self): #Se recupera el valor del atributo privado marca
        return self._marca
    
    @marca.setter
    def marca(self, marca): #Se establece un nuevo valor para el atributo privado marca
        self._marca = marca
        
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):   
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color


        
#Programa Principal
if __name__ == "__main__":
    auto1 = Coche("Toyota", "Corolla", "Rojo")
    auto1.conducir()
    print("\n")
    auto1.marca= ("Honda") # Modificando el atributo publico
    auto1.modelo= ("CR-V") # Modificando el atributo protegido (no recomendado)
    auto1.color= ("Azul") # Modificando el atributo privado a través del setter
    auto1.conducir()