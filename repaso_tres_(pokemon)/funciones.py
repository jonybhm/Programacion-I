import json
import re
'''
{
    "id": 1,
    "nombre": "bulbasaur",
    "tipo": ["planta"],
    "evoluciones": ["ivysaur", "venusaur"],
    "poder": 4,
    "fortaleza":["agua"],
    "debilidad":["fuego"]
}
'''

def leer_json(ruta_archivo:str)->list:
    with open(ruta_archivo,"r") as archivo:
        dic_contenido_archivo = json.load(archivo)

    return dic_contenido_archivo["pokemones"]

#lista_prueba = leer_json(r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\repaso_tres_(pokemon)\pokedex.json")

def mostrar (lista:list,clave:str):
    for pokemon in lista:
        print("Pokemon: {0}/{1}: {2}".format(pokemon["nombre"],clave,pokemon[clave]))

def listar_valores (lista_pokemon:list):
    for pokemon in lista_pokemon:
        print("{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}"
        .format(pokemon["id"],pokemon["nombre"],pokemon["tipo"],pokemon["evoluciones"],
        pokemon["poder"],pokemon["fortaleza"],pokemon["debilidad"]))

def buscar_indice_minimo(lista_pokemon:list,clave:str):
    indice_min=-1
    if (len(lista_pokemon)>0):
        indice_min = 0
        for indice in range(len(lista_pokemon)):
            if(lista_pokemon[indice][clave]<lista_pokemon[indice_min][clave]):
                indice_min=indice

    return indice_min


def ordenar_asc_desc (lista_pokemon:list,clave:str,orden:str="asc")->list:
    lista_a_ordenar = lista_pokemon.copy()
    i_min = 0
    for i in range(len(lista_a_ordenar)):
        i_min = buscar_indice_minimo(lista_a_ordenar[i:],clave) + i
        lista_a_ordenar[i],lista_a_ordenar[i_min] = lista_a_ordenar[i_min],lista_a_ordenar[i]

    if(orden == "desc"):
        lista_a_ordenar.reverse()

    return lista_a_ordenar

def calcular_promedio (lista_pokemon:list,clave:str,)->float:
    contador = 0
    acumulador = 0
    for pokemon in lista_pokemon:
        acumulador += pokemon[clave]
        contador += 1
    promedio = acumulador/contador
    return promedio

def listar_valores_menor_mayor_prom (lista_pokemon:list,clave:str,tipo_prom:str="menor")->list:
    promedio = calcular_promedio (lista_pokemon,clave)
    lista_mostrar = []
    if(tipo_prom=="menor"):
        for pokemon in lista_pokemon:
            if(promedio>pokemon[clave]):
                lista_mostrar.append(pokemon)
    elif(tipo_prom=="mayor"):
        for pokemon in lista_pokemon:
            if(promedio<pokemon[clave]):
                lista_mostrar.append(pokemon)    
    return lista_mostrar

def buscar_por_tipo (lista_pokemon:list,tipo:str)->list:
    lista_tipo = []
    for pokemon in lista_pokemon:
        tipo_pokemon = ""
        for tipos in pokemon["tipo"]:
            tipo_pokemon += tipos
        match_tipo = re.match(tipo,tipo_pokemon,re.IGNORECASE)
        if (match_tipo):
            lista_tipo.append(pokemon)
    
    return lista_tipo


def exportar_a_csv(lista_pokemon:list,ruta_nombre_archivo:str):
    with open(ruta_nombre_archivo,"w") as archivo:
        for pokemon in lista_pokemon:
            archivo.write("{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}"
            .format(pokemon["id"],pokemon["nombre"],pokemon["tipo"],pokemon["evoluciones"],
            pokemon["poder"],pokemon["fortaleza"],pokemon["debilidad"]))
