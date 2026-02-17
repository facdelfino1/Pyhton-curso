def convertir_a_pesos(dolares, tasa_cambio):
    valor_pesos = dolares * tasa_cambio
    
    return valor_pesos

def calcular_impuesto_pais(monto_pesos):
    impuesto = monto_pesos * 0.30
    return impuesto

def calcular_percepcion(monto_pesos):
    # Supongamos que la percepción es del 45%
    return monto_pesos * 0.45