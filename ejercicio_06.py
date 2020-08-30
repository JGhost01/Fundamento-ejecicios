#Crear el código Python necesario para obtener el hostname de una URL.


url = 'uasdvirtual.uasd.eud.do/diplomados/my'

obtener_hostname = url.strip().split('/')

hostname = obtener_hostname[:1]

print('hostname:', hostname)