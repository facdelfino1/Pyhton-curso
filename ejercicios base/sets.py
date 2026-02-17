suscriptores = set()
suscriptores_min = 15
suscriptores.add("user1@example.com")
extensiones = {".com", ".net", ".org", ".edu"}

for subs in range(suscriptores_min):

    try:
        email= str(input("Ingrese su mail para suscribirse: ")).strip()
        if not any(email.endswith(ext) for ext in extensiones):
            raise ValueError("El mail ya se encuentra registrado")
        
        suscriptores.add(email)
        print(f"La suscripcion fue correcta\n La lista de suscriptores actual es {suscriptores}:")
    except ValueError:
        print("El mail ya se encuentra registrado")

print(f"Lista de suscriptores: {suscriptores}")

        

            