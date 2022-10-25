lista = [14,5,20,10,23,15,7,16,29,21,-102,99,0]

def buscar_minimo(lista_con_valores:list):
    indice_valor_minimo = 0
    indice_iteracion = -1
    for valor in lista_con_valores:
        indice_iteracion += 1
        if(lista_con_valores[indice_valor_minimo] > valor):
            indice_valor_minimo = indice_iteracion
    
    return indice_valor_minimo

#print (lista[buscar_minimo(lista)])    

def ordenar_lista (lista_original:list)->list:
    lista_para_ordenar = lista_original.copy()
    lista_ordenada = []
    while (len(lista_para_ordenar)>0):
        indice_valor_minimo = buscar_minimo(lista_para_ordenar)
        lista_ordenada.append(lista_para_ordenar.pop(indice_valor_minimo))#.pop retorna el valor de la lista y lo elimina de la misma 

    
    return lista_ordenada

print(ordenar_lista(lista))

def ordenar_lista_metodo_swap(lista_original:list)->list:
    lista_a_ordenar = lista_original.copy()
    flag = True #es True si hubo un cambio de lugares entre valores
    lim = 1 #este valor va aumentado a medida que cambio de numero a comparar, asi no se pasa del limite de la lista
    while (flag == True):
        flag = False
        for i in range(len(lista_a_ordenar) - lim):
            if (lista_a_ordenar[i]>lista_a_ordenar[i+1]):
                lista_a_ordenar[i+1],lista_a_ordenar[i]=lista_a_ordenar[i],lista_a_ordenar[i+1] #intercambiar valores en python
                '''buffer = lista_a_ordenar[i]
                lista_a_ordenar [i] = lista_a_ordenar[i+1]                 
                lista_a_ordenar [i+1] = buffer''' #otro metodo para interacambiar valores
                flag = True
        lim += 1
    return lista_a_ordenar

#print(ordenar_lista_metodo_swap(lista))

def ordenar_lista_metodo_quick_sort(lista_original:list)->list:
    lista_a_ordenar = lista_original.copy()
    derecha_valores_mayores = []
    izquierda_valores_menores = []
    indice_mitad_lista = len(lista_a_ordenar)/2
    pivote = lista_a_ordenar[int(indice_mitad_lista)]
    for valor in lista_a_ordenar:
        if (valor < pivote):
            izquierda_valores_menores.append(valor)
        elif (valor > pivote):
            derecha_valores_mayores.append(valor)
    
    print (derecha_valores_mayores)
    print (izquierda_valores_menores)

#ordenar_lista_metodo_quick_sort(lista)


def ordenar_metodo_nahuel_mejorado(lista_original:list):
    lista_ordenada = lista_original.copy()

    for i in range(len(lista_ordenada)):
        indice_min = buscar_minimo(lista_original[i:]) + i #[i:] compara desde la posicion en adelante
        lista_ordenada[i],lista_ordenada[indice_min] = lista_ordenada[indice_min],lista_ordenada[i]

    return lista_ordenada

print(ordenar_metodo_nahuel_mejorado(lista))