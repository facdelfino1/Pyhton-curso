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
    auto1.marca= ("Honda") 
    auto1.modelo= ("CR-V") 
    auto1.color= ("Azul") 

    #Intentar agregar un nuevo atributo a la instancia auto1  SOLO SIRVE PARA AUTO1, NO PARA AUTO2
    setattr(auto1, "año", 2022) # Agregamos un nuevo atributo a la instancia auto1
    print(f"El año del auto aplicando nuevos atributos con setattr es: {auto1.año}") # Imprim

    auto2= Coche('Chevrolet', 'Trailblazer', 'Negro', '2017')

    auto1.conducir()