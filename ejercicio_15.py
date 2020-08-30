
#En base al ejercicio #14 crear el código Python necesario para guardar la salida de ese ejercicio en un fichero
#de texto.
#Se debe mostrar en pantalla la salida del ejercicio #14 más:
#- Se ha guardado la lista en el fichero: nombre.txt
#Si necesitas ayuda con el manejo de ficheros recuerda repasar el material de la clase extra #2, al igual que
#este repositorio donde hace unos años realice un ejemplo del manejo de ficheros con una clase bien sencilla de
#implementar.
#Enlace directo: https://github.com/cjgarcia/archpy

import json
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


print('esta es nuesta lista de compras:', len(lista_compras))
print('articulos unicos:', len(set([articulo['nombre'] for articulo in lista_compras])))
print('articulo mas costoso es:', max([articulo['precio'] for articulo in lista_compras]))
print('articulo mas economico es:', min([articulo['precio'] for articulo in lista_compras]))

Archivo_json = open("prueba.json", "a+")

str_json = json.dumps(lista_compras, indent=4)

Archivo_json.write(str_json)

Archivo_json.close()

print("Se ha guardado la lista en el fichero: prueba.json")