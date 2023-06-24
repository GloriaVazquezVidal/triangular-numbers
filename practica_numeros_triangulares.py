 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import math

 ##1. Identificacion de numeros triangulares

def is_triangular(t):
    """Recibe un numero natural t (mayor que 0) y comprueba si cumple la propiedad de que es triangular o no.
    
    Parametros
    ----------
    t : int
        El numero natural objeto de estudio

    Devuelve
    -------
    booleano
        True si el numero es triangular; False si el numero no es triangular.
    """
    i = 1
    #inicializamos la variable sumatorio a 0. Guarda la suma total de los elementos i
    sumatorio = 0 
    while sumatorio < t:
        #la suma acumulada se guarda en la variable sumatorio
        sumatorio = sumatorio + i 
        i += 1
    return sumatorio == t



##2. Test de identificacion de numeros triangulares
  
def test_is_triangular():
    """Comprueba una lista dada de numeros para ver cuales son triangulares o no
    
    Parametros
    ----------
    Ninguno.

    Devuelve
    -------
    Par (numero, True/False), 
        numero: int. 
        booleano: True si el numero de la lista es triangular; False si el numero no es triangular.
    """
    
    lista = [1, 2, 3, 5, 6, 7, 9, 10, 3240, 3241, 470935, 470936, 369797610, 369797611, 378854101, 378854102]
    for numero in lista:
      print(numero, is_triangular(numero))
      
      
##3. Numero triangular previo

def triangular_previo(n): #n mayor o igual que 2 porque 1 no tiene triangular previo
    """Recibe un numero natural n (mayor o igual que 2) y devuelve el numero triangular previo a n sin que lo supere.
    
    Parametros
    ----------
    n : int
        El numero natural objeto de estudio.

    Devuelve
    -------
    int
        Numero triangular previo al numero n.
    """
    i = 1
    #inicializamos la variable sumatorio a 0. Guarda la suma total de los elementos i
    sumatorio = 0 
    while sumatorio < n:
        #la suma acumulada se guarda en la variable sumatorio
        sumatorio = sumatorio + i 
        i += 1
    return sumatorio - i + 1  #sumatorio previo 
    
    
##4. Test de identificacion de numeros triangulares

def test_triangular_previo():
    """Devuelve los numeros triangulares previos de los numeros de la lista dada.

    Parametros
    ----------
    Ninguno.

    Devuelve
    -------
    Par (numero, previo), 
        numero: int. Cada elemento entero de la lista.
        previo: int. El numero triangular previo del elemento entero de la lista al que se refiere.
    """
    
    lista = [9, 10, 3241, 470936, 369797611, 378854102]
    for numero in lista:
      print(f"Para el numero {numero}, su numero triangular previo es {triangular_previo(numero)}")
      
      
##5. Mejora de la eficiencia

#5.1. Mejora de la funcion is_triangular(t)
def cuadrado_perfecto(n):
    """Comprueba si el numero natural n cumple que es un cuadrado perfecto.

    Parametros
    ----------
    n : int
        El numero natural objeto de estudio.

    Devuelve
    -------
    booleano
        True si el numero es un cuadrado perfecto; False si el numero no es un cuadrado perfecto.
    """
    
    #calculamos la raiz cuadrada del numero n natural
    raiz_n = math.sqrt(n) 
    #si el numero es cuadrado perfecto, al calcular la raiz cuadrada del numero y elevarlo al cuadrado, ha de devolver el mismo numero
    return int(raiz_n) ** 2 == n 

def improved_is_triangular(t):
    """Recibe un numero natural t (mayor que 0) y comprueba si cumple la propiedad de que es triangular o no.
    
    Parametros
    ----------
    t : int
        El numero natural objeto de estudio

    Devuelve
    -------
    booleano
        True si el numero es triangular; False si el numero no es triangular.
    """
    #si el numero 1 + 8*t cumple que es cuadrado perfecto (calculado a mano), entonces t es un numero triangular
    return cuadrado_perfecto(1 + 8*t)

#5.2. Mejora de la funcion improved_triangular_previo(t)

def improved_triangular_previo(t):
    """Recibe un numero natural t (mayor o igual que 2) y devuelve el numero triangular previo a t sin que lo supere.
    
    Parametros
    ----------
    t : int
        El numero natural objeto de estudio.

    Devuelve
    -------
    int
        Numero triangular previo al numero t.
    """
    solucion_ecuacion = (-1 + math.sqrt(1 + 8*(t-1))) * 0.5
    n = math.floor(solucion_ecuacion)
    return int((n*(n+1)) * 0.5)

#5.3. Explicacion de por que la eficiencia mejora con las funciones anteriores
    """La complejidad temporal de utilizar un bucle como en la funcion is_triangular(t) es de O(sqrt(n)).
    En cambio, la complejidad temporal de la funcion improved_is_triangular(t) es de 0(log(n)). 
    Si representamos las graficas sqrt(n) y log(n), podemos comprobar que, para n natural distinto de cero (es decir, no nulo),
    sqrt(n) acota superiormente a log(n) y, por tanto, siempre crece mas rapido que este. En conclusion, mejoramos la eficiencia
    del codigo mediante la funcion improved_is_triangular(t), sin bucles.

    Ademas, en la funcion improved_triangular_previo(t) calculamos una constante concreta en lugar de ejecutar un bucle, por lo que
    el orden de complejidad temporal mejora como en el caso anterior.

    Veamoslo a partir de la siguiente funcion.
    """
    
def triangular_and_previo(t):
    """Recibe un numero natural t (mayor que 0) y comprueba si cumple la propiedad de que es triangular o no y devuelve
    el numero triangular previo a t sin que lo supere.
    
    Parametros
    ----------
    t : int
        El numero natural objeto de estudio.

    Devuelve
    -------
    t : int
        El numero natural objeto de estudio.
        
    improved_is_triangular(t) : booleano
        El resultado de comprobar si t es un numero triangular. True si es triangular y False si no lo es.
    
    improved_triangular_previo(t) : int
        Numero triangular previo al numero t.
    """
    print(f"¿El numero {t} es triangular? {improved_is_triangular(t)}. Y su numero triangular previo es {improved_triangular_previo(t)}.")