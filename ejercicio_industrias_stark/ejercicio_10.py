import re
import json
from ejercicio_07 import * 
from data_stark import lista_personajes


def sumar_dato_heroe(lista_heroes:list,caracteristica:str):

    suma = float(lista_heroes[0][caracteristica])

    for personaje in lista_heroes:
        if(type(personaje)==type(dict()) and len(personaje)>0):
            suma += float(personaje[caracteristica])

    return suma

def calcular_min(lista_heroes:list,caracteristica:str)->dict:
    '''
    Calcula el minimo de una caracteristica determinada
    Recibe la lista importada y un str que representa la caracteristica
    Devuelve un dic con el hero con el minimo de esa caracteristica
    '''
    lista_heroes[0][caracteristica] = float(lista_heroes[0][caracteristica])
    dic_heroe_con_caracteristica_minimo = lista_heroes[0]

    for personaje in lista_heroes:
        personaje[caracteristica] = float (personaje[caracteristica])
        if (personaje[caracteristica]<dic_heroe_con_caracteristica_minimo[caracteristica]):
            dic_heroe_con_caracteristica_minimo = personaje
    
    return dic_heroe_con_caracteristica_minimo

def calcular_max(lista_heroes:list,caracteristica:str)->dict:
    '''
    Calcula el maximo de una caracteristica determinada
    Recibe la lista importada y un str que representa la caracteristica
    Devuelve un dic con el hero con el maximo de esa caracteristica
    '''
    lista_heroes[0][caracteristica] = float(lista_heroes[0][caracteristica])
    dic_heroe_con_caracteristica_maximo = lista_heroes[0]

    for personaje in lista_heroes:
        personaje[caracteristica] = float (personaje[caracteristica])
        if (personaje[caracteristica]>dic_heroe_con_caracteristica_maximo[caracteristica]):
            dic_heroe_con_caracteristica_maximo = personaje
    
    return dic_heroe_con_caracteristica_maximo

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


def leer_archivo(archivo_extension:str)->dict:
    dic_json = {}
    with open (archivo_extension,"r") as archivo:
        dic_json = json.load(archivo)
    return dic_json["heroes"]

#data_stark = leer_archivo(r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\ejercicio_archivos\data_stark.json")
#stark_menu_principal_desafio_5(data_stark)
#C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\ejercicio_archivos\data_stark.json

def guardar_archivo (archivo_extension:str,lista_con_contenido:list)->bool:
    with open(archivo_extension,"w") as archivo:
        for contenido in lista_con_contenido:
            linea_archivo = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}\n".format(contenido["nombre"]            
            ,contenido["identidad"],contenido["empresa"],contenido["altura"],contenido["peso"]
            ,contenido["genero"],contenido["color_ojos"],contenido["color_pelo"],contenido["fuerza"],contenido["inteligencia"])
            archivo.write(linea_archivo)
            
        
#guardar_archivo(r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\ejercicio_archivos\data_stark_2.csv",lista_personajes)


'''
 Crear la función 'capitalizar_palabras' la cual recibirá por parámetro un
string que puede contener una o muchas palabras. La función deberá
retornar dicho string en el cual todas y cada una de las palabras que
contenga, deberán estar capitalizadas (Primera letra en mayúscula).
'''

def capitalizar_palabra(patron:str):
    patron_capitalized = patron.capitalize()
    return patron_capitalized

#print(capitalizar_palabra("hola mi nombre"))

def parse_csv(nombre_archivo:str)->list:
    lista_rta = []
    archivo = open(nombre_archivo,"r")
    for linea in archivo:
        lista = linea.splir(",")
        video = {}
        video["title"] = lista[0]
        video["views"] = lista[1]
        video["length"] = lista[2]
        video["url"] = lista[3]
        video["date"] = lista[4]
        lista_rta.append(video)
    archivo.close()
    return lista_rta
    

'''
Crear la función 'obtener_nombre_capitalizado' la cual recibirá por
parámetro un diccionario el cual representará a un héroe y devolverá
un string el cual contenga su nombre formateado de la siguiente
manera:
Nombre: Venom
Reutilizar 'capitalizar_palabras
'''

def obtener_nombre_capitalizado(heroe:dict)->str:
    '''
    La funcion capitaliza un nombre
    Recibe un diccionario que representa la info del heroe
    Devuelve un str con le nombre capitalizado
    '''
    nombre = heroe["nombre"]
    nombre_capitalizado = nombre.capitalize()
    return nombre_capitalizado

#print(obtener_nombre_capitalizado(lista_personajes[0]))

