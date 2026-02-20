class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca #Atributo Publico
        self._modelo = modelo #  Atributo Protegido
        self.__color = color # Atributo Privado

    def conducir(self):
        print(f"""\t Conduciendo el auto
              Marca: {self.marca}
              Modelo: {self._modelo}
              Color: {self.__color}""")
        
#Programa Principal
if __name__ == "__main__":
    auto1 = Coche("Toyota", "Corolla", "Rojo")
    auto1.conducir()
    print("\n")
    auto1.marca = "Honda" # Modificando el atributo publico
    auto1._modelo = "Civic" # Modificando el atributo protegido (no recomendado)
    # auto1.__color = "Azul" # No se puede modificar el atributo privado directamente
    auto1.conducir()