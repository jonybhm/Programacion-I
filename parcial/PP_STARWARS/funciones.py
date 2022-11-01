import re
import json

'''
{
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    "gender": "male"
}
'''


def cargar_json(ruta_archivo:str)->list:
    '''
    Carga un archivo json en formato dict
    Recibe un str que representa la ruta del archivo json
    Devuelve un list que contiene diccionarios con informacion 
    '''
    with open(ruta_archivo,"r") as archivo:
        dic_archivo = json.load(archivo)

    return dic_archivo["results"]

#lista_prueba = cargar_json(r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\PP_STARWARS\data.json")


def mostrar(lista_personajes:list,clave:str):
    '''
    Imprime en pantalla los datos que se le pasen, el nombre y cualquier otra clave
    Recibe una lista con los personajes a mostrar y un str que representa la clave a mostrar
    No devuelve nada
    '''
    for personaje in lista_personajes:
        print("Nombre:{0} / {1}:{2}\n".format(personaje["name"],clave,personaje[clave]))

def buscar_indice_max(lista_personajes:list,clave:str)->int:
    '''
    Busca el indice donde este valor maximo de acuerdo a la clave que se la pase
    Recibe una lista de personajes y un str que representa la clave a comparar
    Devuelve un int que representa la posicion en la lista donde se encuentra el maximo
    '''
    i_max = 0
    for i in range(len(lista_personajes)):
        lista_personajes[i][clave] = int(lista_personajes[i][clave])
        lista_personajes[i_max][clave] = int(lista_personajes[i_max][clave])
        if(lista_personajes[i][clave]>lista_personajes[i_max][clave]):
            i_max = i
    return i_max

def listar_por_genero(lista_personajes:list,genero:str)->list:
    '''
    Busca en una lista de personajes y junta por clave genero
    Recibe una lista de personajes, un str que representa el genero
    Devuelve una lista con personajes del mismo genero
    '''
    lista_mismo_genero = []
    for personaje in lista_personajes:
        if(personaje["gender"]==genero):
            lista_mismo_genero.append(personaje)
    return lista_mismo_genero

def listar_max_por_genero (lista_personajes:list,clave:str="height")->list:
    '''
    Lista por clave los maximos de cada genero
    Recibe una lista de personajes y un str que representa la clave ("height" es por defecto)
    Devuelve una lista con los maximos representantes de cada genero
    '''
    lista_mas_altos = []
    
    lista_mas_alto_masculino = listar_por_genero(lista_personajes,"male")
    mas_alto_masculino = lista_mas_alto_masculino[buscar_indice_max(lista_mas_alto_masculino,clave)]
    lista_mas_altos.append(mas_alto_masculino)
    
    lista_mas_alto_femenino = listar_por_genero(lista_personajes,"female")
    mas_alto_femenino = lista_mas_alto_femenino[buscar_indice_max(lista_mas_alto_femenino,clave)]
    lista_mas_altos.append(mas_alto_femenino)

    lista_mas_alto_n_a = listar_por_genero(lista_personajes,"n/a")
    mas_alto_n_a = lista_mas_alto_n_a[buscar_indice_max(lista_mas_alto_n_a,clave)]
    lista_mas_altos.append(mas_alto_n_a)

    return lista_mas_altos

def ordenar_lista(lista_personajes:list,clave:str)->list:
    '''
    Ordena la lista de personajes en relacion al indice maximo y la clave que se le pase
    Recibe la lista de personajes y un str que representa la clave
    Devuelve una lista con los personajes ordenados
    '''
    lista_a_ordenar = lista_personajes.copy()
    i_max = 0
    for i in range(len(lista_a_ordenar)):
        i_max = buscar_indice_max(lista_a_ordenar[i:],clave) + i
        lista_a_ordenar[i],lista_a_ordenar[i_max] = lista_a_ordenar[i_max],lista_a_ordenar[i]
    
    return lista_a_ordenar


def buscar_personaje_en_lista(lista_personajes:list,nombre:str):
    '''
    Busca un personaje en la lista de personajes en base al nombre
    Recibe una lista de personajes y un str que representa el nombre del personaje
    No devuelve nada
    '''
    lista_nombres_coincidentes = []
    se_encontro = False
    for personaje in lista_personajes:
        resultado_match = re.search(nombre,personaje["name"],re.IGNORECASE)
        if (resultado_match):
            se_encontro = True
            print("Nombre:{0}/Altura:{1}/Peso:{2}/Genero:{3}\n"
            .format(personaje["name"],personaje["height"],personaje["mass"],personaje["gender"]))
    if(se_encontro == False):
        print("No se encontro coincidencias\n")
   
    return lista_nombres_coincidentes

def exportar_a_csv(lista_personajes:list,ruta_archivo:str):
    '''
    Exporta una lista a un archivo csv
    Recibe la lista a exportar y un str que representa la ruta del archivo
    No devuelve nada
    '''
    with open(ruta_archivo,"w") as archivo:
        for personaje in lista_personajes:
            archivo.write("{0},{1},{2},{3}\n".format(personaje["name"],personaje["height"],personaje["mass"],personaje["gender"]))