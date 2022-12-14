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

#data_stark = leer_archivo(r"C:\Users\JONY\Desktop\Programaci??n\1 er cuatrimestre\Programacion-I\ejercicio_archivos\data_stark.json")
#stark_menu_principal_desafio_5(data_stark)
#C:\Users\JONY\Desktop\Programaci??n\1 er cuatrimestre\Programacion-I\ejercicio_archivos\data_stark.json

def guardar_archivo (archivo_extension:str,lista_con_contenido:list)->bool:
    with open(archivo_extension,"w") as archivo:
        for contenido in lista_con_contenido:
            linea_archivo = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}\n".format(contenido["nombre"]            
            ,contenido["identidad"],contenido["empresa"],contenido["altura"],contenido["peso"]
            ,contenido["genero"],contenido["color_ojos"],contenido["color_pelo"],contenido["fuerza"],contenido["inteligencia"])
            archivo.write(linea_archivo)
            
        
#guardar_archivo(r"C:\Users\JONY\Desktop\Programaci??n\1 er cuatrimestre\Programacion-I\ejercicio_archivos\data_stark_2.csv",lista_personajes)


'''
 Crear la funci??n 'capitalizar_palabras' la cual recibir?? por par??metro un
string que puede contener una o muchas palabras. La funci??n deber??
retornar dicho string en el cual todas y cada una de las palabras que
contenga, deber??n estar capitalizadas (Primera letra en may??scula).
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
Crear la funci??n 'obtener_nombre_capitalizado' la cual recibir?? por
par??metro un diccionario el cual representar?? a un h??roe y devolver??
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
Crear la funci??n 'obtener_nombre_y_dato' la cual recibir?? por
par??metro un diccionario el cual representar?? a un h??roe y una key
(string) la cual representar?? la key del h??roe a imprimir. La funci??n
devolver?? un string el cual contenga el nombre y dato (key) del h??roe a
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
Crear la funci??n 'es_genero' la cual recibir?? por par??metro un
diccionario que representar?? un h??roe y un string el cual ser?? usado
para evaluar si el h??roe coincide con el g??nero buscado (El string
puede ser M, F o NB). retornar?? True en caso de que cumpla, False
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
Crear la funci??n 'stark_guardar_heroe_genero' la cual recibira por
par??metro la lista de h??roes y un string el cual representar?? el g??nero
a evaluar (puede ser M o F). Deber?? imprimir solamente los h??roes o
hero??nas que coincidan con el g??nero pasado por par??metro y
adem??s, deber?? guardar dichos nombres en un archivo con extensi??n
csv (cada nombre deber?? ir separado por una coma)
Reutilizar las funciones 'es_genero', 'obtener_nombre_capitalizado',
'imprimir_dato' y 'guardar_archivo'.
En el caso de 'guardar_archivo', cuando se llame a esta funci??n el
nombre de archivo a guardar deber?? respetar el formato:
heroes_M.csv, heroes_F.csv o heroes_NB seg??n corresponda.
La funci??n retornar?? True si pudo guardar el archivo, False caso
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
#r"C:\Users\JONY\Desktop\Programaci??n\1 er cuatrimestre\Programacion-I\ejercicio_industrias_stark\archivo_datos_genero.csv")

'''
Basandote en la funci??n 'calcular_min', crear la funci??n
'calcular_min_genero' la cual recibir?? como par??metro extra un string
que representa el g??nero de la hero??na/h??roe a buscar. modificar un
poco la l??gica para que dentro no se traiga por defecto al primer h??roe
de la lista sino que mediante un flag, se traiga el primer h??roe que
COINCIDA con el g??nero pasado por par??metro. A partir de all??, podr??
empezar a comparar entre h??roes o hero??nas que coincidan con el
g??nero pasado por par??metro. La funci??n retornar?? el h??roe o hero??na
que cumpla la condici??n de tener el m??nimo (peso, altura u otro dato)
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
con la misma l??gica la cual reciba un par??metro string que
representar?? el g??nero del h??roe/hero??na a buscar y renombrarla a
'calcular_max_min_dato_genero'. La estructura ser?? similar a la ya
antes creada, salvo que dentro de ella deber?? llamar a
'calcular_max_genero' y 'calcular_min_genero', pasandoles el nuevo
par??metro. Esta funci??n retornar?? el h??roe o hero??na que cumpla con
las condiciones pasados por par??metro. Por ejemplo, si se le pasa 'F' y
'minimo', retornar?? la hero??na que tenga el m??nimo (altura, peso u otro
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
Basandote en la funci??n 'stark_calcular_imprimir_heroe' crear la
funci??n ???stark_calcular_imprimir_guardar_heroe_genero??? que adem??s
reciba un string el cual representar?? el g??nero a evaluar. El formato de
mensaje a imprimir deber?? ser estilo:
Mayor Altura: Nombre: Gamora | Altura: 183.65
Adem??s la funci??n deber?? guardar en un archivo csv el resultado
obtenido.
Reutilizar: 'calcular_max_min_dato_genero', 'obtener_nombre_y_dato',
'imprimir_dato' y 'guardar_archivo'.
En el caso de 'guardar_archivo' el nombre del archivo debe respetar el
formato:
heroes_calculo_key_genero.csv
Donde:
??? c??lculo: representar?? el string m??ximo o m??nimo
??? key: representar?? cual es la key la cual se tiene que hacer el
c??lculo
??? genero: representar?? el g??nero a calcular.
Ejemplo: para calcular el h??roe m??s alto femenino, el archivo se
deber?? llamar:
heroes_maximo_altura_F.csv
Esta funci??n retornar?? True si pudo guardar el archivo, False caso
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
#r"C:\Users\JONY\Desktop\Programaci??n\1 er cuatrimestre\Programacion-I\ejercicio_industrias_stark")

'''
Basandote en la funci??n 'sumar_dato_heroe', crear la funci??n llamada
'sumar_dato_heroe_genero' la cual deber?? tener un par??metro extra
del tipo string que representar?? el g??nero con el que se va a trabajar.
Esta funci??n antes de realizar la suma en su variable sumadora,
deber?? validar lo siguiente:
A. El tipo de dato del h??roe debe ser diccionario.
B. El h??roe actual de la iteraci??n no debe estar vac??o (ser
diccionario vac??o)
C. El g??nero del h??roe debe coincidir con el pasado por
par??metro.
Una vez que cumpla con las condiciones, podr?? realizar la suma. La
funci??n deber?? retornar la suma del valor de la key de los h??roes o
hero??nas que cumplan las condiciones o -1 en caso de que no se
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
Crear la funci??n 'cantidad_heroes_genero' la cual recibir?? por
par??metro la lista de h??roes y un string que representar?? el g??nero a
buscar. La funci??n deber?? iterar y sumar la cantidad de h??roes o
hero??nas que cumplan con la condici??n de g??nero pasada por
par??metro, retornar?? dicha suma.
'''
def cantidad_heroes_genero(lista_heroes:list,genero:str)->int:
    contador = 0 
    for heroe in lista_heroes:
        if(es_genero(heroe,genero) == True):
            contador += 1
    return contador

#print(cantidad_heroes_genero(lista_personajes,"F"))

'''
Basandote en la funci??n 'calcular_promedio', crear la funci??n
'calcular_promedio_genero' la cual tendr?? como par??metro extra un
string que representar?? el g??nero a buscar. la l??gica es similar a la
funci??n anteriormente mencionada en el enunciado. Reutilizar las
funciones: 'sumar_dato_heroe_genero', 'cantidad_heroes_genero' y
'dividir'.
retornar?? el promedio obtenido, seg??n la key y g??nero pasado por
par??metro.
'''

def calcular_promedio_genero(lista_heroes:list,caracteristica:str,genero:str)->float:
    acumulador = sumar_dato_heroe_genero(lista_heroes,caracteristica,genero)
    contador = cantidad_heroes_genero(lista_heroes,genero)
    promedio = acumulador/contador
    return promedio

#print(calcular_promedio_genero(lista_personajes,"peso","M"))


'''
Basandote en la funci??n ???stark_calcular_imprimir_promedio_altura',
desarrollar la funci??n 'stark_calcular_imprimir_guardar_
promedio_altura_genero' la cual tendr?? como par??metro extra un string
que representar?? el g??nero de los h??roes a buscar.
La funci??n antes de hacer nada, deber?? validar que la lista no est??
vac??a. En caso de no estar vac??a: calcular?? el promedio y lo imprimir??
formateado al estilo:
Altura promedio g??nero F: 178.45
En caso de estar vac??a, imprimir?? como mensaje:
Error: Lista de h??roes vac??a.
Luego de imprimir la funci??n deber?? guardar en un archivo los mismos
datos. El nombre del archivo debe tener el siguiente formato:
heroes_promedio_altura_genero.csv
Donde:
A. genero: ser?? el g??nero de los h??roes a calcular, siendo M y F
??nicas opciones posibles.
Ejemplos:
heroes_promedio_altura_F.csv
heroes_promedio_altura_M.csv
Reutilizar las funciones: 'calcular_promedio_genero', 'imprimir_dato' y
'guardar_archivo'.
Esta funci??n retornar?? True si pudo la lista tiene alg??n elemento y pudo
guardar el archivo, False en caso de que est?? vac??a o no haya podido
guardar el archivo
'''

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes:list,caracteristica:str,genero:str,archivo_primer_parte:str):
    error = False
    lista = []
    if (len(lista_heroes)>0):
        error = True
        lista_heroes_genero=genero
        promedio = calcular_promedio_genero(lista_heroes,caracteristica,genero)
        print ("Altura promedio g??nero {0}: {1}".format(genero,promedio))
        for heroe in lista_heroes:
            if(es_genero(heroe,genero)):
                lista.append(heroe)
    else:
        print("Error: Lista de h??roes vac??a.")

    archivo = archivo_primer_parte
    archivo += "\heroes_promedio_altura_{0}.csv".format(genero)        
    guardar_archivo(archivo,lista)
    return error

