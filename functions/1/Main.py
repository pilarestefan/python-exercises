import funciones as fn

valor = float(input("Ingrese valor: "))
ivaCalculado = fn.calcularIva(valor)
print (f"Iva calculado {ivaCalculado} ")

valorACalcularDescuento = int(input("Ingrese el precio al cual desea calcular su descuento: "))
descuentoARealizar = int(input("Ingrese el descuento a realizar: "))
calculoDescuento = fn.descuento(valorACalcularDescuento,descuentoARealizar)

print (f"valor del producto con el descuento aplicado {calculoDescuento}: ")

estatura = float(input("Ingrese su estatura en metros: "))
peso = int(input("Ingrese su peso en kilogramos: "))
estadoCorporal = fn.calcularImc(estatura, peso)
print (f"Su estado corporal es: {estadoCorporal}")

