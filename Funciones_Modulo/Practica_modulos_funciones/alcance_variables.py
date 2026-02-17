
#variable global, se puede acceder desde cualquier parte del código, incluso dentro de funciones
contador_global = 0


def incrementar_contador():
    #Declaramos una variable local
    contador_local = 0


#usar variable global 

    global contador_global
    contador_global += 1

#Incrementamos la variable local
    contador_local += 1
    print(f"Contador local: {contador_local}")
    print(f"Contador global: {contador_global}")

incrementar_contador()
incrementar_contador()
