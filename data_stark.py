from archivo import lista_personajes


def nombres_superheroes() -> str:

    for nombres_superheroes in lista_personajes:
    
        print(f"Nombre del heroe: {nombres_superheroes ['nombre']}")
    return nombres_superheroes
    
def nombre_y_altura_superheroe():
    
    for nombre_altura in lista_personajes:
    
        print(f"El superheroe: {nombre_altura['nombre']} mide {nombre_altura['altura']} cm")
    return nombre_altura    
        
def heroe_mas_alto() -> float:
    
    altura_maxima = float (lista_personajes[0]['altura'])
    superheroe_mas_alto = lista_personajes[0]['nombre']
    
    for superheroe in lista_personajes:
        altura_general = float(superheroe['altura'])
        
        if altura_general > altura_maxima:
            superheroe_mas_alto = superheroe['nombre']
            return superheroe
            
    print(f"El superheroe más alto es: {superheroe_mas_alto}")    

        
def heroe_mas_bajo() -> float:
    altura_minima = lista_personajes[0]['altura']
    superheroe_mas_bajo = lista_personajes[0]['nombre']
    
    for superheroe in lista_personajes:
        altura_general = float(superheroe['altura'])
        
        if altura_general < altura_minima:
            superheroe_mas_bajo = altura_minima
            
        print(f"El superheroe más bajo es: {superheroe_mas_bajo}")
        

def promedio_altura() -> float:
    cantidad_superheroes = 0
    altura_superheroes = 0
    
    for superheroe in lista_personajes:
        
        altura_superheroes += float (lista_personajes['altura'])
        cantidad_superheroes =+ 1
        
    promedio = altura_superheroes // cantidad_superheroes
    
    
    print(f"El promedio de las alturas de los superheroes es de: {promedio}")
    return superheroe
    
def altura_maxima_minima():
    altura_minima = lista_personajes[0]['altura']
    superheroe_mas_bajo = lista_personajes[0]['nombre']
    
    for superheroe in lista_personajes:
        altura_general = float(superheroe['altura'])
        
        if altura_general < altura_minima:
            superheroe_mas_bajo = altura_minima
            return superheroe
        
    altura_maxima = lista_personajes[0]['altura']
    superheroe_mas_alto = lista_personajes[0]['nombre']
    
    for superheroe in lista_personajes:
        altura_general = float(superheroe['altura'])
        
        if altura_general > altura_maxima:
            superheroe_mas_alto = superheroe['nombre']
            return superheroe            
        print(f"La altura máxima de un superheroe es: {superheroe_mas_alto}")
        print(f"La altura minima de un superheroe es: {superheroe_mas_bajo}")

def comparación_pesos():
    peso_maximo = float( lista_personajes[0] ['peso'])
    nombre_mas_pesado = lista_personajes[0] ['nombre']
    peso_minimo = float (lista_personajes [0] ['peso'])
    nombre_menos_pesado = lista_personajes [0] ['nombre']
    
    for superheroe in lista_personajes:
        peso_superheroe = float(lista_personajes['peso'])
        
        if peso_superheroe > peso_maximo:
            nombre_mas_pesado = peso_maximo ['nombre']
            
        else:
            nombre_menos_pesado = peso_minimo ['nombre']
            
    print(f"El superheroe más pesado es {nombre_mas_pesado}")
    print(f"El superheroe menos pesado es {nombre_menos_pesado}")
    return superheroe        