def es_par(numero:int) -> bool:
    '''
    Esta función sirve para determinar si un número es par o impar.

    Args:
        numero (int): Recibe un número ingresado por el usuario.

    Returns:
        bool: Retorna True si el número es par y False si el número es impar
    '''
    if numero == 0:
        print(numero)
        return True
    elif numero == 1 or numero == -1:
        print(numero)
        return False
    elif numero > 0:
        print(numero)
        return es_par(numero - 2)
    else:
        print(numero)
        return es_par(numero + 2)

def es_primo(numero:int, divisor:int=2) -> bool:
    '''
    Esta función sirve para determinar si un número es primo o no.

    Args:
        numero (int): Recibe un número ingresado por el usuario.
        divisor (int): Número divisor.

    Returns:
        bool: Retorna True si el número es primo y False si no lo es.    
    '''
    if numero < 2:
        return False
    elif divisor == numero:
        return True
    elif numero % divisor == 0:
        return False
    
    return es_primo(numero, divisor + 1)

def es_multiplo(a:int, b:int) -> bool:
    '''
    Esta función sirve para determinar si un número es múltiplo de otro.

    Args:
        a (int): Recibe un número ingresado por el usuario.
        b (int): Recibe un número ingresado por el usuario para dividir el anterior.
    Returns:
        bool: Retorna True si los números son múltiplos y False si no lo son.
    '''
    if b == 0:
        return False

    if a == 0:
        return True
    if a < b:
        return False

    return es_multiplo(a - b, b) 

def en_rango_recursivo(numero:int, minimo:int, maximo:int) -> bool:
    '''
    Esta función sirve para saber si un número está dentro de un rango determinado.

    Args: 
        numero (int): Recibe un número.
        minimo (int): Recibe el número mínimo del rango.
        maximo (int): Recibe el número máximo del rango.

    Returns:
        bool: Retorna True si el número está dentro del rango y False si no lo está.
    '''
    if minimo > maximo:
        return False
    elif numero < minimo or numero > maximo:
        return False
    if numero == minimo:
        return True

    return en_rango_recursivo(numero, minimo + 1, maximo)

def pedir_numero(mensaje:str="Ingresa un número: ") -> int:
    '''
    Esta función sirve para pedirle al usuario un número.

    Args: 
        mensaje (str): Envía un mensaje al usuario para solicitar un número

    Returns: 
        int: Retorna el número ingresado por el usuario
    '''
    return int(input(mensaje))