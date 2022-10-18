'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
'''
{
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    "gender": "male"
}
'''
import functools
import funciones

def starwars_app():
    '''
    Muestra un menu interactivo para el usuario
    Return none
    '''
    lista_personajes = funciones.cargar_json(r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\PP_STARWARS\data.json")
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            lista_a_mostrar = lista_personajes.copy()
            lista_a_mostrar.sort(key=lambda altura:float(altura["height"]))
            funciones.mostrar(lista_a_mostrar,"height")

        elif(respuesta=="2"):
            lista_dos = list(filter(lambda personaje:personaje["gender"]=="female",lista_personajes))
            lista_a_mostrar = functools.reduce (lambda personaje,maximo : maximo if float(maximo["height"])>float(personaje["height"]) else personaje,
            lista_dos)
            funciones.mostrar(lista_a_mostrar,"height")
            
        elif(respuesta=="3"):
            lista_a_mostrar = funciones.ordenar_lista(lista_personajes,"mass")
            funciones.mostrar(lista_a_mostrar,"mass")

        elif(respuesta=="4"):
            nombre_usuario = input("Ingrese un nombre a buscar:\n")
            funciones.buscar_personaje_en_lista(lista_personajes,nombre_usuario)
            
        elif(respuesta=="5"):
            funciones.exportar_a_csv(lista_a_mostrar,
            r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\PP_STARWARS\data.csv")

        elif(respuesta=="6"):
            break


starwars_app()

