# 1. Iniciar ciclo FOR para 4 reservas.

# 2. Pedir NOMBRE. Si es "SALIR" -> break.

# 3. Iniciar ciclo WHILE para la HORA (validar entre 9 y 23).
  #    - Usar try-except para evitar errores de tipeo.

# 4. Pedir TIPO DE CANCHA (Fútbol o Tenis).
    
# 5. Pedir si alquila EQUIPAMIENTO (Si o No).

# 6. Definir UBICACION (VIP o Lateral) usando operadores:
#  - Regla 1: Tenis Y hora > 18.
#  - Regla 2: Fútbol Y alquila pelotas.
#  - Usar paréntesis para separar estas dos reglas grandes unidas por un OR.

# 7. Imprimir resumen de la reserva.

print(" ### Sistema de Reservas de canchas ### ")



for i in range(4):
    nombre= str(input("Ingrese su nombre de pila:")).strip()
    if nombre.lower() == "salir":
        print("Su solicitud esta siendo procesada, saliendo del sistema ...")
        break
    hora = 0
    while hora < 9 or hora > 23:
        try:
            hora = int(input(f"Ingrese la hora de reserva para {nombre}, debe ser entre 9 y 23hs: "))
        except ValueError:
            print("Error: Ingrese un numero compatible para la hora.")

    print(""" Tipos de canchas disponibles:\n
        1. Futbol
        2. Tenis
          """)
    
    tipo_cancha = int(input("Ingrese el tipo de cancha que desea reservar (Futbol o Tenis): "))

    if tipo_cancha == 1:
        print("Ha sido seleccionada la cancha de futbol")
    elif tipo_cancha == 2:
        print("Ha sido seleccionada la cancha de tenis")
    else:
        print("Tipo de cancha invalida, por favor seleccione una opcion valida.")

    necesita_equipamiento = str(input("Desea alquilar equipamiento? (Si/No): ")).strip().lower()
    if necesita_equipamiento == "si":
        alquila_equipamiento = True
    else: 
        alquila_equipamiento = False
    
    if (tipo_cancha == 2 and hora > 18) or (tipo_cancha == 1 and alquila_equipamiento):
        ubicacion = "VIP"
    else:
        ubicacion = "Lateral"
    
    print(f"La reserva a pedido de { nombre}, es para el horario {hora}hs, en una cancha de {'Futbol' if tipo_cancha == 1 else 'Tenis'}, con equipamiento: {'Si' if alquila_equipamiento else 'No'}, en ubicacion: {ubicacion}.")


 