from distutils.ccompiler import gen_preprocess_options
import re
from tkinter.ttk import Separator
from urllib import response
from data_stark import lista_personajes


def extraer_iniciales (nombre_heroe:str)->str:
    '''
    Extrae las iniciales del string que representa un nombre
    Recibe un str que representa un nombre propio
    Devuelve un String con las iniciales de dicho nombre separadas por un punto
    '''

    if(len(nombre_heroe) > 0):
        lista_nombre_apellido = nombre_heroe.split(" ")
        iniciales = ""

        for inicial in lista_nombre_apellido:
            if (inicial != "the" and inicial.count("-")!=1):
                iniciales += inicial[:1] + "."
            elif (inicial.count("-")==1):
                lista_dos = inicial.split("-")
                for inciales_con_guion in lista_dos:
                    iniciales += inciales_con_guion[:1] + " " 
    else:
        iniciales = "N/A"

    return iniciales

def definir_iniciales_nombre (heroe:dict)->bool:
    '''
    Agrea a un diccionario existente las iniciales, ademas en caso de error devuelve False
    Recibe un diccionario con datos como nombre
    Devuelve un bool que indica en caso de error un False
    '''

    error = True
    if(type(heroe) == type(dict()) and heroe.get("nombre")):
        iniciales = extraer_iniciales(heroe["nombre"])
        heroe["iniciales"] = iniciales
    else:
        error = False

    return error

#print(definir_iniciales_nombre(lista_personajes[0]))
#print (lista_personajes[0])

def agregar_iniciales_nombre (lista_heroes:list)->bool:
    '''
    Recorre la lista de personajes y agrega a cada heroe una key "iniciales"
    Recive una lista importada
    Devuelve un bool en caso de error
    '''
    error = True
    if (type(lista_heroes) == type(list()) and len(lista_heroes) > 0):
        for personaje in lista_heroes:
            definir_iniciales_nombre(personaje)
        else:
            error = False
    
    return error

#print(agregar_iniciales_nombre(lista_personajes))
#print(lista_personajes)

       
def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    '''
    Imprime la lista con los nuevos datos agregados (iniciales)
    Recibe la lista importada de personajes
    '''
    
    error = True
    if (type(lista_heroes) == type(list()) and len(lista_heroes) > 0):
        agregar_iniciales_nombre(lista_heroes)
        for personaje in lista_heroes:
            print("* {0} ({1})".format(personaje["nombre"],personaje["iniciales"]))
    else:
        error = False   

#stark_imprimir_nombres_con_iniciales(lista_personajes)



def generar_codigo_heroe (id_heroe:int,genero_heroe:str)->str:
   
    
    if (type(id_heroe) == type(str())):
        codigo = genero_heroe + "-" 
        codigo += id_heroe.zfill(10-len(codigo))
    else:
        id_heroe = str(id_heroe)
        codigo = genero_heroe + "-" 
        codigo += id_heroe.zfill(10-len(codigo))
    
    return codigo

#print(generar_codigo_heroe(5,"NB"))

def agregar_codigo_heroe (heroe:dict)->bool:
    error = True
    if(len(heroe) > 0 and len(generar_codigo_heroe(heroe["id"],heroe["genero"])) == 10):
        heroe["codigo_heroe"] = generar_codigo_heroe(heroe["id"],heroe["genero"])
    else:
        error = False
    
    return error

#print(agregar_codigo_heroe(lista_personajes[0]))

def stark_generar_codigos_heroes (lista_heroes:list):
    '''
    La funcion agrega la clave "id" que refiere a la posicion en la lista e imprime una lista de codigos
    Recibe la lista importada
    '''
    if(len(lista_heroes)>0):        
        index = 1
        for personaje in lista_heroes:
            if (type(personaje)==type(dict()) and personaje.get("genero")):
                personaje["id"] = index
                index += 1
                agregar_codigo_heroe(personaje)
            else:
                print("El origen de datos no contiene el formato correcto")

        mensaje = "Se asignaron {0} códigos.\n".format(index)
        mensaje += "El código del primer héroe es: {0}\n".format(lista_heroes[0]["codigo_heroe"])
        mensaje += "El código del ultimo héroe es: {0}\n".format(lista_heroes[index-2]["codigo_heroe"])#no entiendo porque es index-2 y no index-1
        print(mensaje)

    else:
                print("El origen de datos no contiene el formato correcto")

#stark_generar_codigos_heroes(lista_personajes)

