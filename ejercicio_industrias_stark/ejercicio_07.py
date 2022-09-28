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
import re

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

def imprimir_menu_desafio_5():
    
    mensaje = "\nA. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M"
    mensaje += "\nB. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F"
    mensaje += "\nC. Recorrer la lista y determinar cuál es el superhéroe más alto de género M"
    mensaje += "\nD. Recorrer la lista y determinar cuál es el superhéroe más alto de género F"
    mensaje += "\nE. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M"
    mensaje += "\nF. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F"
    mensaje += "\nG. Recorrer la lista y determinar la altura promedio de los superhéroes de género M"
    mensaje += "\nH. Recorrer la lista y determinar la altura promedio de los superhéroes de género F"
    mensaje += "\nI. Determinar cuántos superhéroes tienen cada tipo de color de ojos."
    mensaje += "\nJ. Determinar cuántos superhéroes tienen cada tipo de color de pelo."
    mensaje += "\nK. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’)."
    mensaje += "\nL. Listar todos los superhéroes agrupados por color de ojos."
    mensaje += "\nM. Listar todos los superhéroes agrupados por color de pelo."
    mensaje += "\nN. Listar todos los superhéroes agrupados por tipo de inteligencia"
    mensaje += "\nO-Z. Salir\n"
    respuesta = input(mensaje)
    return respuesta


    

def stark_menu_principal_desafio_5(lista_heroes:list):

    respuesta = re.findall("[A-Za-z]{1}",imprimir_menu_desafio_5())
    
    while (len(respuesta) > 0):
                
        if(respuesta == ['A']):
            recorrer_lista_personajes_por_genero(lista_heroes,"M")
        elif(respuesta == ['B']):
            recorrer_lista_personajes_por_genero(lista_heroes,"F")
        elif(respuesta == ['C']):
            print(calcular_personaje_mas_alto_bajo_por_genero(lista_heroes,"M","alto"))
        elif(respuesta == ['D']):
            print(calcular_personaje_mas_alto_bajo_por_genero(lista_heroes,"F","alto"))
        elif(respuesta == ['E']):
            print(calcular_personaje_mas_alto_bajo_por_genero(lista_heroes,"M","bajo"))
        elif(respuesta == ['F']):
            print(calcular_personaje_mas_alto_bajo_por_genero(lista_heroes,"M","bajo"))
        elif(respuesta == ['G']):
            print(calcular_promedio_alturas_por_genero(lista_heroes,"M"))
        elif(respuesta == ['H']):
            print(calcular_promedio_alturas_por_genero(lista_heroes,"F"))
        elif(respuesta == ['I']):
            print(determinar_cantidad_caracteristica(lista_heroes,"color_pelo"))
        elif(respuesta == ['J']):
            print(determinar_cantidad_caracteristica(lista_heroes,"color_ojos"))
        elif(respuesta == ['K']):
            print(determinar_cantidad_caracteristica(lista_heroes,"inteligencia"))
        elif(respuesta == ['L']):
            print(listar_heroes_misma_caracteristica(lista_heroes,"color_pelo"))
        elif(respuesta == ['M']):
            print(listar_heroes_misma_caracteristica(lista_heroes,"color_ojos"))
        elif(respuesta == ['N']):
            print(listar_heroes_misma_caracteristica(lista_heroes,"inteligencia"))
        
    
        respuesta = re.findall("[A-Za-z]{1}",imprimir_menu_desafio_5())
    


