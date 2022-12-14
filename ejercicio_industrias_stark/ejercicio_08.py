'''Desafío #02: (con biblioteca propia: stark_biblioteca)
En base a lo resuelto en el desafío #00, deberás mejorar la calidad de 
tus funciones. Es por ello que te proponemos lo siguiente:
IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas 
escribiendo que es lo que hacen, que son los parámetros que reciben 
(si es una lista, un string, etc y que contendrá) y que es lo que retorna la función!
'''


from data_stark import lista_personajes
'''{
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  }'''

'''Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista de héroes. 
La función deberá:
Recorrer la lista y convertir al tipo de dato correcto las keys 
(solo con las keys que representan datos numéricos)
Validar primero que el tipo de dato no sea del tipo al cual será casteado. 
Por ejemplo si una key debería ser entero (ejemplo edad) verificar antes que no se encuentre ya en ese tipo de dato.
Si al menos un dato fue modificado, la función deberá imprimir como mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.
Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”'''

def stark_normalizar_datos (lista_heroes:list)->list:
    '''
    Castea los datos a sus tipos correspondietes
    Recibe la lista de datos 
    Devuelve la misma lista con datos casteados
    '''
    if (len(lista_heroes)>0):
        flag = False
        for personaje in lista_heroes:
            if (personaje["altura"]!=float()):
                personaje["altura"] = float(personaje["altura"])
                flag = True
            if (personaje["peso"]!=float()):
                personaje["peso"] = float(personaje["peso"])
                flag = True
            if (personaje["fuerza"]!=int()):
                personaje["fuerza"] = int(personaje["fuerza"])
                flag = True
    else:
        print("la lista esta vacia")

    if(flag==True):
        print("datos normalizados")
       
    lista_con_datos_casteados = lista_heroes 
    #print (type(lista_con_datos_casteados[0]["altura"]))   
    return lista_con_datos_casteados

'''
Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario 
el cual representara a un héroe y devolverá un string el cual contenga su nombre formateado de la siguiente manera: 
Nombre: Howard the Duck
'''

def obtener_nombre (dic_heroe:dict)->str:
    nombre_heroe = "Nombre: {0}".format(dic_heroe["nombre"])
    
    '''
    Transforma el value de la clave "nombre" a un str 
    Recibe el diccionario que se encuentra dentro de la lista
    Devuelve un str con el formato "Nombre: ..."
    '''
    
    return nombre_heroe

'''
Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y 
deberá imprimirlo en la consola. La función no tendrá retorno.
'''

def imprimir_dato (dato:str):
    print (dato)

'''
Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por 
parámetro la lista de héroes y deberá imprimirla en la consola. 
Reutilizar las funciones hechas en los puntos 1.1 y 1.2. 
Validar que la lista no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
Con este se resuelve el Ej 1 del desafío #00
'''

def stark_imprimir_nombres_heroes (lista_heroes:list):
    
    for personaje in lista_heroes:
        imprimir_dato(obtener_nombre(personaje))

'''
Crear la función 'obtener_nombre_y_dato' la misma recibirá por 
parámetro un diccionario el cual representara a un héroe y una key 
(string) la cual representará el dato que se desea obtener. 

La función deberá devolver un string el cual contenga el nombre y dato (key)
del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.

El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza)
Nombre: Venom | fuerza: 500
'''

def obtener_nombre_y_dato (hero:dict,clave:str)->str:
    '''
    Obtiene el nombre y dato del personaje
    Recibe un diccionario y la clave que quiero obtener
    Devuelve un str con el formato "Nombre: ... | Dato: ..."
    '''
    nombre_y_dato = "Nombre: {0} | {1}: {2}".format(hero["nombre"],clave,hero[clave])
    return nombre_y_dato

#print(obtener_nombre_y_dato(lista_personajes[0],"fuerza"))

'''
Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá 
por parámetro la lista de héroes, la cual deberá iterar e imprimir su nombre y 
altura USANDO la función creada en el punto 2. Validar que la lista de héroes 
no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
Con este se resuelve el Ej 2 del desafío #00
'''

def stark_imprimir_nombres_alturas (lista_heroes:list):
  if (len(lista_heroes) > 0):
    for personaje in lista_heroes:
      imprimir_dato(obtener_nombre_y_dato(personaje,"altura"))
  else:
    print("-1")


'''
Crear la función 'calcular_max' la cual recibirá por parámetro la lista de héroes
y una key (string) la cual representará el dato que deberá ser evaluado a efectos 
de determinar cuál es el máximo de la lista. Por ejemplo la función deberá poder 
calcular: el peso, la altura o fuerza máximas y retornar el héroe que tenga el dato más alto.
Ejemplo de llamada:
calcular_max(lista, 'edad')
'''

