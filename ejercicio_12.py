
lista_compras = []

while True:
    articulos_input = input("introduce los articulos:")
    
    if articulos_input == "parar":
            break

    else:
            articulo = {}
            articulo['nombre'] = articulos_input
            articulo['cantidad'] = float(input("introduce la cantidad:"))
            articulo['precio'] = float(input("introduce el precio:"))
            articulo['montoxpagar'] = articulo['cantidad'] * articulo['precio']
            lista_compras.append(articulo)

print("nombre", "Cantidad","Precio", "Monto a Pagar", sep='|\t')

for articulo in lista_compras:
        print(articulo['nombre'], articulo['cantidad'], articulo['precio'], articulo['montoxpagar'], sep='|\t')