#print(stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes,"peso","F",
#r"C:\Users\JONY\Desktop\Programaci??n\1 er cuatrimestre\Programacion-I\ejercicio_industrias_stark"))

'''
Crear la funci??n 'calcular_cantidad_tipo' la cual recibir?? por par??metro
la lista de h??roes y un string que representar?? el tipo de dato/key a
buscar (color_ojos, color_pelo, etc)
Antes de hacer nada, deber?? validar que la lista no est?? vac??a. En caso
de estarlo devolver un diccionario con la siguiente estructura:
{
"Error": ???La lista se encuentra vac??a???
}
La funci??n deber?? retornar un diccionario con los distintos valores del
tipo de dato pasada por par??metro y la cantidad de cada uno (crear un
diccionario clave valor).
Por ejemplo, si el tipo de dato fuese color_ojos, devolver?? un
diccionario de la siguiente manera:
{
"Celeste": 4,
"Verde": 8,
"Marron": 6
}
Reutilizar la funci??n 'capitalizar_palabras' para capitalizar los valores
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
        dic_return["Error"] = "La lista se encuentra vac??a"
    
    return dic_return

#print(calcular_cantidad_tipo(lista_personajes,"color_pelo")) 

'''
Crear la funci??n 'guardar_cantidad_heroes_tipo' la cual recibir?? como
par??metro un diccionario que representar?? las distintas variedades del
tipo de dato (distintos colores de ojos, pelo, etc) como clave con sus
respectivas cantidades como valor. Como segundo par??metro recibir??
el dato (color_pelo, color_ojos, etc) el cual tendr??s que usarlo
??nicamente en el mensaje final formateado. Esta funci??n deber?? iterar
cada key del diccionario y variabilizar dicha key con su valor para
luego formatearlos en un mensaje el cual deber?? guardar en archivo.
Por ejemplo:
"Caracteristica: color_ojos Blue - Cantidad de heroes: 9"
Reutilizar la funci??n 'guardar_archivo'. El nombre del archivo final
deber?? respetar el formato:
heroes_cantidad_tipoDato.csv
Donde:
??? tipoDato: representar?? el nombre de la key la cual se est??
evaluando la cantidad de h??roes.
Ejemplo:
heroes_cantidad_color_pelo.csv
heroes_cantidad_color_ojos.csv
La funci??n retornar?? True si sali?? todo bien, False caso contrario.
'''
'''
Crear la funci??n 'stark_calcular_cantidad_por_tipo' la cual recibir?? por
par??metro la lista de h??roes y un string que representar?? el tipo de
dato/key a buscar (color_ojos, color_pelo, etc). Dentro deber??s
reutilizar 'calcular_cantidad_tipo' y 'guardar_cantidad_heroes_tipo' con
la l??gica que cada una de esas funciones manejan.
Esta funci??n retornar?? True si pudo guardar el archivo, False caso
contrario.
'''
#ESTA RELACIONADA A LA ANTERIOR


'''
Crear la funci??n 'obtener_lista_de_tipos' la cual recibir?? por par??metro
la lista de h??roes y un string que representar?? el tipo de dato/key a
buscar (color_ojos, color_pelo, etc).
Esta funci??n deber?? iterar la lista de h??roes guardando en una lista las
variedades del tipo de dato pasado por par??metro (sus valores).
En caso de encontrar una key sin valor (o string vac??o), deber??s
hardcodear con el valor 'N/A' y luego agregarlo a la lista donde ir??s
guardando todos los valores encontrados, si el valor del h??roe no tiene
errores, guardarlo tal cual viene.
Finalmente deber??s eliminar los duplicados de esa lista y retornarla
como un set.
Reutilizar 'capitalizar_palabras' para guardar cada uno de los datos
con la primera letra may??scula.
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
Crear la funci??n 'normalizar_dato' la cual recibir?? por par??metro un
dato de h??roe (el valor de una de sus keys, por ejemplo si la key fuese
color_ojos y su valor fuese Verde, recibira este ultimo) y tambien una
variable como string la cual representar?? el valor por defecto a colocar
en caso de que el valor est?? vac??o. Deber?? validar que el dato no est??
vac??o, en caso de estarlo lo reemplazar?? con el valor default pasado
por par??metro y lo retornar??, caso contrario lo retornar?? sin
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
Crear la funci??n 'normalizar_heroe' la cual recibir?? dos par??metros. el
primero ser?? un diccionario que representar?? un solo h??roe, el
segundo par??metro ser?? el nombre de la key de dicho diccionario la
cual debe ser normalizada.
La funci??n deber?? capitalizar las palabras que tenga dicha key como
valor, luego deber?? normalizar el dato (ya que si viene vac??o, habr??
que setearlo con N/A).
Finalmente deber?? capitalizar todas las palabras del nombre del h??roe
y deber?? retornarlo.
Reutilizar: 'capitalizar_palabras' y 'normalizar_dato'
'''
