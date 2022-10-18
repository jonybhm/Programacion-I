import copy
lista_precios = {
    
    "banana" : {
        "precio" : 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40        
    },
    
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100        
    }, 
    
    "mango" : {
        "precio": 300,
        "unidad_medida": "unidad",
        "stock": 100  
    }

}

# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios' en caso de existir mostrar precio y el stock. 
# En caso de no existir el producto mostrar el mensaje 'el articulo no se encuentra en la lista'

# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el precio total (precio * cantidad)

# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, unidad de medida y stock. Agregar la nueva fruta a la lista de precios

# Punto 4: imprimir el listado de frutas (solo su nombre)

# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir eliminarla. En caso de que el producto no exista mostrar 
# el mensaje 'el articulo no se encuentra en la lista'

while(True):
    lista_precios_copia = copy.deepcopy(lista_precios)

    producto_respuesta = input("\nelija un producto:\n>")
    mensaje_error = 'el articulo no se encuentra en la lista'
    diccionario_respuesta = lista_precios_copia.get(producto_respuesta.lower(),mensaje_error)
    if(diccionario_respuesta != mensaje_error):
        print("-precio: ${0}".format(diccionario_respuesta.get("precio")))
        print("-stock: {0} unidades".format(diccionario_respuesta.get("stock")))
        cantidad_respuesta = input("ingrese la cantidad a llevar:\n>")
        precio_total = diccionario_respuesta.get("precio") * int(cantidad_respuesta)
        print("-precio total: ${0}".format(precio_total))
    else:
        print(mensaje_error)

    producto_usuario = input("\nIngrese un nuevo producto para agregar a la lista:\n>")
    precio_usuario = input("Precio unitario:\n>")
    unidad_medida_usuario = input("Unidad medida:\n>")
    stock_usuario = input("Stock:\n>")
    dic_nuevo_producto = {producto_usuario:{"precio":float(precio_usuario),"unidad_medida":unidad_medida_usuario,"stock":int(stock_usuario)}}

    lista_precios_copia.update(dic_nuevo_producto)

    print("\nlista productos actualizada:\n")
    for producto in lista_precios_copia:
        print(producto)

    eliminar_fruta_usuario = input("\nIndique un producto a eliminar:\n>")
    producto_eliminado = lista_precios_copia.pop(eliminar_fruta_usuario,mensaje_error)
    if (producto_eliminado != mensaje_error):
        print ("\nse ha eliminado un producto de la lista.\nLista actualizada:\n")
        for producto in lista_precios_copia:
            print(producto)
    else:
        print(mensaje_error)

    salir_usuario = input("\nDesea continuar? s/n\n>")
    if (salir_usuario == "n"):
        break     