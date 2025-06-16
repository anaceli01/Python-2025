
from colorama import init, Fore #FUNCIÓN 'FORE' EXTRAE LOS COLORES
init()

#CONDICIONAL IF
print(Fore.CYAN + '############ 01 - UTILIZANDO IF Y ELSE#########')

licencia = False
edad = 19
automovil = False

#¿ESTARÁ CORRECTO ESTE CÓDIGO?
#Incorrecto

print(Fore.YELLOW + '\n>>>Testeando los comparadores y el IF')
if licencia and edad>= 18:
    print(Fore.WHITE + 'Puedo conducir porque tengo licencia.')
elif automovil:
    print(Fore.WHITE + 'Tengo automóvil, pero no la edad ni la licencia.')
else:
    print(Fore.WHITE + 'No puedo conducir porque no tengo ni la edad, ni la licencia, ni automóvil.')





              