def calcular_max(lista_heroes:list,caracteristica:str)->dict:
    '''
    Calcula el maximo de una caracteristica determinada
    Recibe la lista importada y un str que representa la caracteristica
    Devuelve un dic con el hero con el maximo de esa caracteristica
    '''
    lista_heroes[0][caracteristica] = float(lista_heroes[0][caracteristica])
    dic_heroe_con_caracteristica_maximo = {"nombre":lista_heroes[0]["nombre"],caracteristica:lista_heroes[0][caracteristica]}

    for personaje in lista_heroes:
        personaje[caracteristica] = float (personaje[caracteristica])
        if (personaje[caracteristica]>dic_heroe_con_caracteristica_maximo[caracteristica]):
            dic_heroe_con_caracteristica_maximo = {"nombre":personaje["nombre"],caracteristica:personaje[caracteristica]}
    
    return dic_heroe_con_caracteristica_maximo

'''
Crear la función 'calcular_min' la cual recibirá por parámetro la lista de héroes y una 
key (string) la cual representará el dato que deberá ser evaluado a efectos de determinar
cuál es el mínimo de la lista. Por ejemplo la función deberá poder calcular: el peso, 
la altura o fuerza máximas y retornar el héroe que tenga el dato más bajo. 
Ejemplo de llamada:
calcular_min(lista, 'edad')
'''

def calcular_min(lista_heroes:list,caracteristica:str)->dict:
    '''
    Calcula el minimo de una caracteristica determinada
    Recibe la lista importada y un str que representa la caracteristica
    Devuelve un dic con el hero con el minimo de esa caracteristica
    '''
    lista_heroes[0][caracteristica] = float(lista_heroes[0][caracteristica])
    dic_heroe_con_caracteristica_minimo = {"nombre":lista_heroes[0]["nombre"],caracteristica:lista_heroes[0][caracteristica]}

    for personaje in lista_heroes:
        personaje[caracteristica] = float (personaje[caracteristica])
        if (personaje[caracteristica]<dic_heroe_con_caracteristica_minimo[caracteristica]):
            dic_heroe_con_caracteristica_minimo = {"nombre":personaje["nombre"],caracteristica:personaje[caracteristica]}
    
    return dic_heroe_con_caracteristica_minimo

'''
Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:

La lista de héroes
El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
La función deberá retornar el héroe que cumpla con la condición pedida. Reutilizar las funciones hechas en los puntos 4.1 y 4.2
Ejemplo de llamada:
calcular_max_min_dato(lista, "maximo", "edad")
'''

def calcular_max_min_dato(lista_heroes:list,tipo_calculo:str,caracteristica:str)->dict:
    '''
    Calcula el maximo o minimo de cualquier caracteristica
    Recibe la lista importada y dos str que indican el tipo de calculo y la caracteristica a calcular
    Devuelve un diccionario con los datos del heroe    
    '''
    if (tipo_calculo == "maximo"):
        heroe_maximo_o_minimo = calcular_max(lista_heroes,caracteristica)
    elif (tipo_calculo == "minimo"):
        heroe_maximo_o_minimo = calcular_min(lista_heroes,caracteristica)
    
    return heroe_maximo_o_minimo

'''
Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres parámetros: 
La lista de héroes
El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
Con este se resuelve el Ej 3, Ej 4, Ej 6 y Ej 7 del desafío #00

La función deberá obtener el héroe que cumpla dichas condiciones, imprimir su nombre y el valor calculado. 
Reutilizar las funciones de los puntos:
punto 1.2, punto: 2, punto 4.1, punto 4.2 y punto 4.3 
Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
Ejemplo de llamada:
     stark_calcular_imprimir_heroe (lista, "maximo", "edad")
            Ejemplo de salida:
    Mayor altura: Nombre: Howard the Duck | altura: 79.34
'''

def stark_calcular_imprimir_heroe (lista_heroes:list,tipo_calculo:str,caracteristica:str):
    '''
    Calcula e imprime al heroe con los datos
    Recibe la lista importada y dos str del tipo de calculo y la caracteristica
    '''
    if (len(lista_heroes)>0):
        if(tipo_calculo == "maximo"):
            mensaje = "Mayor {2}: Nombre: {0} | altura: {1}".format(calcular_max_min_dato(lista_heroes,tipo_calculo,caracteristica)["nombre"],
            calcular_max_min_dato(lista_heroes,tipo_calculo,caracteristica)[caracteristica],caracteristica)
            imprimir_dato(mensaje)

        elif (tipo_calculo == "minimo"):
            mensaje = "Menor {2}: Nombre: {0} | altura: {1}".format(calcular_max_min_dato(lista_heroes,tipo_calculo,caracteristica)["nombre"],
            calcular_max_min_dato(lista_heroes,tipo_calculo,caracteristica)[caracteristica],caracteristica)
            imprimir_dato(mensaje)
    else:
        print("-1")


