
lista_nombres = []
while True:
    nombre = input("Nombre? : ")
    lista_nombres.append(nombre)
    rta = input("Para salir pulse (s)")
    if(rta == 's'):
        break

for nombre in lista_nombres:
    print(nombre)