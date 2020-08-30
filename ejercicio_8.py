#Modificar el ejercicio #7 para obtener el número de elementos únicos en la lista de compras. Por ejemplo: Si
#agrego dos veces “arroz”, solo me debería contar uno.
#Para agregar un ítem a la lista solo basta agregar su nombre.
#Al final solo se requiere que se muestre:
#- El número total de ítems agregados a la lista de compras.
#- El número de ítems únicos agregados a la lista de compras.





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
print('articulos unicos:', len(set(lista_compras)))