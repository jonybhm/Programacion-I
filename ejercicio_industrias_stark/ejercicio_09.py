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
            if (definir_iniciales_nombre(lista_heroes) == False):
                print("El origen de datos no contiene el formato correcto")
                break
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

#agrego la clave "id" que refiere a la posicion en la lista
index = 0
for personaje in lista_personajes:
    personaje["id"] = index
    index += 1
    

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
    


