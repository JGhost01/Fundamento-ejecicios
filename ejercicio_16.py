import json

data_reco = open('prueba.json').read()
prueba_json = json.loads(data_reco)


def buscar(nombre):
    item_en = None

    for articulos in prueba_json:
        if articulos['nombre'].lower() == nombre.lower():
            item_en = articulos
    return item_en

def agregar(**datos):
    datos['montoxpagar'] = datos['cantidad'] * datos['precio']
    prueba_json.append(datos)
    pass

def eliminar():
    for i in range((len(prueba_json) - 1)):
        if prueba_json[i]['nombre'].lower() == nombre.lower():
            del prueba_json[i]
    pass

def guardar():
    fichero_json = open('prueba.json', 'w')
    str_json = json.dumps(prueba_json, indent=4)
    fichero_json.write(str_json)
    fichero_json.close()

def mostrar_canasta():
    for item in prueba_json:
        print(item)

# agregar(nombre='Pizza congelada', cantidad=2, precio=300)
# print("Se ha agregado un nuevo item a la lista")
# mostrar_canasta()


#eliminar('papa')
#print("Se ha eliminado un item a la lista")

# mostrar_canasta()
#articulos = buscar('peras')

#if articulos:
 #   print(articulos)
#else:
 #   print("no encontrado")

agregar(nombre = 'queso', cantidad = 1, precio = 10)

guardar()
print("Se han guardado los cambios!")

