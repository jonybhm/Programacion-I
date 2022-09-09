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
'''
def stark_normalizar_datos (lista_heroes:list)->list:
    
    
    Castea los datos a sus tipos correspondietes
    Recibe la lista de datos 
    Devuelve la misma lista con datos casteados
    
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

print(stark_normalizar_datos(lista_personajes))
'''


def obtener_nombre (dic_heroe:dict)->str:
    nombre_heroe = "Nombre: {0}".format(dic_heroe["nombre"])
    
    '''
    Transforma el value de la clave "nombre" a un str 
    Recibe el diccionario que se encuentra dentro de la lista
    Devuelve un str con el formato "Nombre: ..."
    '''
    
    return nombre_heroe


    


def imprimir_dato (dato:str):
    print (dato)

def stark_imprimir_nombres_heroes (lista_heroes:list):
    
    for personaje in lista_heroes:
        imprimir_dato(obtener_nombre(personaje))

stark_imprimir_nombres_heroes(lista_personajes)
