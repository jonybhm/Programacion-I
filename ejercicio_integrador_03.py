"""
Jonathan De Castro 1°H
Ejercicio Integrador 03

La división de alimentos de industrias Wayne está trabajando en un pequeño software
para cargar datos de heroínas y héroes, para para tener un control de las condiciones de heroes existentes, nos solicitan:
Nombre de Heroína/Héroe
EDAD (mayores a 18 años)
Sexo ("m", "f" o "nb")
Habilidad ("fuerza", "magia", "inteligencia").
A su vez, el programa deberá mostrar por consola lo siguiente:
Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
El sexo y nombre de Heroe | Heroína de mayor edad.
La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
El promedio de edad entre Heroinas.
El promedio de edad entre Heroes de fuerza.
"""
primer_ingreso = True

contador_heroinas_fuerza = 0
contador_heroinas_magia = 0
contador_heroinas_restante = 0
acumulador_edad_heroinas = 0

contador_heroes_fuerza = 0
acumulador_edad_heroes_fuerza = 0

while (True):
    
    nombre_hero = input("Ingrese un nombre: \n")

    edad_hero = input("Ingrese la edad: \n")
    edad_hero = int(edad_hero)
    while(edad_hero<18):
        edad_hero = input("Ingrese una edad valida: \n")
        edad_hero = int(edad_hero)
    
    genero_hero = input("Ingrese el genero (m / f / nb): \n")
    while(genero_hero!="m" and genero_hero!="f" and genero_hero!="nb"):
        genero_hero = input("Ingrese un genero valido: \n")

    habilidad_hero = input("Ingrese la habilidad: \n")
    while(habilidad_hero!="fuerza" and habilidad_hero!="magia" and habilidad_hero!="inteligencia"):
        habilidad_hero = input("Ingrese una habilidad valida: \n")

    if(primer_ingreso):
        nombre_hero_fuerza_mas_joven = nombre_hero
        edad_hero_fuerza_mas_joven = edad_hero
        nombre_hero_mas_viejo = nombre_hero
        edad_hero_mas_viejo = edad_hero
        primer_ingreso = False
    elif(edad_hero_fuerza_mas_joven>edad_hero):
        nombre_hero_fuerza_mas_joven = nombre_hero
        edad_hero_fuerza_mas_joven = edad_hero
    elif(edad_hero_mas_viejo<edad_hero):
        nombre_hero_mas_viejo = nombre_hero
        edad_hero_mas_viejo = edad_hero

    if(genero_hero=="f"):
        acumulador_edad_heroinas = acumulador_edad_heroinas + edad_hero
        if(habilidad_hero=="fuerza"):
            contador_heroinas_fuerza+=1
        elif(habilidad_hero=="magia"):
            contador_heroinas_magia+=1
        else:
            contador_heroinas_restante+=1
    else:
        acumulador_edad_heroes_fuerza = acumulador_edad_heroes_fuerza + edad_hero
        if(habilidad_hero=="fuerza"):
            contador_heroes_fuerza+=1

    rta = input ("Desea seguir cargando? s/n\n")
    if (rta=="n"):
        break

promedio_edad_heroinas = acumulador_edad_heroinas / (contador_heroinas_fuerza+contador_heroinas_magia+contador_heroinas_restante)
promedio_edad_heroes_fuerza = acumulador_edad_heroes_fuerza / contador_heroes_fuerza

print("La persona con habilidad de fuerza mas joven es {}\n".format(nombre_hero_fuerza_mas_joven))
print("La persona mas veterna es {} con una edad de {} años\n".format(nombre_hero_mas_viejo,edad_hero_mas_viejo))
print("La cantidad total de heroina de 'Fuerza' y 'Magia' es {}\n".format(contador_heroinas_fuerza+contador_heroinas_magia))
print("El promedio de edad de las heroinas es de {} años\n".format(promedio_edad_heroinas))
print("El promedio de edad de los heroes de 'Fuerza' es de {} años\n".format(promedio_edad_heroes_fuerza))

