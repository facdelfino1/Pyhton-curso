from academia import obtener_promedio, evaluar_promedios

nombre= str(input("Ingrese el nombre del estudiante: "))
cantidad_notas= 3
registro_Notas = ()
registro_facultas = {}

for i in range(cantidad_notas):
    nota= float(input(f"Ingrese la nota {i+1}: "))
    registro_Notas += (nota,)

while True:
    ingresar_nuevo_Alumno= int(input("Desea agregar otro alumno? (1.SI / 2.NO)"))
    if ingresar_nuevo_Alumno == 1:
            nombre= str(input("Ingrese el nombre del estudiante: "))
            nota= float(input(f"Ingrese la nota {i+1}: "))
            registro_Notas += (nota,)
            registro_facultas[nombre] = registro_Notas
            
    elif ingresar_nuevo_Alumno == 2:
         for alumno, notas in registro_facultas.items():
             print(f"Alumno: {alumno}, Notas: {notas}")
         break

  

promedio = obtener_promedio(registro_Notas)
aprobado, condicion = evaluar_promedios(promedio)
print(f"""El promedio de 
      Alumno: {nombre}
      Promedio: {promedio:.2f}
      Estado: {condicion}.""")

if aprobado:
    print("Felicidades , sigue asi!.")
