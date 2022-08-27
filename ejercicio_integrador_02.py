"""
Ejercicio Integrador 02

La división de alimentos está trabajando en un pequeño software para 
cargar las compras de ingredientes para la cocina de Industrias Wayne. 
Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
PESO: (entre 10 y 100 kilos)
PRECIO POR KILO: (mayor a 0 [cero]).
TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de 
descuento sobre el precio bruto. o si compro más de 300 kilos en total, 
tenes 25% de descuento sobre el precio bruto.
El importe total a pagar, BRUTO sin descuento.
El importe total a pagar con descuento (Solo si corresponde).
Informar el tipo de alimento más caro.
El promedio de precio por kilo en total.
"""
acumulador_peso = 0
acumulador_precio = 0
primer_alimento_ingresado = True
while(True):

    peso = input("Ingrese el peso de la comida en kg\n")
    peso = int(peso)
    while(peso<10 or peso>100):
        peso = input("Ingrese un peso valido\n")
        peso = int(peso)


    precio_por_kilo = input("Ingrese el precio por kilo\n")
    precio_por_kilo = int(precio_por_kilo)
    while(precio_por_kilo<0):
        precio_por_kilo = input("Ingrese un precio por kilo valido\n")
        precio_por_kilo = int(precio_por_kilo)


    tipo = input("Ingrese el tipo de comida (v, a, m);(vegetal, animal, mezcla)\n")
    while(tipo!="v" and tipo!="a" and tipo!="m"):
        tipo = input("Ingrese un tipo valido\n")

    acumulador_peso = acumulador_peso+peso
    acumulador_precio = acumulador_precio+precio_por_kilo*peso

    if(primer_alimento_ingresado):
        precio_alimento_mas_caro = precio_por_kilo
        tipo_alimento_mas_caro = tipo
        primer_alimento_ingresado = False
    elif(precio_alimento_mas_caro<precio_por_kilo):
        precio_alimento_mas_caro = precio_por_kilo
        tipo_alimento_mas_caro = tipo

    rta = input("Desea salir? s/n \n")
    if(rta == 's'):
        break

if(acumulador_peso>300):
    descuento = 0.25
elif(acumulador_peso<=300 and acumulador_peso>=100 ):
    descuento = 0.15
else:
    descuento = 0

promedio_precio_por_kilo = acumulador_precio/acumulador_peso
    
print("El importe total a pagar, BRUTO sin descuento es: ${}\n".format(acumulador_precio))
if(acumulador_peso>=100):
    precio_con_descuento = acumulador_precio-acumulador_precio-descuento
    print("El importe total a pagar con descuento es: ${}\n".format(precio_con_descuento))
print("El tipo de alimento más caro es: {}\n".format(tipo_alimento_mas_caro))
print("El promedio de precio por kilo en total es: ${}\n".format(promedio_precio_por_kilo))