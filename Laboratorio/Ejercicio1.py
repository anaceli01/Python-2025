#Karla - Ignacio
#Una ferretería necesita desarrollar un programa que permita gestionar el stock de productos de 
#su tienda. La ferretería requiere saber el total a pagar por la cantidad de herramientas 
#ingresadas a su bodega. (50 Puntos)

#Pedir por consola los precios unitarios (float) y las cantidades (int) de cuatro productos:

#Martillo 
pma = float(input("Ingrese el precio unitario del martillo: "))
cma = int(input("Ingrese la cantidad disponible de martillos: "))

#Clavos
pcl = float(input("Ingrese el precio unitario de los  clavos: "))
ccl = int(input("Ingrese la cantidad disponible de los clavos: "))

#Serrucho 
pse = float(input("Ingrese el precio unitario del serrucho: "))
cse = int(input("Ingrese la cantidad disponible del serruchos: "))

#Tornillos
pto = float(input("Ingrese el precio unitario de los tornillos: "))
cto = int(input("Ingrese la cantidad disponible de los tornillos: "))

#Calcular y mostrar los subtotales para cada producto y redondearlos a 2 decimales.
sma = pma * cma #martillo

scl = pcl * ccl #clavos

sse = pse * cse #serrucho

sto = pto * cto #tornillos

#Imprimir los siguientes resultados, en este orden: 

#Subtotal Martillo | Subtotal Clavos | Subtotal Serrucho | Subtotal Tornillos 
# b. Suma total de los cuatro subtotales. 
st = sma + scl + sse + sto

# c. Valor máximo entre los cuatro subtotales. 
vmax = max(sma, scl, sse, sto)


# d. Valor mínimo entre los cuatro subtotales. 
vmin = min(sma, scl, sse, sto)

# e. Promedio del precio unitario de las herramientas, redondeado a 2 decimales 
ppu = pma + pcl + pse + pto / 4

# f. Obtener el IVA (19%) del total de las herramientas ingresadas al sistema. 
i = (sma + scl + sse + sto) * 19 / 100
iva = st + i

print(f"Subtotal del martillo: {sma: .2f} CLP, Subtotal de clavos: {scl: .2f} CLP, Subtotal de serruchos: {sse: .2f} CLP, Subtotal de tornillos: {sto: .2f} CLP")
print(f"Suma de los 4 productos: {st: .2f} CLP")
print(f"El valor maximo entre los 4 productos es: {vmax} CLP")
print(f"El valor minimo entre los 4 productos es: {vmin} CLP")
print(f"El promedio del precio unitario de las herramientas es de: {iva: .2f} CLP")
print(f"El IVA es : {i}")
print(f"El total de todo con el IVA aplicado es de: {iva: .2f} CLP")

