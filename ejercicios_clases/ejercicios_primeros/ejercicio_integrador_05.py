"""
Ejercicio Integrador 05

En la base de datos de la división de armamento de industrias Wayne se 
tiene una información la cual están con la necesidad de cambiar el formato 
la lista de habilidades con sus respectivos puntos de combate, actualmente 
cada una de ellas está presente como un diccionario pero para su nuevo sistema 
requieren que el tipo de dato sea una tupla la cual albergue solamente el nombre 
de la habilidad y su poder al estilo ("rayo laser", 99). A su vez, todas y cada una de 
las habilidades deben estar dentro de una lista de habilidades, la cual debe ser el 
valor de una key que conforme un diccionario, como key par albergarlas usaremos “habilidades_UTN”.

Formato de resultado esperado:
{
 "habilidades_UTN": [("habilidad_alfa", número), ("habilidad_beta", número)] etc.
}
Ordenar la lista de "habilidades_UTN" según el número de cada tupla, de manera ascendente. 
Una vez hecho esto, deberá recorrer dicha lista imprimiendo sus valores,  conjuntamente 
con la key que integra dicha estructura de datos.

EJEMPLO

habilidades_UTN:
Habilidad 1: habilidad_alfa | Poder: numero
Habilidad 2: habilidad_beta | Poder: numero
Etcétera.

"""

habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]

dic_habilidades_UTN = {}
lista_habilidades_UTN = []
for i in range(len(habilidades)):
    tupla_nombre_poder = (habilidades[i]["Nombre"] , habilidades[i]["Poder"])
    lista_habilidades_UTN.append(tupla_nombre_poder) 
    lista_ordenada_por_poder = sorted (lista_habilidades_UTN, 
    key=lambda habilidad:habilidad[1]) #funcion "sorted" ordena por la posicion 1 en la lista
    #print (tupla_nombre_poder)
    #print(habilidades[i]["Nombre"] , habilidades[i]["Poder"])

#print(lista_ordenada_por_poder)
dic_habilidades_UTN["Habilidades UTN"] = lista_ordenada_por_poder
print("'Habilidades UTN':\n ")
for i in range(len(lista_habilidades_UTN)):
    print("Habilidad {}:{} | Poder:{}\n ".format(i+1,
    dic_habilidades_UTN["Habilidades UTN"][i][0],
    dic_habilidades_UTN["Habilidades UTN"][i][1]))
 #print(dic_habilidades_UTN)