def sanitizar_entero(numero_str:str)->int:
    '''
    la funcion analiza si el dato es numerico entero, positico o negativo
    Recibe un str que representa un numero
    Devuelve el numero en formato int sin espacios,si es no numerico = -1 , negativo = -2, otro error = -3
    '''
    es_numero_entero = re.findall("[0-9]+",numero_str)
    lista_con_no_numericos = re.findall("([a-zA-Z]+)",numero_str)
    lista_con_negativos = re.findall("-([0-9]+)",numero_str)
    
    if(len(es_numero_entero) > 0 and len(lista_con_negativos) == 0
    and len(lista_con_no_numericos) == 0):
        numero = int (es_numero_entero[0]) 
        print(numero)
        return numero
    else:
        
        if(len(lista_con_no_numericos) > 0):
            print("-1")        
        elif(len(lista_con_negativos) > 0):
            print("-2")
        else:
            print("-3")



def sanitizar_flotante(numero_str:str)->float:
    '''
    la funcion analiza si el dato es numerico flotante, positico o negativo
    Recibe un str que representa un numero
    Devuelve el numero en formato int sin espacios,si es no numerico = -1 , negativo = -2, otro error = -3
    '''
    es_numero_flotante = re.findall("[0-9]+.[0-9]+",numero_str) #"[0-9]+.[0-9]+" numero flotante
    lista_con_no_numericos = re.findall("([a-zA-Z]+)",numero_str)
    lista_con_negativos = re.findall("-([0-9]+.[0-9]+)",numero_str)
    
    if(len(es_numero_flotante) > 0 and len(lista_con_negativos) == 0 
    and len(lista_con_no_numericos) == 0):
        numero = float (es_numero_flotante[0]) 
        print(numero)
        return numero
    else:
        
        if(len(lista_con_no_numericos) > 0):
            print("-1")        
        elif(len(lista_con_negativos) > 0):
            print("-2")
        else:
            print("-3")

def sanitizar_string (valor_str:str,valor_por_defecto = "-")->str:
    '''
    La funcion verifica el valor si es un string sin numeros,en caso de tener barras las reemplaza por espacios
    Recibe un valor en str
    Devuelve el valor sanitizado 
    '''
    posee_numero = re.findall("[0-9]+",valor_str)
    str_sin_numeros = re.findall("[a-zA-Z/ ]+",valor_str)
    if (len(str_sin_numeros) > 0 and len(posee_numero) == 0):
        str_valor = str_sin_numeros[0]
        str_valor = str_valor.replace("/"," ")
        str_valor = str_valor.lower()
        print(str_valor)
        return str_valor
    else:
        print("N/A")

def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str):
    '''
    La funcion utiliza las tres funciones de sanitizacion
    recibe el diccionario que representa al heroe, la clave con el valor a sanitizar y el tipo de dato
    '''
    tipo_dato = tipo_dato.lower()

    if(heroe.get(clave)):
     
        if(tipo_dato == "string"):
            sanitizar_string(heroe[clave])
        elif(tipo_dato == "entero"):
            sanitizar_entero(heroe[clave])
        elif(tipo_dato == "flotante"):
            sanitizar_flotante(heroe[clave])
        else:
            print("Tipo de dato no reconocido")
        
    else:
        print("La clave especificada no existe en el héroe")
    
#sanitizar_dato(lista_personajes[10],"fuerza","ENTERO")

def stark_normalizar_datos(lista_heroes:list):
    if (len(lista_heroes) > 0):
        for personaje in lista_heroes:
            sanitizar_dato(personaje,"altura","FLOTANTE")
            sanitizar_dato(personaje,"peso","FLOTANTE")
            sanitizar_dato(personaje,"color_ojos","STRING")
            sanitizar_dato(personaje,"color_pelo","STRING")
            sanitizar_dato(personaje,"fuerza","ENTERO")
            sanitizar_dato(personaje,"inteligencia","STRING")
    else:
        "Error: la lista esta vacia"

    print("Datos normalizados") 

#stark_normalizar_datos(lista_personajes)

def generar_indice_nombres(lista_heroes:list)->list:
    '''
    la funcion genera una lista con los cada palabra que componen los nombres de los personajes
    recive la lista con diccionarios de los personajes
    devuelve una lista solo de palabras
    '''
    lista_nombres_heroes = []
    for personaje in lista_heroes:
        lista_palabras_en_nombre = re.split(" ",personaje["nombre"])
        for palabra in lista_palabras_en_nombre:
            lista_nombres_heroes.append(palabra)
            

    return lista_nombres_heroes
    
#print(generar_indice_nombres(lista_personajes))

def stark_imprimir_indice_nombre(lista_heroes:list):
    mensaje = ""
    if(len(lista_heroes)>0):
        for nombre in generar_indice_nombres(lista_heroes):
            mensaje += "{0}-".format(nombre)

    print(mensaje)

