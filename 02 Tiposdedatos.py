
#01 DECLARANDO E INICIALIZANDO VARIABLES NÚMERICAS
edad = 31
estatura = 1.71
peso = 75.4
complejo = 1 + 9j
complejo2 = complex(1, 4)

print (complejo)
print (complejo2)

#02 OPERACIÓN ARITMÉTICA
imc = peso / (estatura ** 2)
print (f"Su IMC es: {imc}")


#03 FORMATEO DE SALIDA DEL RESULTADO (PARA ACORTAR DECIMALES)

#FORMA 1 (UTILIZANDO F-STRINGS Y : .2f)
print(f"Su IMC es: {imc:.2f}") #Salida con dos decimales

#FORMA 2 (UTILIZANDO EL MÉTODO FORMAT)
print("Su IMC es: {:.2f}".format(imc)) #Salida con dos decimales

#APLICANDO MÉTODO ROUND
print((round)(imc, 2))

#TRANSFORMANDO UN NÚMERO ENTERO EN UN NÚMERO FLOTANTE (DECIMAL)
print (float(edad))

#04 DATOS DE TIPO STRING (CADENAS DE TEXTO)

carrera = "Ingeniería Civil en Informática"
asignatura = "Programación"
descripcion = '''Esta es una asignatura de primer semestre'''

print (carrera [0]) #Imprime el primer carácter de la cadena
print (carrera[-1]) #Imprime el último carácter de la cadena


print("Hola" * 4) #Imprime 4 veces
#print("Hola" /2)

#UTILIZANDO EL INTERVALO DE UNA CADENA
print (asignatura[0:5]) #Imprime desde el primer carácter (0) hasta el sexto (5)

#UTLIZANDO EL MÉTODO SPLIT (GENERA UN ARREGLO DE CADENA)
print (descripcion.split()) #Imprime separando carácter por carácter

#ARREGLO NUMÉRICO
v = [1, 2, 3, 4, 5] #Inicializando un arreglo numérico
print (v[0]) #






