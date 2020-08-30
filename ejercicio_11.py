#Modificar el ejercicio #10 para evitar que se pueda agregar un ítem con el mismo nombre a la lista de
#compras.

lista_compras = []
cantidad = []
precio = []
ojos = set()
i=0
while 1:
    i+=1
    articulos = input("introduce los articulos:")
    
    if articulos == "parar":
            break
    if articulos not in ojos:
            ojos.add(articulos)
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

print('esta es nuesta lista de compras:', lista_compras)
print('Esta es nuestra cantidad de items:', len(lista_compras))
print('articulos unicos:', len(set(lista_compras)))