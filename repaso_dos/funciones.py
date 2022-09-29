import json
import re

'''
{
"nombre": "Howard the Duck",
"identidad": "Howard (Last name unrevealed)",
"altura": 79.35,
"peso": 18.45,
"fuerza": 2,
"inteligencia": ""
}
'''

#------------------------IMPORTAR DESDE ARCHIVO JSON------------------------

def leer_json(ruta_al_archivo:str)->list:
    '''
    Carga de un archivo tipo json la informacion del mismo
    Recivo un string que muestra la ruta del archivo json
    Devuelve una lista con la informacion del json
    '''
    with open(ruta_al_archivo,"r") as archivo:
        lista_de_dic_del_archivo = json.load (archivo)
    
    return lista_de_dic_del_archivo["heroes"]


#------------------------MOSTRAR ELEMENTOS DE LA LISTA POR NOMBRE Y VALOR ------------------------

def mostrar (lista:list,clave:str):
    '''
    La funcion imprime en pantalla una lista solo con una clave y los nombres de los heroes correspondientes
    Recibe una lista original y un str que representa una clave
    '''
    for elemento in lista:
        print("{0}: {1}/Heroe: {2}".format(clave,elemento[clave],elemento["nombre"]))


#------------------------LISTAR HEROES ------------------------

def listar_heroes(lista_heroes:list):
    '''
    La funcion imprime los heroes de la lista
    Recibe una lista con los diccionarios 
    No devuelve nada
    '''
    for heroe in lista_heroes:
        print("\nNombre:{0} / Identidad: {1} / Altura: {2} cm / Peso: {3} kg / Fuerza: {4} N / Inteligencia: {5}"
        .format(heroe["nombre"],heroe["identidad"],heroe["altura"],heroe["peso"],heroe["fuerza"],heroe["inteligencia"]))


    
#------------------------CALCULAR MINIMO ------------------------

def calcular_indice_minimo(lista_heroes:list,clave:str)->int:
    '''
    Calcula el minimo de una lista dada una clave de referencia
    Recibe la lista de diccionarios un str que representa a la clave
    Devuelve un entero que representa la posicion del minimo en la lista, devuelve -1 en caso de ser una lista vacia
    '''
    indice_min = 0
    for indice in range(len(lista_heroes)):
        if(lista_heroes[indice][clave] < lista_heroes[indice_min][clave]):
            indice_min = indice
    return indice_min

lista_heroes_orignal = leer_json(r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\repaso_dos\data_stark.json")
  

#------------------------ORDENAR MODO ASCENDENTE Y DESCENDENTE ------------------------


def ordenar_updown_downup (lista_heroes:list,clave:str,orden:str="asc")->list:
    '''
    Ordena la lista de menor a mayor o viceverza 
    Recibe la lista de heroes, un str que representa la clave y un str que representa el tipo de ordenamiento
    Devuelve la lista ordenada segun lo indicado
    '''
    lista_a_ordenar = lista_heroes.copy()
    lista_ordenada = []
    while (len(lista_a_ordenar)>0):
        indice_minimo = calcular_indice_minimo(lista_a_ordenar,clave)
        elemento = lista_a_ordenar.pop(indice_minimo)
        lista_ordenada.append(elemento)
    if (orden=="desc"):
        lista_ordenada.reverse()

    return lista_ordenada


#------------------------CALCULAR PROMEDIO ------------------------

def calcular_promedio (lista_heroes:list,clave:str,condicion_promedio:str)->list:
    '''
    La funcion calcula el promdeio de cualquier clave numerica
    Recibe la lista de heroes, un str que representa la clave y un str con la condicion de si supera o no supera al mismo
    Devuelve una lista ordenada con las valores que superen o no al promedio
    '''
      
    contador = 0
    acumulador = 0
    for heroe in lista_heroes:
        acumulador += heroe[clave]
        contador += 1
    promedio = acumulador / contador
    lista_valores_en_relacion_al_promedio = []
    if(condicion_promedio == "mayor"):
        for heroe in lista_heroes:
            if (heroe[clave]>promedio):
                lista_valores_en_relacion_al_promedio.append(heroe)
    elif(condicion_promedio == "menor"):
        
        for heroe in lista_heroes:
            if (heroe[clave]<promedio):
                lista_valores_en_relacion_al_promedio.append(heroe)    
                     
    return lista_valores_en_relacion_al_promedio

#------------------------BUSCAR POR TIPO DE INTELIGENCIA ------------------------

def buscar_por_inteligencia (lista_heroes:list,tipo_inteligencia:str):
    '''
    Busca y lista heroes por inteligencia
    Recibe la lista de heroes y un str que representa el tipo de inteligencia
    '''
    print("\n")
    for heroe in lista_heroes:
        match = re.search(tipo_inteligencia,heroe["inteligencia"],re.IGNORECASE)
        if (match):
            nombre_heroe = heroe["nombre"]
            print ("\nNombre: {0}".format(nombre_heroe))
        
    

#------------------------EXPORTAR LISTA A ARCHIVO CSV ------------------------

def expotar_a_archivo_csv(lista_heroes_segun_opcion:list,nombre_y_ruta_archivo:str):
    with open(nombre_y_ruta_archivo,"w") as archivo:
        for heroe in lista_heroes_segun_opcion:
            archivo.write("{0},{1},{2},{3},{4},{5}\n"
            .format(heroe["nombre"],heroe["identidad"],heroe["altura"]
            ,heroe["peso"],heroe["fuerza"],heroe["inteligencia"]))

