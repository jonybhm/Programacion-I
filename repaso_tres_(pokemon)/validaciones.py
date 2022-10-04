import re

def validar_entero(numero_str:str)->int:
    '''
    la funcion analiza si el dato es numerico entero, positico o negativo
    Recibe un str que representa un numero
    Devuelve el numero en formato int sin espacios,si es no numerico = -1 , negativo = -2, otro error = -3
    '''
    es_numero_entero = re.findall("[0-9]+",numero_str)
    lista_con_no_numericos = re.findall("([a-zA-Z]+)",numero_str)
    lista_con_negativos = re.findall("-([0-9]+)",numero_str)
    
    if(len(es_numero_entero) > 0 and len(lista_con_negativos) == 0
    and len(lista_con_no_numericos) == 0):
        numero = int (es_numero_entero[0]) 
    else:
        
        if(len(lista_con_no_numericos) > 0):
            numero = -1        
        elif(len(lista_con_negativos) > 0):
            numero = -2
        else:
            numero = -3
    return numero

def validar_flotante(numero_str:str)->float:
    '''
    la funcion analiza si el dato es numerico flotante, positico o negativo
    Recibe un str que representa un numero
    Devuelve el numero en formato int sin espacios,si es no numerico = -1 , negativo = -2, otro error = -3
    '''
    es_numero_flotante = re.findall("[0-9]+.[0-9]+",numero_str) #"[0-9]+.[0-9]+" numero flotante
    lista_con_no_numericos = re.findall("([a-zA-Z]+)",numero_str)
    lista_con_negativos = re.findall("-([0-9]+.[0-9]+)",numero_str)
    
    if(len(es_numero_flotante) > 0 and len(lista_con_negativos) == 0 
    and len(lista_con_no_numericos) == 0):
        numero = float (es_numero_flotante[0]) 
        
    else:
        
        if(len(lista_con_no_numericos) > 0):
            numero = -1         
        elif(len(lista_con_negativos) > 0):
            numero = -2 
        else:
            numero = -3  
    return numero

def validar_string_asc_desc (valor_str:str,valor_por_defecto = "-")->str:
    '''
    La funcion verifica el valor si es un string sin numeros,en caso de tener barras las reemplaza por espacios
    Recibe un valor en str
    Devuelve el valor sanitizado 
    '''
    posee_numero = re.findall("[0-9]+",valor_str)
    str_sin_numeros = re.match(r"asc|desc",valor_str)
    if (str_sin_numeros and len(posee_numero) == 0):
        str_valor = valor_str
        str_valor = str_valor.replace("/"," ")
        str_valor = str_valor.lower()
                
    else:
        str_valor = "N/A"
    
    return str_valor

def validar_string_mayor_menor (valor_str:str,valor_por_defecto = "-")->str:
    '''
    La funcion verifica el valor si es un string sin numeros,en caso de tener barras las reemplaza por espacios
    Recibe un valor en str
    Devuelve el valor sanitizado 
    '''
    posee_numero = re.findall("[0-9]+",valor_str)
    str_sin_numeros = re.match(r"mayor|menor",valor_str)
    if (str_sin_numeros and len(posee_numero) == 0):
        str_valor = valor_str
        str_valor = str_valor.replace("/"," ")
        str_valor = str_valor.lower()
                
    else:
        str_valor = "N/A"
    
    return str_valor

def validar_string (valor_str:str,valor_por_defecto = "-")->str:
    '''
    La funcion verifica el valor si es un string sin numeros,en caso de tener barras las reemplaza por espacios
    Recibe un valor en str
    Devuelve el valor sanitizado 
    '''
    posee_numero = re.findall("[0-9]+",valor_str)
    str_sin_numeros = re.findall("[a-zA-Z/ ]+",valor_str)
    if (len(str_sin_numeros) > 0 and len(posee_numero) == 0):
        str_valor = str_sin_numeros[0]
        str_valor = str_valor.replace("/"," ")
        str_valor = str_valor.lower()
                
    else:
        str_valor = "N/A"
    
    return str_valor