from data_stark import lista_personajes


'''{
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  }'''

#--------------PERSONAJE MAS ALTO------------------------
def calcular_personaje_mas_alto():
    personaje_mas_alto = lista_personajes[0]
    personaje_mas_alto["altura"] = float(personaje_mas_alto["altura"])

    for personaje in lista_personajes:    
        personaje["altura"] = float(personaje["altura"])
        if(personaje_mas_alto["altura"] < personaje["altura"]):
            personaje_mas_alto = personaje       

    print(personaje_mas_alto["nombre"])      
    print(personaje_mas_alto["altura"])

#--------------PERSONAJE MAS BAJO------------------------
def calcular_personaje_mas_bajo():
    personaje_mas_bajo = lista_personajes[0]
    personaje_mas_bajo["altura"] = float(personaje_mas_bajo["altura"])

    for personaje in lista_personajes:    
        personaje["altura"] = float(personaje["altura"])
        if(personaje_mas_bajo["altura"] > personaje["altura"]):
            personaje_mas_bajo = personaje       
        
    print(personaje_mas_bajo["nombre"])
    print(personaje_mas_bajo["altura"])

#--------------PROMEDIO ALTURAS------------------------
def calcular_promedio_alturas():
    acumulador_alturas_personajes = 0

    for personaje in lista_personajes:    
        personaje["altura"] = float(personaje["altura"])
        acumulador_alturas_personajes = acumulador_alturas_personajes + personaje["altura"]
        
    print(acumulador_alturas_personajes/len(lista_personajes))

#--------------PERSONAJE MAS PESADO------------------------
def calcular_personaje_mas_pesado():
    personaje_mas_pesado = lista_personajes[0]
    personaje_mas_pesado["peso"] = float(personaje_mas_pesado["peso"])

    for personaje in lista_personajes:    
        personaje["peso"] = float(personaje["peso"])
        if(personaje_mas_pesado["peso"] < personaje["peso"]):
            personaje_mas_pesado = personaje       

    print(personaje_mas_pesado["nombre"])      
    print(personaje_mas_pesado["peso"])

#--------------PERSONAJE MAS LIVIANOs------------------------
def calcular_personaje_mas_liviano():
    personaje_mas_liviano = lista_personajes[0]
    personaje_mas_liviano["peso"] = float(personaje_mas_liviano["peso"])

    for personaje in lista_personajes:    
        personaje["peso"] = float(personaje["peso"])
        if(personaje_mas_liviano["peso"] > personaje["peso"]):
            personaje_mas_liviano = personaje       
        
    print(personaje_mas_liviano["nombre"])
    print(personaje_mas_liviano["peso"])


while (True):
    respuesta = input("\n1-Mostrar heroe más alto\n2-Mostrar heroe más bajo\n3-Mostrar promedio alturas\n4-Mostrar heroe más pesado\n5-Mostrar heroe más liviano\n6-Salir\n")
    if(respuesta == "1"):
        calcular_personaje_mas_alto()
    elif(respuesta == "2"):
        calcular_personaje_mas_bajo()
    elif(respuesta == "3"):
        calcular_promedio_alturas()
    elif(respuesta == "4"):
        calcular_personaje_mas_pesado()
    elif(respuesta == "5"):
        calcular_personaje_mas_liviano()
    elif(respuesta == "6"):
        break