'''
Crear la función 'obtener_nombre_y_dato' la cual recibirá por
parámetro un diccionario el cual representará a un héroe y una key
(string) la cual representará la key del héroe a imprimir. La función
devolverá un string el cual contenga el nombre y dato (key) del héroe a
imprimir.
El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.
El string resultante debe estar formateado al estilo: (suponiendo que la
key es fuerza)
Nombre: Venom | Fuerza: 500
Reutilizar 'obtener_nombre_capitalizado'
'''

def obtener_nombre_y_dato(heroe:dict,clave:str)->str:
    '''
    La funcion devuelve el nombre y dato especifico
    Recive un dict que representa al heroe y un str que representa la clave
    Devuelve un str con el nombre y clave
    '''
    nombre = obtener_nombre_capitalizado(heroe)
    nombre_y_dato = "Nombre: {0} | {1}: {2}".format(nombre,clave,heroe[clave])
    return nombre_y_dato

#print (obtener_nombre_y_dato(lista_personajes[0],"color_pelo"))

'''
Crear la función 'es_genero' la cual recibirá por parámetro un
diccionario que representará un héroe y un string el cual será usado
para evaluar si el héroe coincide con el género buscado (El string
puede ser M, F o NB). retornará True en caso de que cumpla, False
caso contrario.
'''    

def es_genero(heroe:dict,patron_genero:str)->bool:
    genero_coincide = False
    genero_match = re.search(patron_genero,heroe["genero"])
    if (genero_match):
        genero_coincide = True

    return genero_coincide

#print(es_genero(lista_personajes[0],"M")) 

'''
Crear la función 'stark_guardar_heroe_genero' la cual recibira por
parámetro la lista de héroes y un string el cual representará el género
a evaluar (puede ser M o F). Deberá imprimir solamente los héroes o
heroínas que coincidan con el género pasado por parámetro y
además, deberá guardar dichos nombres en un archivo con extensión
csv (cada nombre deberá ir separado por una coma)
Reutilizar las funciones 'es_genero', 'obtener_nombre_capitalizado',
'imprimir_dato' y 'guardar_archivo'.
En el caso de 'guardar_archivo', cuando se llame a esta función el
nombre de archivo a guardar deberá respetar el formato:
heroes_M.csv, heroes_F.csv o heroes_NB según corresponda.
La función retornará True si pudo guardar el archivo, False caso
contrario.
'''

def stark_guardar_heroe_genero(lista_heroes:list,genero:str,direccion_archivo:str):
    print ("\n{0}".format(genero))
    lista_heroes_cuyo_genero_coincide = []
    for heroe in lista_heroes:        
        if (es_genero(heroe,genero) == True):
            lista_heroes_cuyo_genero_coincide.append(heroe)
            print("{0},".format(heroe["nombre"]))
    guardar_archivo(direccion_archivo,lista_heroes_cuyo_genero_coincide)

    return lista_heroes_cuyo_genero_coincide

#stark_guardar_heroe_genero(lista_personajes,"F",
#r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\ejercicio_industrias_stark\archivo_datos_genero.csv")

'''
Basandote en la función 'calcular_min', crear la función
'calcular_min_genero' la cual recibirá como parámetro extra un string
que representa el género de la heroína/héroe a buscar. modificar un
poco la lógica para que dentro no se traiga por defecto al primer héroe
de la lista sino que mediante un flag, se traiga el primer héroe que
COINCIDA con el género pasado por parámetro. A partir de allí, podrá
empezar a comparar entre héroes o heroínas que coincidan con el
género pasado por parámetro. La función retornará el héroe o heroína
que cumpla la condición de tener el mínimo (peso, altura u otro dato)
'''


def calcular_min_genero (lista_heroes:list,caracteristica:str,genero:str)->dict:
    lista_heroes_mismo_genero = []
    dic_heroe_min_genero ={}
    for heroe in lista_heroes:
        if (es_genero(heroe,genero) == True):
            lista_heroes_mismo_genero.append(heroe)
    
    dic_heroe_min_genero = calcular_min(lista_heroes_mismo_genero,caracteristica)
    return dic_heroe_min_genero

#print(calcular_min_genero(lista_personajes,"peso","F"))

