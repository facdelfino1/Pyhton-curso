class Aritmeticas:
    def __init__(Self,operador1,operador2):
        Self._operador1 = operador1
        Self._operador2 = operador2
    
    def get_suma(Self):
        resultado = Self._operador1 + Self._operador2
        return resultado
    
    def set_suma(self,operador1, operador2):
        self._operador1 = operador1
        self._operador2 = operador2
    
    def get_resta(Self):
        resultado_resta = Self._operador1 - Self._operador2
        return resultado_resta
    
    def set_resta(self,operador1, operador2):
        self._operador1 = operador1
        self._operador2 = operador2


operaciones1= Aritmeticas (20,93)
print(f"El resultado de la suma es: {operaciones1.get_suma()}")
print(f"El resultado de la resta es: {operaciones1.get_resta()}")
print("\n")
operaciones2= Aritmeticas (100,50)
print(f"El resultado de la suma es: {operaciones2.get_suma()}")
print(f"El resultado de la resta es: {operaciones2.get_resta()}")
print("\n")
operaciones2.set_suma(149,120)
print(f"El resultado de la  de  suma es: {operaciones2.get_suma()}")
operaciones2.set_resta(19,11)
print(f"El resultado de la resta es: {operaciones2.get_resta()}")