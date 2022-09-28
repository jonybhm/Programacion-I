'''
1-Listar TOP N videos
2-Ordenar videos por duracion (UP/DOWN)
3-Ordenar videos por cantidad de views (UP/DOWN)
4-Buscar videos por título
5-Exportar lista de videos a CSV
6-Salir

'''
#import funciones -> funciones.cargar_json()
#from funciones import cargar_json
from sys import int_info
from funciones import * #importa todas las funciones
#1° ARMAR UN MENU

def app_principal():
    lista_videos = cargar_json("ruta del archivo")
    while (True):
        mensaje = "1-Listar TOP N videos\n"
        mensaje += "2-Ordenar videos por duracion (UP/DOWN)\n"
        mensaje += "3-Ordenar videos por cantidad de views (UP/DOWN)\n"
        mensaje += "4-Buscar videos por título\n"
        mensaje += "5-Exportar lista de videos a CSV\n"
        mensaje += "6-Salir\n>"
            
        respuesta = input (mensaje)
        if(respuesta == "1"):
            
            print ("1-Listar TOP N videos\n")

            top = int(input("\nCantidad de elementos a mostrar\n"))
            #validar que sea un entero y dentro de la cantidad de elementos de la lista, usar bibilioteca de validaciones
            while(type(top)!=type(int()) and top > len(lista_videos)):
                top = int(input("\nCantidad de elementos a mostrar debe ser entero\n"))
            mostrar_lista_videos(lista_videos[:top])

        elif(respuesta == "2"):

            print ("2-Ordenar videos por duracion (UP/DOWN)\n")

        elif(respuesta == "3"):
            
            print ("Ordenar videos por cantidad de views (UP/DOWN)\n")
        
        elif(respuesta == "4"):
            
            print ("4-Buscar videos por título\n")
        
        elif(respuesta == "5"):
            
            print ("5-Exportar lista de videos a CSV\n")
        
        elif(respuesta == "6"):
            
            print ("6-Salir\n")
            break

app_principal()