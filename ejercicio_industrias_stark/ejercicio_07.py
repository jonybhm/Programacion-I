from data_stark import lista_personajes
'''

{
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
  }
'''

#--------------BUSCAR PRIMER GENERO------------------------
def buscar_primer_personaje_por_genero(lista_heroes:list,genero:str)->dict:
    '''
    Busca el primer personaje de determinado genero
    Recibe la lista importada y un string que determine el genero
    Devuelve el diccionario con los datos del personaje
    '''
    primer_personaje_por_genero = {}
    for personaje in lista_heroes:
        if (personaje["genero"] == genero):
            primer_personaje_por_genero = personaje 
            break
   
    return primer_personaje_por_genero

#--------------RECORRER LISTAS POR GENERO ------------------------
def recorrer_lista_personajes_por_genero(lista_heroes:list,genero:str):
    '''
    Recorre e imprime la lista de personajes dado un genero especifico
    Recibe la lista importada un str con el genero
    '''
    for personaje in lista_heroes:
        if(personaje["genero"] == genero):
            print(personaje["nombre"])

          

#--------------PERSONAJE MAS ALTO / BAJO------------------------
def calcular_personaje_mas_alto_bajo_por_genero(lista_heroes:list,genero:str,altura:str)->dict:
    '''
    Calcula el personaje mas alto o bajo segun el genero
    Recibe la lista importada, y dos str, uno para el genero y otro para el tipo de altura (alto/bajo)
    Devuelve un 
    '''
    
    personaje_mas_alto_o_bajo = buscar_primer_personaje_por_genero(lista_heroes,genero)
    personaje_mas_alto_o_bajo["altura"] = float(personaje_mas_alto_o_bajo["altura"])

    for personaje in lista_heroes:
        if(personaje["genero"] == genero):    
            personaje["altura"] = float(personaje["altura"])
            if(personaje_mas_alto_o_bajo["altura"] < personaje["altura"] and altura=="alto"):
                personaje_mas_alto_o_bajo = personaje       
            elif(personaje_mas_alto_o_bajo["altura"] > personaje["altura"] and altura=="bajo"):
                personaje_mas_alto_o_bajo = personaje      

    return personaje_mas_alto_o_bajo


#--------------PROMEDIO ALTURAS POR GENERO------------------------
def calcular_promedio_alturas_por_genero(lista_heroes:list,genero:str)->float:
    acumulador_alturas_personajes = 0

    for personaje in lista_heroes:    
        if(personaje["genero"] == genero):
            personaje["altura"] = float(personaje["altura"])
            acumulador_alturas_personajes = acumulador_alturas_personajes + personaje["altura"]
        
    promedio_alturas = acumulador_alturas_personajes/len(lista_heroes)

    return promedio_alturas


#--------------DETERMINAR CANTIDAD DE CADA CARACTERISTICA------------------------
def determinar_cantidad_caracteristica(lista_heroes:list,caracteristica:str)->list:
    '''
    Determina la cantidad de personajes que comparten la misma caracteristica
    Recibe la lista importada y el key que representa la caracteristica
    Devuelve una lista de diccionarios que indica el tipo de caracteristica y la cantidad de las misma
    '''
    lista_caracteristica = [{caracteristica:lista_heroes[0][caracteristica],"cantidad":0}]
    for personaje in lista_heroes:
        dic_caracteristica = {}
        flag = False
        for ojos in lista_caracteristica:
            if (personaje[caracteristica] == ojos[caracteristica]):
                ojos["cantidad"]+=1
                flag = True
            
        if (flag == False):
            dic_caracteristica = {caracteristica:personaje[caracteristica],"cantidad":1}
            lista_caracteristica.append(dic_caracteristica)
    
    if (caracteristica=="inteligencia"):
        for inteligencia in lista_caracteristica:
            if (inteligencia["inteligencia"]==""):
                inteligencia["inteligencia"]="No tiene"

    return lista_caracteristica


