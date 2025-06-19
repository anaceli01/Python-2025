


resumen = str(input('Ingrese su resumen, debe tener como máximo 50 carácteres: \n'))
resumen = resumen[:50]



resumen_mayuscula = resumen.upper()
resumen_minuscula = resumen.lower()
resumen_contados = len(resumen)
resumen_primeras_15 = resumen[:15]
resumen_segundas_15 = resumen[-15:]
resumenc = resumen_contados <= 50
resumen_j =(resumen.split())
resumen_jo = (resumen_j.join())
print(f"El resumen es menor o igual a 50: {resumenc}")
print(f'Resumen en minúsculas: {resumen_minuscula}')
print(f'Resumen en mayúsculas: {resumen_mayuscula}')
print(f'Cantidad de letras (e) repetidas: {resumen.count('e')}')
print(f'Primeras 15 letras: {resumen_primeras_15}')
print(f'Últimas 15 letras: {resumen_segundas_15}')
print(f'Resumen con comas: {resumen_jo}')

