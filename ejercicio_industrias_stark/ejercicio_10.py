import re
import json
from ejercicio_07 import buscar_primer_personaje_por_genero 
from ejercicio_07 import recorrer_lista_personajes_por_genero
from ejercicio_07 import calcular_personaje_mas_alto_bajo_por_genero
from ejercicio_07 import calcular_promedio_alturas_por_genero
from ejercicio_07 import determinar_cantidad_caracteristica
from ejercicio_07 import listar_heroes_misma_caracteristica
from ejercicio_07 import imprimir_menu_desafio_5
from ejercicio_07 import stark_menu_principal_desafio_5
from data_stark import lista_personajes


def leer_archivo(archivo_extension:str)->dict:
    dic_json = {}
    with open (archivo_extension,"r") as archivo:
        dic_json = json.load(archivo)
    return dic_json["heroes"]

#data_stark = leer_archivo(r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\ejercicio_archivos\data_stark.json")
#stark_menu_principal_desafio_5(data_stark)
#C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\ejercicio_archivos\data_stark.json

def guardar_archivo (archivo_extension:str,lista_con_contenido:list)->bool:
    with open(archivo_extension,"w") as archivo:
        for contenido in lista_con_contenido:
            linea_archivo = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}\n".format(contenido["nombre"]            
            ,contenido["identidad"],contenido["empresa"],contenido["altura"],contenido["peso"]
            ,contenido["genero"],contenido["color_ojos"],contenido["color_pelo"],contenido["fuerza"],contenido["inteligencia"])
            archivo.write(linea_archivo)
            
        
#guardar_archivo(r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\ejercicio_archivos\data_stark_2.csv",lista_personajes)


'''
 Crear la función 'capitalizar_palabras' la cual recibirá por parámetro un
string que puede contener una o muchas palabras. La función deberá
retornar dicho string en el cual todas y cada una de las palabras que
contenga, deberán estar capitalizadas (Primera letra en mayúscula).
'''

def capitalizar_palabra(patron:str):
    patron_capitalized = patron.capitalize()
    return patron_capitalized

#print(capitalizar_palabra("hola mi nombre"))

'''
Crear la función 'obtener_nombre_capitalizado' la cual recibirá por
parámetro un diccionario el cual representará a un héroe y devolverá
un string el cual contenga su nombre formateado de la siguiente
manera:
Nombre: Venom
Reutilizar 'capitalizar_palabras
'''

