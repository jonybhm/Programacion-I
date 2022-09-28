for i in range(3):   

    respuesta = input("Ingrese un numero:")
    respuesta=int(respuesta)
    
    if(respuesta<=10):
        print("Su numero es menor o igual a 10")
    elif(respuesta>10 and respuesta<=20):
        print("Su numero es menor a 20")
    else:
        print("su numero es mayor a 20")