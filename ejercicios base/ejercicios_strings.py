# import random as rd 
# # frase = "Programacion"

# # #1 traer CION
# # frase_nueva = frase[8:]
# # #rint(frase_nueva)

# # # 2 extraer G en negativo

# # frase_2 = frase[-9:-8]
# # #print(frase_2)

# # # 3 invertir cadena

# # frase_invertida = frase[::-1]
# # #print(frase_invertida)


# # codigo= "ABC123456XYZ"

# # frase_codigo= codigo[3:9]
# # print(frase_codigo)  # Salida: 123456

# # frase_letras = codigo[-1:-4:-1]
# # print(frase_letras)  # Salida: ZYX

# # frase_prin = codigo[0:3]
# # print(frase_prin)  # Salida: ABC


# # datos = "ID_usuario: 4502 - Nombre: Facundo"

# # # 1. Buscá la posición de "Facundo" usando .find()
# # # 2. Usá esa posición para extraer el nombre con slicing

# # filtro_datos = datos.find("Facundo")
# # print(f"La ubicacion de la letra facundo esta en {filtro_datos} posicion")

# # nombre_extraido = datos[filtro_datos:]
# # print(f"El nombre extraido es: {nombre_extraido}")

# simbolo = "="
# titulo = " Generador de Mails "

# # # Creá una variable linea multiplicando el simbolo por 15.
# linea = simbolo * 15

# # # Imprimí el resultado uniendo linea + titulo + linea.

# # multiplicacion = print(linea + titulo + linea)


# # frase = "Me gusta javaScript porque javaScript es el futuro"

# # # Usá .replace() para cambiar todas las palabras "javaScript" por "Python".

# # # Guardá el resultado en una nueva variable llamada frase_final.

# # # Imprimí frase_final.

# # frase_final = frase.replace("javaScript", "Python")
# # print(frase_final)

# # name= print(linea + titulo + linea)

# # nombre = "Facundo Delfino"
# # empresa = "Tech Solutions"
# # dominio = "com.ar"



# # nombre_limpio = nombre.replace(" ", ".")
# # empresa_limpio=empresa.replace(" ", "")

# # mail = f"{nombre_limpio}@{empresa_limpio}.{dominio}".lower()
# # print(mail)  # Output:



# # edad = int(input("ingresa tu edad: "))
# # print(f"Tu edad es {edad} años, si a tu edad le sumamos 5, será {edad + 5} años")


# #Crear un programa para solicitar la informacion de un empleado, introduciendo los datos por consola

# # nombre_empleado = str(input("ingrese su nombre completo: "))
# # edad_empleado = int(input("ingrese su edad actual: "))
# # salario_Empleado = float(input("ingrese su salario mensual en USD: "))
# # # es_jefe = input("¿ Es jefe de su departamento dentro de la empresa? : (si / no)")

# # # dato_final= f"El nombre completo del empleado es {nombre_empleado}, tiene {edad_empleado} años de edad, su salario mensual actual en USD es de {salario_Empleado} y notifica que {es_jefe} es jefe de su area dentro de la empresa."

# # # # print(dato_final)

# # salario_anual = salario_Empleado * 12
# # bono = round(salario_anual * 1.10, 2)
# # print(f"su salario anual es de: USD {salario_anual}, si le dieran el bono del 10% su slario anual seria de {bono} USD")


# # header = " Receta de cocina "
# # linea = "=" * 10
# # print(linea + header + linea)


# # nombre_receta = str(input("Ingrese el nombre de la receta: "))
# # ingredientes =str(input("Ingrese los ingredientes correspondientes separados por coma: "))
# # tiempo_preparacion= int(input("Ingrese el tiempo de preparacion en minutos: "))
# # dificultad = str(input("Ingrese el nivel de dificultad (facil, intermedio, dificil): "))

# # resultado = f"La receta se llama {nombre_receta}, los ingredientes son {ingredientes}, el tiempo de preparacion es de {tiempo_preparacion} minutos y su nivel de dificultad es {dificultad}."

# # print(resultado)

# #Random sirve para generar numeros aleatorios
# #numero_aleatorio = rd.randint(1, 100) #numero random entre el 1 y 100

# nombre_usuario = str(input("Ingrese su nombre de usuario: "))
# apellido_usuario = str(input("Ingrese su apellido de usuario: "))   
# año_nacimiento = int(input("Ingrese su año de nacimiento: "))

# nombre_usuario_filtrado = nombre_usuario[:3]
# apellido_usuario_filtrado = apellido_usuario[:3]
# año_nacimiento_filtrado = str(año_nacimiento)[-2:]

# valor_Aleatorio =  rd.randint(1000,9999)

# resultado_final = f"El nombre de usuario generado con sus datos es {nombre_usuario_filtrado}{apellido_usuario_filtrado}{año_nacimiento_filtrado}{valor_Aleatorio}".lower()
# print(resultado_final)

# stock_gpus = 20

# # 1. Llega un camión con 15 GPUs nuevas (usá +=)
# # 2. Se venden 8 GPUs a una empresa (usá -=)
# # 3. Se encuentran 2 unidades dañadas y se retiran (usá -=)

# # Imprimí el stock final

# stock_gpus += 15
# stock_gpus -= 8 
# stock_gpus -= 2
# print (f"El stock final luego de realizar todas las operaciones es de: {stock_gpus} unidades")

# salario = 1500

# salario *= 1.10  # Aumento del 10%

# #Al ser ascendido, se le duplica el sueldo
# salario *= 2

# salario_final= round(salario, 2)
# print(f"El salario final del empleado es de: USD {salario_final}")


xp_jugador = 100

#jugador suma 500 xp
xp_jugador += 500
#jugador pierde la mitad de su xp
xp_jugador /= 2
#El jugador triplica su actual xp
xp_jugador *= 3
# Queremos saber cuantas vidas tiene si c/u vale 400xp
print(f"El jugador tiene {xp_jugador // 400} vidas y su xp restante es de {xp_jugador}")
