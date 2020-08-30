#Crear el código Python necesario para guardar una lista sencilla de compras. La lista debe ser interactiva,
#recibir por pantalla los ítem de la lista de compra hasta que el usuario entre el str “parar”. Al final de la corrida, el
#script debe mostrar el total de ítems agregados a la lista.

#Para agregar un ítem a la lista solo basta agregar su nombre.
#Al final solo se requiere que se muestre el número total de ítems agregados a la lista de compras


lista_compras = []
i=0
while 1:
    i+=1
    articulos = input("introduce los articulos:")
    if articulos == "parar":
            break
    else:
        lista_compras.append(articulos)

print('Esta es nuestra cantidad de items:', len(lista_compras))
