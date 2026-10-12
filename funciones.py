def es_par(numero):
    if numero == 0:
        return True
    elif numero == 1 or numero == -1:
        return False
    elif numero > 0:
        return es_par(numero - 2)
    else:
        return es_par(numero + 2)

def es_primo(numero, divisor=2):
    if numero < 2:
        return False
    elif divisor == numero:
        return True
    elif numero % divisor == 0:
        return False
    
    return es_primo(numero, divisor + 1)

def es_multiplo(a, b):
    a = abs(a)
    b = abs(b)

    if b == 0:
        return False

    if a == 0:
        return True
    if a < b:
        return False

    return es_multiplo(a - b, b) 

def en_rango_recursivo(numero, minimo, maximo):
    if minimo > maximo:
        return False
    elif numero < minimo or numero > maximo:
        return False
    if numero == minimo:
        return True

    return en_rango_recursivo(numero, minimo + 1, maximo)

def pedir_numero(mensaje="Ingresa un número: "):
    return int(input(mensaje))


