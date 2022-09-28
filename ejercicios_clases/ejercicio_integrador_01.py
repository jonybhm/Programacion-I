"""
La división de higiene está trabajando en un 
control de stock para productos sanitarios. 
Debemos realizar la carga de 5 (cinco) productos 
prevención de contagio, de cada una debe obtener 
los siguientes datos:
El tipo (validar "barbijo", "jabón" o "alcohol")
El precio: (validar entre 100 y 300)
La cantidad de unidades ( no puede ser 0 ni negativo 
y no debe superar las 1000 unidades)
La marca y el Fabricante.

Se debe informar lo siguiente:
Del más caro de los barbijos, 
la cantidad de unidades y el fabricante.
Del ítem con más unidades, el fabricante.
Cuántas unidades de jabones hay en total.
"""

primer_valor_ingresado = True
acumulador_jabon=0

for i in range(2):
    
    tipo = input("Ingrese el tipo\n")
    while(tipo != "jabon" and tipo != "barbijo" 
    and tipo != "alcohol"):
        tipo = input("INgrese un tipo valido\n")

    precio = input("ingrese un precio\n")
    precio=float(precio)
    while(precio<100 or precio >300):
        precio = input("ingrese un precio valido\n")
        precio = float(precio)

    cantidad = input("ingrese una cantidad\n")
    cantidad=int(cantidad)
    while(cantidad<=0):
        cantidad = input("Ingrese un cantidad valida\n")
        cantidad = int(cantidad) 
    
    marca = input("ingrese la marca\n")
    fabricante = input("ingrese un fabricante\n")
    
    if(primer_valor_ingresado):
        barbijo_mas_caro = precio
        cantidad_barbijo_mas_caro = cantidad
        fabricante_barbijo_mas_caro = fabricante

        cantidad_fabricante_con_mas_unidades = cantidad
        fabricante_con_mas_unidades = fabricante

        primer_valor_ingresado = False
        if(barbijo_mas_caro < precio):
            barbijo_mas_caro = precio
            cantidad_barbijo_mas_caro = cantidad
            fabricante_barbijo_mas_caro = fabricante

        elif(cantidad_fabricante_con_mas_unidades < cantidad):
            cantidad_fabricante_con_mas_unidades = cantidad
            fabricante_con_mas_unidades = fabricante
    
    
    if(tipo == "jabon"):
        acumulador_jabon = acumulador_jabon+cantidad
   
print("El barbijo mas caro es {} y la cantidad es {}\n".format(fabricante_barbijo_mas_caro,cantidad_barbijo_mas_caro))
print("El fabricante del item con mas unidades es {}\n".format(fabricante_con_mas_unidades))
print("La cantidad total de jabones es {}\n".format(acumulador_jabon))