'''
Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de héroes y un 
string que representara el dato/key de los héroes que se requiere sumar. Validar que cada héroe 
sea tipo diccionario y que no sea un diccionario vacío antes de hacer la suma. La función deberá 
retorna la suma de todos los datos según la key pasada por parámetro
'''

def sumar_dato_heroe(lista_heroes:list,caracteristica:str):

    suma = float(lista_heroes[0][caracteristica])

    for personaje in lista_heroes:
        if(type(personaje)==type({}) and len(personaje)>0):
            suma += float(personaje[caracteristica])

    return suma

'''
Crear la función  ‘dividir’ la cual recibirá como parámetro dos números (dividendo y divisor). 
Se debe verificar si el divisor es 0,  en caso de serlo, retornar 0, caso contrario realizar 
la división entre los parámetros y retornar el resultado
'''

def dividir (dividendo:float,divisor:float)->float:
    division = 0

    if(divisor != 0):
        division = dividendo / divisor
       
    return division

'''    
Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de héroes
y un string que representa el dato del héroe que se requiere calcular el promedio. 
La función debe retornar el promedio del dato pasado por parámetro

IMPORTANTE: hacer uso de las las funciones creadas en los puntos 5.1 y 5.2
'''

def calcular_promedio(lista_heroes:list,caracteristica:str)->float:
    contador_heroes = 0
    for personaje in lista_heroes:
        contador_heroes += 1

    promedio = dividir(sumar_dato_heroe(lista_heroes,caracteristica),contador_heroes)

    return promedio

'''
Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá una lista de héroes 
y utilizando la función del punto 5.3 calcula y mostrará la altura promedio. Validar que la 
lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y 5.3
Con este se resuelve el Ej 5 del desafío #00
'''

def stark_calcular_imprimir_promedio_altura(lista_heroes:list,caracteristica:str):
    if (len(lista_heroes) > 0):
        imprimir_dato(calcular_promedio(lista_heroes,caracteristica))
    else:
        print("-1")

'''
Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla, el cual 
permite utilizar toda la funcionalidad ya programada. Se deberá reutilizar la función 
antes creada encargada de imprimir un string (1.2)
'''
def imprimir_menu():
    mensaje = "\n1-Listar heroes \n2-Mostrar heroe mas alto"
    mensaje += "\n3-Mostrar heroe mas bajo\n4-Mostrar heroe mas pesado"
    mensaje += "\n5-Mostrar heroe mas liviano\n6-Mostrar promedio de altura"
    mensaje += "\n7-Salir\n> "
    
    return mensaje

'''
Crear la función “validar_entero” la cual recibirá por parámetro un string de número el
cual deberá verificar que sea sea un string conformado únicamente por dígitos.
Retornara True en caso de serlo, False caso contrario
'''
def validar_entero(numero:str)->bool:

    flag = False
    if(numero.isdigit):
        flag = True
    
    return flag

'''
Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú de opciones 
y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. 
En caso de ser correcto dicho número, lo retornara casteado a entero, caso contrario retorna -1. 
Reutilizar las funciones del ejercicio 6.1 y 6.2
'''

def stark_menu_principal():
    respuesta = input(imprimir_menu())
    while (validar_entero(respuesta)==False):
        print("Ingrese un numero valido")
        respuesta = input(imprimir_menu())
    return respuesta

'''
Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y 
se encargará de la ejecución principal de nuestro programa. 
Utilizar if/elif o match según prefiera (match solo para los que cuentan con python 3.10+). 
Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. 
Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.
'''

def stark_marvel_app():
    while (True):
        if(stark_menu_principal() == "1"):
            stark_imprimir_nombres_heroes(lista_personajes)
        elif(stark_menu_principal() == "2"):
            stark_calcular_imprimir_heroe(lista_personajes,"maximo","altura")
        elif(stark_menu_principal() == "3"):
            stark_calcular_imprimir_heroe(lista_personajes,"minimo","altura")
        elif(stark_menu_principal() == "4"):
            stark_calcular_imprimir_heroe(lista_personajes,"maximo","peso")
        elif(stark_menu_principal() == "5"):
            stark_calcular_imprimir_heroe(lista_personajes,"minimo","peso")
        elif(stark_menu_principal() == "6"):
            stark_calcular_imprimir_promedio_altura(lista_personajes,"altura")
        elif(stark_menu_principal() == "7"):
            break

stark_marvel_app()

