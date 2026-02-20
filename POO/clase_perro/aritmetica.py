class Aritmetica:

    def __init__(self,operador1, operador2):

        self._operador1 = operador1
        self._operador2 = operador2
    
    def suma(self):
        resultado = self._operador1 + self._operador2
        return resultado
    
    def resta(self):
        resultado_resta = self._operador1 - self._operador2
        return resultado_resta
    
    def multiplicacion(self):
        resultado_multiplicacion = self._operador1 * self._operador2
        return resultado_multiplicacion
    

aritmetica1 = Aritmetica(5,7)
print(f"El resultado de la suma de los operadores es {aritmetica1.suma()}\n El resultado de la resta de los operadores es {aritmetica1.resta()}\n El resultado de la multiplicacion de los operadores es {aritmetica1.multiplicacion()}")
print("\n")
aritmetica2 = Aritmetica(12,16)
print(f"El resultado de la suma de los operadores es {aritmetica2.suma()}\n El resultado de la resta de los operadores es {aritmetica2.resta()}\n El resultado de la multiplicacion de los operadores es {aritmetica2.multiplicacion()}")
       