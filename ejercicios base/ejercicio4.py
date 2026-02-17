lista_calificaciones = []

cantidad_calificaciones = int(input("Ingrese la cantidad de calificaciones que desea promediar: "))

for calificaciones in range(cantidad_calificaciones):
    calificacion = float(input(f"Ingrese la calificacion {calificaciones + 1}: "))
    lista_calificaciones.append(calificacion)

promedio_gral = round(sum(lista_calificaciones) / cantidad_calificaciones, 2)
promedio = promedio_gral

print(f"El promedio general de las calificaciones es de : {promedio_gral}")

if promedio >= 7 and promedio <= 10:
    print("¡Excelente desempeño!")
elif promedio >= 5 and promedio < 7:
    print("Buen trabajo, pero hay espacio para mejorar.")
elif promedio >= 4 and promedio < 5:
    print("Necesitas esforzarte más.")
else:
    print("Reprobado. Es importante dedicar más tiempo al estudio.")