'''
Basandote en la funcion 'calcular_max_min_dato', crear una funcion
con la misma lógica la cual reciba un parámetro string que
representará el género del héroe/heroína a buscar y renombrarla a
'calcular_max_min_dato_genero'. La estructura será similar a la ya
antes creada, salvo que dentro de ella deberá llamar a
'calcular_max_genero' y 'calcular_min_genero', pasandoles el nuevo
parámetro. Esta función retornará el héroe o heroína que cumpla con
las condiciones pasados por parámetro. Por ejemplo, si se le pasa 'F' y
'minimo', retornará la heroína que tenga el mínimo (altura, peso u otro
dato)
'''
def calcular_max_min_dato (lista_heroes:list,caracteristica:str,genero:str,tipo_busqueda:str)->dict:
    lista_heroes_mismo_genero = []
    dic_heroe_min_genero ={}
    for heroe in lista_heroes:
        if (es_genero(heroe,genero) == True):
            lista_heroes_mismo_genero.append(heroe)
    if (tipo_busqueda == "minimo"):
        dic_heroe_min_genero = calcular_min(lista_heroes_mismo_genero,caracteristica)
    elif(tipo_busqueda == "maximo"):
        dic_heroe_min_genero = calcular_max(lista_heroes_mismo_genero,caracteristica)

    return dic_heroe_min_genero

#print(calcular_max_min_dato(lista_personajes,"peso","M","maximo"))

'''
Basandote en la función 'stark_calcular_imprimir_heroe' crear la
función ‘stark_calcular_imprimir_guardar_heroe_genero’ que además
reciba un string el cual representará el género a evaluar. El formato de
mensaje a imprimir deberá ser estilo:
Mayor Altura: Nombre: Gamora | Altura: 183.65
Además la función deberá guardar en un archivo csv el resultado
obtenido.
Reutilizar: 'calcular_max_min_dato_genero', 'obtener_nombre_y_dato',
'imprimir_dato' y 'guardar_archivo'.
En el caso de 'guardar_archivo' el nombre del archivo debe respetar el
formato:
heroes_calculo_key_genero.csv
Donde:
● cálculo: representará el string máximo o mínimo
● key: representará cual es la key la cual se tiene que hacer el
cálculo
● genero: representará el género a calcular.
Ejemplo: para calcular el héroe más alto femenino, el archivo se
deberá llamar:
heroes_maximo_altura_F.csv
Esta función retornará True si pudo guardar el archivo, False caso
contrario
'''

def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes:list
,genero:str,caracteristica:str,tipo_calculo:str,direccion_archivo_primer_parte:str):
    lista = []
    if (len(lista_heroes)>0):
        if(tipo_calculo == "maximo"):
            mensaje = "Mayor {2}: Nombre: {0} | {2}: {1}".format(
            calcular_max_min_dato(lista_heroes,caracteristica,genero,tipo_calculo)["nombre"],
            calcular_max_min_dato(lista_heroes,caracteristica,genero,tipo_calculo)[caracteristica],
            caracteristica)
            lista.append(calcular_max_min_dato(lista_heroes,caracteristica,genero,tipo_calculo))           
            print(mensaje)

        elif (tipo_calculo == "minimo"):
            mensaje = "Menor {2}: Nombre: {0} | {2}: {1}".format(
            calcular_max_min_dato(lista_heroes,caracteristica,genero,tipo_calculo)["nombre"],
            calcular_max_min_dato(lista_heroes,caracteristica,genero,tipo_calculo)[caracteristica],
            caracteristica)
            lista.append(calcular_max_min_dato(lista_heroes,caracteristica,genero,tipo_calculo))
            print(mensaje)
    else:
        print("-1")
    
    archivo = direccion_archivo_primer_parte
    archivo += "\heroes_{0}_{1}_{2}.csv".format(tipo_calculo,caracteristica,genero)
    
    guardar_archivo(archivo,lista)

#stark_calcular_imprimir_guardar_heroe_genero(lista_personajes,"M","peso","minimo",
#r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\ejercicio_industrias_stark")

'''
Basandote en la función 'sumar_dato_heroe', crear la función llamada
'sumar_dato_heroe_genero' la cual deberá tener un parámetro extra
del tipo string que representará el género con el que se va a trabajar.
Esta función antes de realizar la suma en su variable sumadora,
deberá validar lo siguiente:
A. El tipo de dato del héroe debe ser diccionario.
B. El héroe actual de la iteración no debe estar vacío (ser
diccionario vacío)
C. El género del héroe debe coincidir con el pasado por
parámetro.
Una vez que cumpla con las condiciones, podrá realizar la suma. La
función deberá retornar la suma del valor de la key de los héroes o
heroínas que cumplan las condiciones o -1 en caso de que no se
cumplan las validaciones
'''

def sumar_dato_heroe_genero(lista_heroes:list,caracteristica:str,genero:str)->float:
    lista_heroes_genero = []
    for heroe in lista_heroes:
        if(es_genero(heroe,genero)):
            lista_heroes_genero.append(heroe)

    suma_caracterisitca = sumar_dato_heroe(lista_heroes_genero,caracteristica)
    return suma_caracterisitca

