from empresa import Empresa
from empleado import Empleado

print("Sitemas de empleados en una empresa")

empresa1 = Empresa("CPJ")

#contratar empleados

empresa1.contratar_empleado("Fabian", "Pediatra")
empresa1.contratar_empleado("Maria", "Limpieza")
empresa1.contratar_empleado("Facu", "Sistemas")

#Obtener total objetos empleados

print(f"Total empleados en la empresa: {Empleado.obtener_total_empleados()}")

print(f"Total de empleados en el departamento de sistemas: {empresa1.obtener_nro_empleados_por_departamento('Sistemas')}")