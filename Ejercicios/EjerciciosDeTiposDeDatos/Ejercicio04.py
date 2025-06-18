#Desarrollar un programa de gestión de inventario

producto = str(input('Ingrese el nombre del producto: \n'))
precio_unitario = float(input(f'Ingrese el precio unitario del {producto}: \n'))
cantidad_stock = int(input('Ahora ingrese la cantidad en stock: \n'))

total = precio_unitario * cantidad_stock

print(f'Nombre del producto: {producto} \nCantidad de stock: {cantidad_stock} \nValor total: ${total: .2f} \n¿El total sobrepasa los $100.000?: {bool(total>100000)}')