#print(sumar_dato_heroe_genero(lista_personajes,"peso","M"))

'''
Crear la función 'cantidad_heroes_genero' la cual recibirá por
parámetro la lista de héroes y un string que representará el género a
buscar. La función deberá iterar y sumar la cantidad de héroes o
heroínas que cumplan con la condición de género pasada por
parámetro, retornará dicha suma.
'''
def cantidad_heroes_genero(lista_heroes:list,genero:str)->int:
    contador = 0 
    for heroe in lista_heroes:
        if(es_genero(heroe,genero) == True):
            contador += 1
    return contador

#print(cantidad_heroes_genero(lista_personajes,"F"))

'''
Basandote en la función 'calcular_promedio', crear la función
'calcular_promedio_genero' la cual tendrá como parámetro extra un
string que representará el género a buscar. la lógica es similar a la
función anteriormente mencionada en el enunciado. Reutilizar las
funciones: 'sumar_dato_heroe_genero', 'cantidad_heroes_genero' y
'dividir'.
retornará el promedio obtenido, según la key y género pasado por
parámetro.
'''

def calcular_promedio_genero(lista_heroes:list,caracteristica:str,genero:str)->float:
    acumulador = sumar_dato_heroe_genero(lista_heroes,caracteristica,genero)
    contador = cantidad_heroes_genero(lista_heroes,genero)
    promedio = acumulador/contador
    return promedio

#print(calcular_promedio_genero(lista_personajes,"peso","M"))


'''
Basandote en la función ‘stark_calcular_imprimir_promedio_altura',
desarrollar la función 'stark_calcular_imprimir_guardar_
promedio_altura_genero' la cual tendrá como parámetro extra un string
que representará el género de los héroes a buscar.
La función antes de hacer nada, deberá validar que la lista no esté
vacía. En caso de no estar vacía: calculará el promedio y lo imprimirá
formateado al estilo:
Altura promedio género F: 178.45
En caso de estar vacía, imprimirá como mensaje:
Error: Lista de héroes vacía.
Luego de imprimir la función deberá guardar en un archivo los mismos
datos. El nombre del archivo debe tener el siguiente formato:
heroes_promedio_altura_genero.csv
Donde:
A. genero: será el género de los héroes a calcular, siendo M y F
únicas opciones posibles.
Ejemplos:
heroes_promedio_altura_F.csv
heroes_promedio_altura_M.csv
Reutilizar las funciones: 'calcular_promedio_genero', 'imprimir_dato' y
'guardar_archivo'.
Esta función retornará True si pudo la lista tiene algún elemento y pudo
guardar el archivo, False en caso de que esté vacía o no haya podido
guardar el archivo
'''

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes:list,caracteristica:str,genero:str,archivo_primer_parte:str):
    error = False
    lista = []
    if (len(lista_heroes)>0):
        error = True
        lista_heroes_genero=genero
        promedio = calcular_promedio_genero(lista_heroes,caracteristica,genero)
        print ("Altura promedio género {0}: {1}".format(genero,promedio))
        for heroe in lista_heroes:
            if(es_genero(heroe,genero)):
                lista.append(heroe)
    else:
        print("Error: Lista de héroes vacía.")

    archivo = archivo_primer_parte
    archivo += "\heroes_promedio_altura_{0}.csv".format(genero)        
    guardar_archivo(archivo,lista)
    return error

#print(stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes,"peso","F",
#r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\ejercicio_industrias_stark"))

'''
Crear la función 'calcular_cantidad_tipo' la cual recibirá por parámetro
la lista de héroes y un string que representará el tipo de dato/key a
buscar (color_ojos, color_pelo, etc)
Antes de hacer nada, deberá validar que la lista no esté vacía. En caso
de estarlo devolver un diccionario con la siguiente estructura:
{
"Error": “La lista se encuentra vacía”
}
La función deberá retornar un diccionario con los distintos valores del
tipo de dato pasada por parámetro y la cantidad de cada uno (crear un
diccionario clave valor).
Por ejemplo, si el tipo de dato fuese color_ojos, devolverá un
diccionario de la siguiente manera:
{
"Celeste": 4,
"Verde": 8,
"Marron": 6
}
Reutilizar la función 'capitalizar_palabras' para capitalizar los valores
de las keys.
'''
def calcular_cantidad_tipo(lista_heroes:list,clave:str):
    dic_return = {}
    valor_dic = ""
    if (len(lista_heroes)>0):
        for heroe in lista_heroes:
            if(valor_dic != heroe[clave]):
                valor_dic = heroe[clave] 
                dic_return[valor_dic] = 0
            elif(valor_dic == heroe[clave]):
                valor_dic = heroe[clave] 
                dic_return[valor_dic] += 1 #NO ENTIENDO PORQUE NO SALE
    else:
        dic_return["Error"] = "La lista se encuentra vacía"
    
    return dic_return

