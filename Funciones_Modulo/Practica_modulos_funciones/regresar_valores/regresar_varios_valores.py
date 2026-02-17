print( " Regresar varios valores desde una función " )

def personas_mayus(nombre,apellido, edad):
    print(f" Esta funcion devuelve varios valores ")
    return nombre.upper(), apellido.upper(), edad   


print(" Ingreso de datos ")
nombre,apellido, edad= personas_mayus('Facu', 'Delfino',23)
print(f" El resultado es, nombre: {nombre}, apellido: {apellido}, edad: {edad} ")

print(" Fin del programa ")