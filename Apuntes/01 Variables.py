'''Guía inicial de Python (Variables)'''

#Variables
nombre = "Karla"
apellido = "Miranda"

#Formas de escribir el print

#Con coma
print ("Hola, mi nombr es ", nombre, " y mi apellido es", apellido)

#Con signo + (Operador de concatenación)
print ("Hola, mi nombre es " + nombre + " y mi apellido es " + apellido)

#Con llaves, f-string (Cadenas literales)
print (f"Hola, mi nombre es {nombre} y mi apellido es {apellido}")

#Variables
ciudad, region, pais = "Castro", "Los lagos", "Chile"

print (f"Hola soy de {ciudad}, {region}, {pais}")


#USO DEL INPUNT
# \n ES UN SALTO DE LÍNEA

print (nombre)
nombre=str(input("ingrese su nombre: \n"))
print (f"Hola, mi nombre es: {nombre}")

print (nombre)