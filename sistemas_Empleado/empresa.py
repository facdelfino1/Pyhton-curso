from empleado import Empleado
class Empresa:

    def __init__(self,nombre):
        self.nombre = nombre
        self.empleados = [] # Atributo de instancia

    def contratar_empleado(self,nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)

    def obtener_nro_empleados_por_departamento(self, departamento):
       contador_por_departamento = 0
       for empleado in self.empleados:
           if empleado.departamento == departamento:
                contador_por_departamento += 1
    
       return contador_por_departamento
    
    def obtener_total_empleados(self):
        print(f"Total empleados en la empresa: {self.empleados}")
        for empleado in self.empleados:
            print(f"Empleado: {empleado.nombre} - Departamento: {empleado.departamento}")
        return len(self.empleados)


