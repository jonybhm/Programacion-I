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

#--------------PERSONAJE MAS ALTO------------------------
def calcular_personaje_mas_alto():
    personaje_mas_alto = lista_personajes[0]
    personaje_mas_alto["altura"] = float(personaje_mas_alto["altura"])

    for personaje in lista_personajes:    
        personaje["altura"] = float(personaje["altura"])
        if(personaje_mas_alto["altura"] < personaje["altura"]):
            personaje_mas_alto = personaje       

    print(personaje_mas_alto["nombre"])      
    print(personaje_mas_alto["altura"])

#--------------PERSONAJE MAS BAJO------------------------
def calcular_personaje_mas_bajo():
    personaje_mas_bajo = lista_personajes[0]
    personaje_mas_bajo["altura"] = float(personaje_mas_bajo["altura"])

    for personaje in lista_personajes:    
        personaje["altura"] = float(personaje["altura"])
        if(personaje_mas_bajo["altura"] > personaje["altura"]):
            personaje_mas_bajo = personaje       
        
    print(personaje_mas_bajo["nombre"])
    print(personaje_mas_bajo["altura"])

#--------------PROMEDIO ALTURAS------------------------
def calcular_promedio_alturas():
    acumulador_alturas_personajes = 0

    for personaje in lista_personajes:    
        personaje["altura"] = float(personaje["altura"])
        acumulador_alturas_personajes = acumulador_alturas_personajes + personaje["altura"]
        
    print(acumulador_alturas_personajes/len(lista_personajes))

#--------------PERSONAJE MAS PESADO------------------------
def calcular_personaje_mas_pesado():
    personaje_mas_pesado = lista_personajes[0]
    personaje_mas_pesado["peso"] = float(personaje_mas_pesado["peso"])

    for personaje in lista_personajes:    
        personaje["peso"] = float(personaje["peso"])
        if(personaje_mas_pesado["peso"] < personaje["peso"]):
            personaje_mas_pesado = personaje       

    print(personaje_mas_pesado["nombre"])      
    print(personaje_mas_pesado["peso"])

#--------------PERSONAJE MAS LIVIANOs------------------------
def calcular_personaje_mas_liviano():
    personaje_mas_liviano = lista_personajes[0]
    personaje_mas_liviano["peso"] = float(personaje_mas_liviano["peso"])

    for personaje in lista_personajes:    
        personaje["peso"] = float(personaje["peso"])
        if(personaje_mas_liviano["peso"] > personaje["peso"]):
            personaje_mas_liviano = personaje       
        
    print(personaje_mas_liviano["nombre"])
    print(personaje_mas_liviano["peso"])


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


#--------------RECORRER LISTAS POR GENERO M------------------------
def recorrer_lista_personajes_por_genero_masculino():
    for personaje in lista_personajes:
        if(personaje["genero"] == "M"):
            print(personaje["nombre"])

recorrer_lista_personajes_por_genero_masculino()

#--------------RECORRER LISTAS POR GENERO F------------------------
def recorrer_lista_personajes_por_genero_femenino():
    for personaje in lista_personajes:
        if(personaje["genero"] == "F"):
            print(personaje["nombre"])

recorrer_lista_personajes_por_genero_femenino()
'''

#--------------BUSCAR PRIMER FEMENINO------------------------
def buscar_primer_femenino():
    primer_personaje_femenino = {}
    for personaje in lista_personajes:
        if (personaje["genero"] == "F"):
            primer_personaje_femenino = personaje 
            break
   
    return primer_personaje_femenino



#--------------BUSCAR PRIMER MASCULINO------------------------
def buscar_primer_masculino():
    primer_personaje_masculino = {}
    for personaje in lista_personajes:
        if (personaje["genero"] == "M"):
            primer_personaje_masculino = personaje 
            break
   
    return primer_personaje_masculino


            
'''
#--------------PERSONAJE MAS ALTO MASCULINO------------------------
def calcular_personaje_mas_alto_masculino():
    personaje_mas_alto = buscar_primer_masculino()
    personaje_mas_alto["altura"] = float(personaje_mas_alto["altura"])

    for personaje in lista_personajes:
        if(personaje["genero"] == "M"):    
            personaje["altura"] = float(personaje["altura"])
            if(personaje_mas_alto["altura"] < personaje["altura"]):
                personaje_mas_alto = personaje       

    print(personaje_mas_alto["nombre"])      
    print(personaje_mas_alto["altura"])




