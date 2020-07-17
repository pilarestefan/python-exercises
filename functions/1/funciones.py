def calcularIva (precio): 
    iva = precio * 0.19
    return iva

def descuento (precio, descuento):
    valor = precio - descuento
    return valor
    

def calcularImc (estatura, masa):
    iMC = masa / estatura ** 2 
    if (iMC < 18.5 ): 
        return "Bajo peso"
    elif (iMC >= 18.5 and iMC <= 24.9 ): 
        return "Adecuado"
    elif (iMC >= 25.0 and iMC <= 29.9 ): 
        return "Sobre peso"
    elif (iMC >= 30.0 and iMC <= 34.9 ): 
        return "Obesidad Grado 1"
    elif (iMC >= 35.0 and iMC <= 39.9 ): 
        return "Obesidad Grado 2"
    elif (iMC > 40 ): 
        return "Obesidad Grado 3"

