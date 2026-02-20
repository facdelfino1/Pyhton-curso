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
        

        #Metodos getter y setter para el atributo privado color
  #Taambien podriamos remplazar el get y colocar @property y el set por @color.setter para hacerlo mas pythonico, pero lo dejamos asi para entender mejor el concepto de encapsulamiento
    def get_marca(self): #Se recupera el valor del atributo privado marca
        return self._marca
    
    def set_marca(self, marca): #Se establece un nuevo valor para el atributo privado marca
        self._marca = marca
        
    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):   
        return self._color
    
    def set_color(self, color):
        self._color = color


        
#Programa Principal
if __name__ == "__main__":
    auto1 = Coche("Toyota", "Corolla", "Rojo")
    auto1.conducir()
    print("\n")
    auto1.set_marca("Honda") # Modificando el atributo publico
    auto1.set_modelo("CR-V") # Modificando el atributo protegido (no recomendado)
    auto1.set_color("Azul") # Modificando el atributo privado a través del setter
    auto1.conducir()