#--------------PERSONAJE MAS ALTO FEMENINO------------------------
def calcular_personaje_mas_alto_femenino():
    personaje_mas_alto = buscar_primer_femenino()
    personaje_mas_alto["altura"] = float(personaje_mas_alto["altura"])

    for personaje in lista_personajes:
        if(personaje["genero"] == "F"):    
            personaje["altura"] = float(personaje["altura"])
            if(personaje_mas_alto["altura"] < personaje["altura"]):
                personaje_mas_alto = personaje       

    print(personaje_mas_alto["nombre"])      
    print(personaje_mas_alto["altura"])




#--------------PERSONAJE MAS BAJO MASCULINO------------------------
def calcular_personaje_mas_bajo_masculino():
    personaje_mas_bajo = buscar_primer_masculino()
    personaje_mas_bajo["altura"] = float(personaje_mas_bajo["altura"])

    for personaje in lista_personajes:    
        if(personaje["genero"] == "M"):
            personaje["altura"] = float(personaje["altura"])
            if(personaje_mas_bajo["altura"] > personaje["altura"]):
                personaje_mas_bajo = personaje       
        
    print(personaje_mas_bajo["nombre"])
    print(personaje_mas_bajo["altura"])


#--------------PERSONAJE MAS BAJO FEMENINO------------------------
def calcular_personaje_mas_bajo_femenino():
    personaje_mas_bajo = buscar_primer_femenino()
     
    personaje_mas_bajo["altura"] = float(personaje_mas_bajo["altura"])

    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if(personaje_mas_bajo["altura"] > personaje["altura"] and personaje["genero"]=="F"):
            personaje_mas_bajo = personaje
   
    print(personaje_mas_bajo["nombre"])      
    print(personaje_mas_bajo["altura"])


#--------------PROMEDIO ALTURAS MASCULINOS------------------------
def calcular_promedio_alturas_masculinos():
    acumulador_alturas_personajes = 0

    for personaje in lista_personajes:    
        if(personaje["genero"] == "M"):
            personaje["altura"] = float(personaje["altura"])
            acumulador_alturas_personajes = acumulador_alturas_personajes + personaje["altura"]
        
    print(acumulador_alturas_personajes/len(lista_personajes))

calcular_promedio_alturas_masculinos()

#--------------PROMEDIO ALTURAS FEMENINOS------------------------
def calcular_promedio_alturas_femeninos():
    acumulador_alturas_personajes = 0

    for personaje in lista_personajes:    
        if(personaje["genero"] == "F"):
            personaje["altura"] = float(personaje["altura"])
            acumulador_alturas_personajes = acumulador_alturas_personajes + personaje["altura"]
        
    print(acumulador_alturas_personajes/len(lista_personajes))

calcular_promedio_alturas_femeninos()


#--------------DETERMINAR CANTIDAD DE CADA COLOR OJOS------------------------
def determinar_cantidad_color_de_ojo():
    lista_color_ojos = [{"color":lista_personajes[0]["color_ojos"],"cantidad":0}]
    for personaje in lista_personajes:
        dic_color_ojos = {}
        flag = False
        for ojos in lista_color_ojos:
            if (personaje["color_ojos"] == ojos["color"]):
                ojos["cantidad"]+=1
                flag = True
            
        if (flag == False):
            dic_color_ojos = {"color":personaje["color_ojos"],"cantidad":1}
            lista_color_ojos.append(dic_color_ojos)

    return lista_color_ojos