#print(calcular_cantidad_tipo(lista_personajes,"color_pelo")) 

'''
Crear la función 'guardar_cantidad_heroes_tipo' la cual recibirá como
parámetro un diccionario que representará las distintas variedades del
tipo de dato (distintos colores de ojos, pelo, etc) como clave con sus
respectivas cantidades como valor. Como segundo parámetro recibirá
el dato (color_pelo, color_ojos, etc) el cual tendrás que usarlo
únicamente en el mensaje final formateado. Esta función deberá iterar
cada key del diccionario y variabilizar dicha key con su valor para
luego formatearlos en un mensaje el cual deberá guardar en archivo.
Por ejemplo:
"Caracteristica: color_ojos Blue - Cantidad de heroes: 9"
Reutilizar la función 'guardar_archivo'. El nombre del archivo final
deberá respetar el formato:
heroes_cantidad_tipoDato.csv
Donde:
● tipoDato: representará el nombre de la key la cual se está
evaluando la cantidad de héroes.
Ejemplo:
heroes_cantidad_color_pelo.csv
heroes_cantidad_color_ojos.csv
La función retornará True si salió todo bien, False caso contrario.
'''
'''
Crear la función 'stark_calcular_cantidad_por_tipo' la cual recibirá por
parámetro la lista de héroes y un string que representará el tipo de
dato/key a buscar (color_ojos, color_pelo, etc). Dentro deberás
reutilizar 'calcular_cantidad_tipo' y 'guardar_cantidad_heroes_tipo' con
la lógica que cada una de esas funciones manejan.
Esta función retornará True si pudo guardar el archivo, False caso
contrario.
'''
#ESTA RELACIONADA A LA ANTERIOR


'''
Crear la función 'obtener_lista_de_tipos' la cual recibirá por parámetro
la lista de héroes y un string que representará el tipo de dato/key a
buscar (color_ojos, color_pelo, etc).
Esta función deberá iterar la lista de héroes guardando en una lista las
variedades del tipo de dato pasado por parámetro (sus valores).
En caso de encontrar una key sin valor (o string vacío), deberás
hardcodear con el valor 'N/A' y luego agregarlo a la lista donde irás
guardando todos los valores encontrados, si el valor del héroe no tiene
errores, guardarlo tal cual viene.
Finalmente deberás eliminar los duplicados de esa lista y retornarla
como un set.
Reutilizar 'capitalizar_palabras' para guardar cada uno de los datos
con la primera letra mayúscula.
'''
def obtener_lista_de_tipos(lista_heroes:list,clave:str):
    lista = []
    for heroe in lista_heroes:
        if(heroe[clave] == ""):
            lista.append("N/A")
        else:
            dato = capitalizar_palabra(heroe[clave])
            lista.append(dato)

    set_de_lista = set(lista)

    return set_de_lista

#print(obtener_lista_de_tipos(lista_personajes,"inteligencia"))

'''
Crear la función 'normalizar_dato' la cual recibirá por parámetro un
dato de héroe (el valor de una de sus keys, por ejemplo si la key fuese
color_ojos y su valor fuese Verde, recibira este ultimo) y tambien una
variable como string la cual representará el valor por defecto a colocar
en caso de que el valor está vacío. Deberá validar que el dato no esté
vacío, en caso de estarlo lo reemplazará con el valor default pasado
por parámetro y lo retornará, caso contrario lo retornará sin
modificaciones.
'''

def normalizar_datos(valor_hero:str,valor_defecto:str="N/A"):
    
    if (valor_hero == ""):
        valor_normalizado = valor_defecto
    else:
        valor_normalizado = valor_hero
    
    return valor_normalizado


#print(normalizar_datos(lista_personajes[0]["color_ojos"]))

'''
Crear la función 'normalizar_heroe' la cual recibirá dos parámetros. el
primero será un diccionario que representará un solo héroe, el
segundo parámetro será el nombre de la key de dicho diccionario la
cual debe ser normalizada.
La función deberá capitalizar las palabras que tenga dicha key como
valor, luego deberá normalizar el dato (ya que si viene vacío, habrá
que setearlo con N/A).
Finalmente deberá capitalizar todas las palabras del nombre del héroe
y deberá retornarlo.
Reutilizar: 'capitalizar_palabras' y 'normalizar_dato'
'''
