def obtener_promedio(notas):
    if len(notas)== 0:
        return 0
    
    return sum(notas) / len(notas)

def evaluar_promedios(promedio):
    if promedio >= 7:
        return True, "Aprobado"
    elif promedio >= 4:
        return True, "Final"
    elif promedio < 4: 
        return False, "Reprobado"
    else:
        return False, "Error en el promedio"

