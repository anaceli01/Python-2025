#Diccionario
inventario = {
    'Manzana' : (4000, 5000, 6000),
    'Platano' : (2000, 3000, 3000),
    'Cereza' : (3500, 4500, 2500)
}

print(inventario)

precios_platano = set(inventario['Platano'])
print(f'Lista de precios únicos del plátano : {precios_platano}')


tipos_de_frutas = ['Manzana', 'Platano', 'Cereza']
print(f"Lista de frutas: {tipos_de_frutas}")

precios_platano = (2000 + 3000 + 3000)  / 3
print(f"El precio de los platanos es: {precios_platano:.3f}")
