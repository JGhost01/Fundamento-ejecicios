#Modificar el ejercicio #9 para obtener el monto a pagar por cada ítem de la lista de compras.
#Para agregar un ítem a la lista se deberá agregar:
#- Nombre del ítem.
#- Cantidad.
#- Precio.
#- El monto a pagar será igual a la [cantidad] * [precio] de cada ítem.
#Al final solo se requiere que se muestre:
#- El número total de ítems agregados a la lista de compras.
#- El número de ítems únicos agregados a la lista de compras.


lista_compras = []
cantidad = []
precio = []
i=0
while 1:
    i+=1
    articulos = input("introduce los articulos:")

    if articulos == "parar":
            break
    else:
        lista_compras.append(articulos)
    
    cantidad_it = int(input("introduce la cantidad:"))
    precio_it = int(input("introduce el precio:"))
    
    cantidad.append(cantidad_it)
    precio.append(precio_it)

    combi = zip(cantidad, precio)
    list3 = list()

    for n in combi:
        list1 = n[0]
        list2 = n[1]
        resultado = list1 * list2
        list3.append(resultado)

print('Esta es nuestra cantidad de items:', len(lista_compras))
print('articulos unicos:', len(set(lista_compras)))