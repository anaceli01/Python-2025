
entrada = input('Ingrese número entero: \n') #valor ingresado es un string

try:
    numero = int(entrada) #aquí se pasa a número (int)
    print(f'Número ingresado: {numero}')
except ValueError:  #Error por tipo de dato      #ValueError es una sublcase de Exception
    print('Error de valor: El valor ingresado no es entero')
except Exception as e: #errores genéricos e inesperados
    print(f'Error inesperado: {e}')
else:
    print('Conversión fue exitosa')
finally:
    print('Finalización del bloque')




