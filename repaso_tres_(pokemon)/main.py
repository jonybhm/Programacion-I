import string
from funciones import *
from validaciones import *

def menu_ppal_dex ():
    lista_pokemon = leer_json(r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\repaso_tres_(pokemon)\pokedex.json")

    while(True):
        mensaje = "1- Listar N cantidad de pokemons\n"
        mensaje += "2- Ordenar y listar pokemons por poder\n"
        mensaje += "3- Ordenar y listar pokemons por ID\n"
        mensaje += "4- Calcular promedio\n"
        mensaje += "5- Buscar pokemon por tipo\n"
        mensaje += "6- Exportar archivo\n"
        mensaje += "7- Salir\n>"

        respuesta_usuario = input(mensaje)

        if(respuesta_usuario == "1"):
            N_usuario = input("Ingrese un numero de pokemon a mostrar:\n")
            N_usuario = validar_entero(N_usuario)
            if (N_usuario > 0 and N_usuario < len(lista_pokemon)):
                desde = len(lista_pokemon)-N_usuario
                lista_a_exportar = lista_pokemon[desde:]
                mostrar(lista_a_exportar,"id")
            else:
                print("Ingrese un valor entre 1 y {0}\n".format(len(lista_pokemon)))

        elif(respuesta_usuario == "2"):
            orden_usuario = input("Desea ordear ascendente o descendente: asc/desc\n")
            orden_usuario = validar_string_asc_desc(orden_usuario)
            if (orden_usuario != "N/A"):
                lista_a_exportar = ordenar_asc_desc(lista_pokemon,"poder",orden_usuario)
                mostrar(lista_a_exportar,"poder")
            else:
                print("Ingrese 'asc' o 'desc':\n")

        elif(respuesta_usuario == "3"):
            orden_usuario = input("Desea ordear ascendente o descendente: asc/desc\n")
            orden_usuario = validar_string_asc_desc(orden_usuario)
            if (orden_usuario != "N/A"):
                lista_a_exportar = ordenar_asc_desc(lista_pokemon,"id",orden_usuario)
                mostrar(lista_a_exportar,"id")
            else:
                print("Ingrese 'asc' o 'desc':\n")

        elif(respuesta_usuario == "4"):
            clave_usuario = input("Que caracteristica desea calcular promedio:\npoder\nid\n")
            orden_usuario = input("Desea listar valores menores o mayores al promedio: menor/mayor\n")
            orden_usuario = validar_string_mayor_menor(orden_usuario)
            if (orden_usuario != "N/A"):
                lista_a_exportar = listar_valores_menor_mayor_prom(lista_pokemon,clave_usuario,orden_usuario)
                mostrar(lista_a_exportar,clave_usuario)
            else:
                print("Ingrese 'menor' o 'mayor':\n")

        elif(respuesta_usuario == "5"):
            tipo_usuario = input("Ingrese un tipo de pokemon a buscar:\n")
            tipo_usuario = validar_string(tipo_usuario)
            if (tipo_usuario != "N/A"):
                lista_a_exportar = buscar_por_tipo(lista_pokemon,tipo_usuario)
                mostrar(lista_a_exportar,"tipo")
        elif(respuesta_usuario == "6"):
            exportar_a_csv(lista_a_exportar,
            r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\repaso_tres_(pokemon)\pokedex.csv")

        elif(respuesta_usuario == "7"):
            break

menu_ppal_dex ()