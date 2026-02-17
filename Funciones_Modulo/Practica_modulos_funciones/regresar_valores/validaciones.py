def validar_usuario(nombre):
    
    if len(nombre) < 3:
        return False
        
    return True

def validar_Contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    
    for caracter in contraseña:
        if caracter.isdigit():   
            return True
    
    return False



