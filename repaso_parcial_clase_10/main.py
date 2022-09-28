from validaciones import *
from funciones import *



def menu_principal():
    lista_heroes = leer_json(r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\repaso_dos\data_stark.json")
    
    while(True):
        mensaje = "\n1. Listar los primeros N héroes.\n"
        mensaje += "2. Ordenar y Listar héroes por altura.\n"
        mensaje += "3. Ordenar y Listar héroes por fuerza.\n"
        mensaje += "4.Calcular promedio\n"
        mensaje += "5. Buscar y Listar héroes por inteligencia.\n"
        mensaje += "6. Exportar a CSV la lista de héroes ordenada.\n"
        mensaje += "7. Salir\n>"

        opcion_usuario = input (mensaje)

        if (opcion_usuario == "1"):
            N_del_usuario = input("\nIngrese una cantidad de heroes a mostrar")
            N_del_usuario = int(N_del_usuario) #preguntar por la validacion
            lista_opcion = lista_heroes[:N_del_usuario]
            listar_heroes (lista_opcion)
        elif (opcion_usuario == "2"):
            orden_usuario = input ("\ningrese un tipo de orden: asc/desc\n>")
            lista_opcion = ordenar_updown_downup(lista_heroes,"altura",orden_usuario)
            mostrar (lista_opcion,"altura")
        elif (opcion_usuario == "3"):
            orden_usuario = input ("\ningrese un tipo de orden: asc/desc\n>")
            lista_opcion = ordenar_updown_downup(lista_heroes,"fuerza",orden_usuario)
            mostrar (lista_opcion,"fuerza")
        elif (opcion_usuario == "4"):
            clave_usuario = input ("\ningrese un tipo de clave numerica: \nfuerza\naltura\npeso\n>")
            condicion_usuario = input ("\ningrese un tipo de orden: menor/mayor\n")
            lista_opcion = calcular_promedio(lista_heroes,clave_usuario,condicion_usuario)
            mostrar (lista_opcion,clave_usuario)
        elif (opcion_usuario == "5"):
            inteligencia_usuario = input ("\nIngrese un tipo de inteligencia: \ngood\naverage\nhigh\n>")
            buscar_por_inteligencia(lista_heroes,inteligencia_usuario)
        elif (opcion_usuario == "6"):
            expotar_a_archivo_csv(lista_opcion,r"C:\Users\JONY\Desktop\Programación\1 er cuatrimestre\Programacion-I\repaso_dos\data_stark.csv")
        elif (opcion_usuario == "7"):
            break

menu_principal()