import json
import re
from operator import truediv

def cargar_json(ruta_al_archivo:str)->list:
    print("cargar json")
    with open(ruta_al_archivo,"r") as archivo:
        dic_del_archivo = json.load(archivo)
        
    return dic_del_archivo["clave_principal"]

def mostrar_lista_videos(lista_videos:list):
    for video in lista_videos:
        print("\nTitulo:{0} / Vistas:{1:.2f} M / Duracion:{2} Seg\n"
        .format(video["title"],video["views"],video["lenght"]))

def buscar_minimo(lista_videos:list,clave:str)->int:
    '''
    Busca un minimo en una lista de elementos dict
    Recibe una lista de elementos dic y un str que represneta la clave
    Devuelve un int que representa la posicion del minimo
    '''
    flag = True
    if (len(lista_videos)>0):
        flag = False
        indice_min = 0
        for indice in range(1,len(lista_videos)):
            if (lista_videos[indice][clave]<lista_videos[indice_min][clave]):
                indice_min = indice
        return indice_min
               
    return flag

def ordenar_lista_videos_up_down(lista_videos:list,clave:str,orden:str="down")->list:
    lista_a_ordenar = lista_videos.copy()
    lista_ordenada = []
    while(len(lista_a_ordenar)>0):
        indice_minimo = buscar_minimo (lista_videos,clave)
        lista_ordenada.append (lista_a_ordenar.pop(indice_minimo))
    
    if(orden=="up"):
        lista_ordenada = lista_ordenada.reverse()#metodo de listas que la da vuelta

    return lista_ordenada

def buscador_videos(lista_videos:list,patron_ingresado_por_usuario:str):
    print("\n")
    for video in lista_videos: 
        #re.search (" ",lista_videos["tile"],re.IGNORECASE) devuelve "match" o "none", si encuentra entra al if
        match = re.search(patron_ingresado_por_usuario,video["title"]),re.IGNORECASE
        if(match):
            titulo = video["title"]
            palabra = "[1;33m" + match.group(0) + "[1;33m"
            titulo.replace (match.group(0),palabra)
            print("\nTitulo:{0} / Vistas:{1:.2f} M / Duracion:{2} Seg\n"
            .format(titulo,video["views"],video["lenght"]))

def exportar_a_csv(lista_videos:list,direccion_archivo_nuevo:str):
    with open(direccion_archivo_nuevo,"w") as archivo:
        for video in lista_videos:
            archivo.write("{0},{1},{2}\n".format(video["title"],video["views"],video["lenght"]))