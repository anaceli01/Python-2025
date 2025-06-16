


productos = ['Smarthpone', 'Laptop', 'Tablet', 'Smartwatch']
precios = [300, 800, 150, 200]
stock = {
    'Smartphone' : 25,
    'Laptop' : 12,
    'Tablet' : 8,
    'Smartwatch' : 4
}

max_precio = max(precios)
min_precio = min(precios)

prod_max = productos[precios.index(max_precio)]
prod_min = productos[precios.index(min_precio)]

print(f'El artículo más caro es: {prod_max}, precio: ${max_precio}')
print(f'El artículo más barato es: {prod_min}, precio: ${min_precio}')

print('Clasificación por precio:')

for prod, precio in zip(productos, precios):
    if precio < 200:
        categoria = 'Producto Económico'
    elif precio <= 500:
        categoria = 'Producto Estándar'
    else:
        categoria = 'Producto Premium'

    print(f'{prod}: ${precio}')


print('Los productos que tienen menos de 10 unidades disponibles son:')
for prod, cantidad in stock.items():
    if cantidad < 10:
        print(f'{prod} con {cantidad} unidades')