#--------------LISTAR HEROES POR CARACTERISTICA ------------------------
def listar_heroes_misma_caracteristica(lista_heroes:list,caracteristica:str)->list:
    '''
    Hace una lista de diccionarios con heroes que comparten un mismo tipo de caracteristica
    Recibe la lista importada y un str que representa la caracteristica
    Devuelve una lista de diccionarios ordenada por caracteristica
    '''
    lista_heroes_misma_caracteristica = []
    lista_ordenada_por_caracteristica = [{caracteristica:lista_heroes[0][caracteristica],"nombres":lista_heroes_misma_caracteristica}]
    

    for personaje in lista_heroes:
        flag = True
        for caracteristica_i in lista_ordenada_por_caracteristica:
            if (personaje[caracteristica] == caracteristica_i[caracteristica]):
                caracteristica_i["nombres"].append(personaje["nombre"])
                flag = False
        #el if tiene que estar por fuera del for
        if (flag == True):
            lista_heroes_misma_caracteristica = []
            dic_caracteristica_nombre = {caracteristica:personaje[caracteristica],"nombres":lista_heroes_misma_caracteristica}
            lista_ordenada_por_caracteristica.append(dic_caracteristica_nombre)

    #set_ordenado_por_caracteristica = set (lista_ordenada_por_caracteristica)
    #print(set_ordenado_por_caracteristica)    
    return lista_ordenada_por_caracteristica


while (True):
    mensaje = "\n1-Listar heroes masculinos\n2-Listar heroes femeninos"
    mensaje += "\n3-Mostrar heroe mas alto masculino\n4-Mostrar heroe mas alto femenino"
    mensaje += "\n5-Mostrar heroe mas bajo masculino\n6-Mostrar heroe mas bajo femenino"
    mensaje += "\n7-Mostrar promedio alturas heroes masculino\n8-Mostrar promedio alturas heroes femenino"
    mensaje += "\n9-Mostrar cantidad heroes tipo de pelo\n10-Mostrar cantidad heroes tipo de ojos\n11-Mostrar cantidad heroes tipo de inteligencia"
    mensaje += "\n12-Listar heroes tipo de pelo\n13-Listar heroes tipo de ojos\n14-Listar heroes tipo de inteligencia\n15-Salir\n"
    respuesta = input(mensaje)

    if(respuesta == "1"):
        recorrer_lista_personajes_por_genero(lista_personajes,"M")
    elif(respuesta == "2"):
        recorrer_lista_personajes_por_genero(lista_personajes,"F")
    elif(respuesta == "3"):
        print(calcular_personaje_mas_alto_bajo_por_genero(lista_personajes,"M","alto"))
    elif(respuesta == "4"):
        print(calcular_personaje_mas_alto_bajo_por_genero(lista_personajes,"F","alto"))
    elif(respuesta == "5"):
        print(calcular_personaje_mas_alto_bajo_por_genero(lista_personajes,"M","bajo"))
    elif(respuesta == "6"):
        print(calcular_personaje_mas_alto_bajo_por_genero(lista_personajes,"M","bajo"))
    elif(respuesta == "7"):
        print(calcular_promedio_alturas_por_genero(lista_personajes,"M"))
    elif(respuesta == "8"):
        print(calcular_promedio_alturas_por_genero(lista_personajes,"F"))
    elif(respuesta == "9"):
        print(determinar_cantidad_caracteristica(lista_personajes,"color_pelo"))
    elif(respuesta == "10"):
        print(determinar_cantidad_caracteristica(lista_personajes,"color_ojos"))
    elif(respuesta == "11"):
        print(determinar_cantidad_caracteristica(lista_personajes,"inteligencia"))
    elif(respuesta == "12"):
        print(listar_heroes_misma_caracteristica(lista_personajes,"color_pelo"))
    elif(respuesta == "13"):
        print(listar_heroes_misma_caracteristica(lista_personajes,"color_ojos"))
    elif(respuesta == "14"):
        print(listar_heroes_misma_caracteristica(lista_personajes,"inteligencia"))
    elif(respuesta == "15"):
        break




'''
Desafío #01:
Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
utilizando un menú que permita acceder a cada uno de los puntos por separado.
Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a G)
Determinar cuántos superhéroes tienen cada tipo de color de ojos.
Determinar cuántos superhéroes tienen cada tipo de color de pelo.
Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
Listar todos los superhéroes agrupados por color de ojos.
Listar todos los superhéroes agrupados por color de pelo.
Listar todos los superhéroes agrupados por tipo de inteligencia
'''







