print("###  INSCRIPCION A BECA UNIVERSITARIA 2026 ###")

nombre_completo = str(input("Ingrese su nombre de pila: ")).strip()
edad = int(input("Ingrese su edad: "))
promedio_notas = float(input("Ingrese su promedio de notas (0 a 10): "))
ingreso_mensual = float(input("Ingrese su ingreso mensual en USD: "))

id = nombre_completo[0:3].lower() + str(edad)[-2:]
print(f"Su ID de beca es: {id}")

es_apto= (edad >= 17 and  promedio_notas >= 8.5 or ingreso_mensual <= 2500)
if es_apto:
    print(f"Felicitaciones {nombre_completo}, usted fue aprobado para la beca universitaria del corriente año.")
else:
    print(f"Muchas gracias por su participacion en nuestro programa de becas {nombre_completo}, lamentablemente hemos decidido que no cumple con las condiciones para concedersela.")

monto = 500

if promedio_notas >= 9.5:
    monto *= 1.20
    print(f"Adicionalmente, por su alto desempeño academico, aumentamos su beca un 20% mas.")
elif promedio_notas >= 8.5:
    monto *= 1.10
    print(f"Adicionalmente, por su buen desempeño academico, aumentamos su beca un 10% mas.")
else: 
    print("No se aplican bonificaciones adicionales a su beca.") 

print(f"Finalmente, usted {id} recibira una monto mensual de la beca de un total de  {round(monto, 2)} USD durante todo el año academico.")