#--------------DETERMINAR CANTIDAD DE CADA COLOR PELO------------------------
def determinar_cantidad_color_de_pelo():
    lista_color_pelos = [{"color":lista_personajes[0]["color_pelo"],"cantidad":0}]
    for personaje in lista_personajes:
        dic_color_pelos = {}
        flag = False
        for pelos in lista_color_pelos:
            if (personaje["color_pelo"] == pelos["color"]):
                pelos["cantidad"]+=1
                flag = True
            
        if (flag == False):
            dic_color_pelos = {"color":personaje["color_pelo"],"cantidad":1}
            lista_color_pelos.append(dic_color_pelos)
    
    return lista_color_pelos
    

#--------------DETERMINAR CANTIDAD DE CADA TIPO DE INTELIGENCIA------------------------
def determinar_cantidad_tipo_inteligencia():
    lista_tipo_inteligencia = [{"inteligencia":lista_personajes[0]["inteligencia"],"cantidad":0}]
    for personaje in lista_personajes:
        dic_tipo_inteligencia = {}
        flag = False
        for inteligencia in lista_tipo_inteligencia:
            if (personaje["inteligencia"] == inteligencia["inteligencia"]):
                inteligencia["cantidad"]+=1
                flag = True
            
        if (flag == False):
            dic_tipo_inteligencia = {"inteligencia":personaje["inteligencia"],"cantidad":1}
            lista_tipo_inteligencia.append(dic_tipo_inteligencia)

    for inteligencia in lista_tipo_inteligencia:
        if (inteligencia["inteligencia"]==""):
            inteligencia["inteligencia"]="No tiene"

    return lista_tipo_inteligencia

'''

#--------------LISTAR HEROES POR COLOR ------------------------
def lista_heroes_misma_caracteristica(lista:list,clave:str):
    lista_heroes_misma_caracteristica = []
    lista_ordenada_por_caracteristica = [{"caracteristica":lista[0][clave],"nombre_heroe":lista_heroes_misma_caracteristica}]
    

    for personaje in lista:
        flag = True
        for caracteristica in lista_ordenada_por_caracteristica:
            if (personaje[clave] == caracteristica["caracteristica"]):
                caracteristica["nombre_heroe"].append(personaje["nombre"])
                flag = False
        #el if tiene que estar por fuera del for
        if (flag == True):
            lista_heroes_misma_caracteristica = []
            dic_caracteristica_nombre = {"caracteristica":personaje[clave],"nombre_heroe":lista_heroes_misma_caracteristica}
            lista_ordenada_por_caracteristica.append(dic_caracteristica_nombre)

    #set_ordenado_por_caracteristica = set (lista_ordenada_por_caracteristica)
    #print(set_ordenado_por_caracteristica)    
    return lista_ordenada_por_caracteristica

print(lista_heroes_misma_caracteristica(lista_personajes,"color_pelo"))

'''def setear_caracteristica (lista:list,clave:str)->set:
    lista_de_caracteristica = []
    lista_de_caracteristica.append(lista[0][clave])
    for personaje in lista:
        for caracteristica in lista_de_caracteristica:
            if(personaje[clave]!=caracteristica):
                lista_de_caracteristica.append(personaje[clave])

    set_de_caracteristicas = set (lista_de_caracteristica)

    return set_de_caracteristicas

print(setear_caracteristica(lista_personajes,"color_pelo"))'''


         



    
    
    

'''



while (True):
    respuesta = input("\n1-Mostrar heroe más alto\n2-Mostrar heroe más bajo\n3-Mostrar promedio alturas\n4-Mostrar heroe más pesado\n5-Mostrar heroe más liviano\n6-Salir\n")
    if(respuesta == "1"):
        calcular_personaje_mas_alto()
    elif(respuesta == "2"):
        calcular_personaje_mas_bajo()
    elif(respuesta == "3"):
        calcular_promedio_alturas()
    elif(respuesta == "4"):
        calcular_personaje_mas_pesado()
    elif(respuesta == "5"):
        calcular_personaje_mas_liviano()
    elif(respuesta == "6"):
        break

'''