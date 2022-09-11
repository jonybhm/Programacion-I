'''
Crear la función “validar_entero” la cual recibirá por parámetro un string de número el
cual deberá verificar que sea sea un string conformado únicamente por dígitos.
Retornara True en caso de serlo, False caso contrario
'''
def validar_entero(numero:str)->bool:

    flag = False
    if(numero.isdigit):
        flag = True
    
    return flag

print(validar_entero("5"))