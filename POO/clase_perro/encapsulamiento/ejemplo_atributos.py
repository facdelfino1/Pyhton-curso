"""
Ejemplo claro de atributos de clase vs atributos de instancia
"""

class Coche:
    # ATRIBUTO DE CLASE: compartido por TODAS las instancias
    # Pertenece a la clase, no a instancias específicas
    ruedas = 4  # Todos los coches tienen 4 ruedas
    marca_fabrica = "Motor Company"  # Misma para todos
    
    def __init__(self, marca, color, año):
        # ATRIBUTOS DE INSTANCIA: únicos para cada objeto
        # Cada coche tiene su propia marca, color y año
        self.marca = marca
        self.color = color
        self.año = año
        self.velocidad = 0  # Cada coche tiene su propia velocidad actual


# CREAMOS DOS INSTANCIAS
coche1 = Coche("Toyota", "rojo", 2020)
coche2 = Coche("Ford", "azul", 2022)

print("=" * 60)
print("ATRIBUTOS DE INSTANCIA (únicos para cada coche)")
print("=" * 60)
print(f"Coche 1: {coche1.marca} {coche1.color} ({coche1.año})")
print(f"Coche 2: {coche2.marca} {coche2.color} ({coche2.año})")
print()

# Cada coche tiene su propia velocidad
coche1.velocidad = 100
coche2.velocidad = 50
print(f"Velocidad coche1: {coche1.velocidad} km/h")
print(f"Velocidad coche2: {coche2.velocidad} km/h")
print()

print("=" * 60)
print("ATRIBUTOS DE CLASE (compartidos por todas las instancias)")
print("=" * 60)

print(f"Ruedas desde la clase: {Coche.ruedas}")
print()

# Ambos coches comparten los mismos atributos de clase

print(f"Marca de fábrica desde la clase: {Coche.marca_fabrica}")
print()

print("=" * 60)
print("¿QUÉ PASA SI MODIFICAMOS UN ATRIBUTO DE CLASE?")
print("=" * 60)
# Cambiar atributo de clase (afecta a TODAS las instancias)
Coche.ruedas = 5
print(f"Cambié ruedas a 5...")
print(f"Ruedas de coche1: {coche1.ruedas}")
print(f"Ruedas de coche2: {coche2.ruedas}")
print()

print("=" * 60)
print("CASO ESPECIAL: Crear atributo de instancia con mismo nombre")
print("=" * 60)
# Ahora creamos un atributo de instancia con el mismo nombre
coche1.ruedas = 3  # Esto crea un atributo de INSTANCIA que oculta el de clase
print(f"Asigné coche1.ruedas = 3")
print(f"Ruedas de coche1 (ahora es de instancia): {coche1.ruedas}")
print(f"Ruedas de coche2 (sigue siendo de clase): {coche2.ruedas}")
print(f"Ruedas desde la clase: {Coche.ruedas}")
print()

print("=" * 60)
print("RESUMEN")
print("=" * 60)
print("""
ATRIBUTO DE CLASE (ruedas, marca_fabrica):
✓ Se define en el cuerpo de la clase (fuera de __init__)
✓ Es compartido por TODAS las instancias
✓ Se accede con: clase.atributo o instancia.atributo
✓ Cambiar en la clase afecta a todas las instancias
✓ Útil para valores que son iguales en todos los objetos

ATRIBUTO DE INSTANCIA (marca, color, año, velocidad):
✓ Se define en __init__ con self.atributo
✓ Cada instancia tiene su propio valor
✓ Cambios en una instancia NO afectan a las otras
✓ Útil para valores que varían entre objetos
""")