#stark_imprimir_indice_nombre(lista_personajes)

def convertir_cm_a_mtrs(valor_cm:str)->float:
    valor_en_cm = sanitizar_flotante(valor_cm)
    if(type(valor_en_cm) == type(float())):
        valor_en_mtrs = valor_en_cm / 100
        return valor_en_mtrs

#print(convertir_cm_a_mtrs("150.5"))  

def generar_separador(patron:str,largo:int,imprimir=True)->str:
    separador = ""
    if (len(patron) > 0 and len(patron) < 3 and 
    largo > 0 and largo < 236):
        for largo_patron in range(largo):
            separador += "{0}".format(patron)
        return separador
    else:
        print ("N/A")
    
    
#print(generar_separador("/",200))

def generar_encabezado(titulo:str)->str:
    titulo_con_separadores = "{0}\n{1}\n{0}".format(generar_separador("*",178),titulo)
    return titulo_con_separadores

#print(generar_encabezado("TITULO"))

def imprimir_ficha_heroe(heroe:dict):
    stark_generar_codigos_heroes (lista_personajes)
    ficha_personaje = "{0}\nNOMBRE DEL HEROE: {1} ({2})".format(generar_encabezado("PRINCIPAL"),heroe["nombre"],extraer_iniciales(heroe["nombre"]))
    ficha_personaje += "\nIDENTIDAD SECRETA: {0}".format(heroe["identidad"])
    ficha_personaje += "\nCONSULTORA: {0}".format(heroe["empresa"])
    ficha_personaje += "\nCODIGO DE HEROE: {0}".format(generar_codigo_heroe(heroe["id"],heroe["genero"]))
    ficha_personaje += "\n{0}\nALTURA: {1:.2f} Mtrs.".format(generar_encabezado("FISICO"),convertir_cm_a_mtrs(heroe["altura"]))
    ficha_personaje += "\nPESO: {0:.2f} Kg.".format(float(heroe["peso"]))
    ficha_personaje += "\nFUERZA: {0} N".format(heroe["fuerza"])
    ficha_personaje += "\n{0}\nCOLOR DE OJOS: {1}".format(generar_encabezado("SEÑAS PARTICULARES"),heroe["color_ojos"])
    ficha_personaje += "\nCOLOR DE PELO: {0}".format(heroe["color_pelo"])
    print (ficha_personaje)


 
#print(imprimir_ficha_heroe(lista_personajes[10]))


def stark_navegar_fichas(lista_heroes:list):
    index = 0
    imprimir_ficha_heroe(lista_heroes[index])
    respuesta = input ("[1] Ir a la izquierda\n[2] Ir a la derecha\n[S] Salir\n>").upper()
    while (respuesta != "S" and respuesta != "1" and respuesta != "2"):
        respuesta = input ("[1] Ir a la izquierda\n[2] Ir a la derecha\n[S] Salir\n>").upper()

    while (respuesta !="S"):
        if(respuesta == "1"):
            index += -1
            imprimir_ficha_heroe(lista_heroes[index])
        elif(respuesta == "2"):
            index += 1
            imprimir_ficha_heroe(lista_heroes[index])
        respuesta = input ("[1] Ir a la izquierda\n[2] Ir a la derecha\n[S] Salir\n>").upper()


#stark_navegar_fichas(lista_personajes)

def imprimir_menu():
    menu = "\n1 - Imprimir la lista de nombres junto con sus iniciales"
    menu += "\n2 - Generar códigos de héroes"
    menu += "\n3 - Normalizar datos"
    menu += "\n4 - Imprimir índice de nombres"
    menu += "\n5 - Navegar fichas"
    menu += "\n6 - Salir\n>"
    print (menu)

def stark_menu_principal()->str:
    respuesta = input(imprimir_menu())
    return respuesta


def stark_marvel_app_3(lista_heroes:list):
    respuesta = stark_menu_principal()
    
    while(respuesta!="6"):
        if(respuesta == "1"):
            stark_imprimir_nombres_con_iniciales(lista_heroes)
            respuesta = stark_menu_principal()
        elif(respuesta == "2"):
            stark_generar_codigos_heroes(lista_heroes)
            respuesta = stark_menu_principal()
        elif(respuesta == "3"):
            stark_normalizar_datos(lista_heroes)
            respuesta = stark_menu_principal()
        elif(respuesta == "4"):
            stark_imprimir_indice_nombre(lista_heroes)
            respuesta = stark_menu_principal()
        elif(respuesta == "5"):
            stark_navegar_fichas(lista_heroes)
            respuesta = stark_menu_principal()
        else:
            respuesta = stark_menu_principal()      


stark_marvel_app_3(lista_personajes)
