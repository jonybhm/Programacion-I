from data_stark import lista_personajes
from calculos_01 import stark_normalizar_datos
from calculos_01 import obtener_nombre
from calculos_01 import imprimir_dato
from calculos_01 import stark_imprimir_nombres_heroes

stark_imprimir_nombres_heroes(lista_personajes)

'''
Crear la función “validar_entero” la cual recibirá por parámetro un string de número el
cual deberá verificar que sea sea un string conformado únicamente por dígitos.
Retornara True en caso de serlo, False caso contrario
'''
def validar_entero(numero:str)->bool:
    flag = False
    if (type(numero)==str()):
        flag = True

    return flag

print(validar_entero("5.5"))