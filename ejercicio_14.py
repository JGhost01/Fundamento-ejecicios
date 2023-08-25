#Modificar el ejercicio #13 para obtener el ítem con menor costo (costo a pagar).
#Se debe mostrar en pantalla la salida del ejercicio #13 más:
#- El producto más económico es: “producto x”


lista_compras = []

while True:
    articulos_input = input("introduce los articulos deseados:")
    
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


print('esta es nuesta lista de compras:', len(lista_compras))
print('articulos unicos:', len(set([articulo['nombre'] for articulo in lista_compras])))
print('articulo mas costoso es:', max([articulo['precio'] for articulo in lista_compras]))
print('articulo mas economico es:', min([articulo['precio'] for articulo in lista_compras]))