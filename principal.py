from funciones_y_tablas.funciones import (
    es_par, 
    es_primo, 
    es_multiplo, 
    en_rango_recursivo, 
    pedir_numero,
)
from funciones_y_tablas.tablas import tablas


usuario = ""
contrasena = ""
usuario_registrado = ""
contrasena_registrada = ""
usuario_guardado = "pepe"
contrasena_guardada = "1234"
ingreso_exitoso = False

while ingreso_exitoso == False:
    registro = input("¡Hola! ¿Qué deseas hacer? \n "
                     "[1] Registrarte  \n " 
                     "[2] Ingresar \n ")
    if registro == "1":
        usuario = input("Ingrese un nombre de usuario para el registro: ")
        contrasena = input("Ingrese una contraseña para el registro: ")
        usuario_registrado = usuario
        contrasena_registrada = contrasena
        print("¡Registro exitoso! Ya puede ingresar")
    elif registro == "2":   
        usuario = input("Ingrese un nombre de usuario: ")
        contrasena = input("Ingrese una contraseña: ")

        if (usuario_registrado == usuario and contrasena_registrada == contrasena or 
            usuario == usuario_guardado and contrasena == contrasena_guardada):
            
            print("Inicio de sesión correcto.")
            ingreso_exitoso = True
        
        else:
            print("Contraseña o usuario incorrecto.")

    else:
        print("Opción incorrecta.")

if ingreso_exitoso == True:
    salir = False
    while salir == False:
        opciones = input(
            "\n ----- MENÚ PRINCIPAL ----- \n "
            "Ingrese una opción: \n "
            "[1] Proyectos \n "
            "[2] Tablas \n "
            "[3] Variables \n "
            "[4] Mostrar tablas \n "
            "[5] Estadísticas \n "
            "[6] Salir \n")
        match opciones:
            case "1":
                proyectos = int(input(
                    "Has elegido la opción de Proyectos. Los proyectos son: \n " 
                    "[1] Número par \n "
                    "[2] Números primos \n "
                    "[3] Múltiplos \n "
                    "[4] Validación de rango \n"))
                match proyectos:
                    case "1":
                        numero = pedir_numero("Ingresa un número para comprobar si es par: ")
                        print(es_par(numero))

                    case "2":
                        primo = pedir_numero("Ingresa un número para comprobar si es primo: ")                      
                        print(es_primo(primo))

                    case "3":
                        numero = pedir_numero("Ingresa un número: ")
                        divisor = pedir_numero("Ingresa un número como divisor: ")
                        print(es_multiplo(numero,divisor))

                    case "4":
                        numero = pedir_numero("Ingresa un número: ")
                        minimo = pedir_numero("Ingresa el mínimo del rango: ")
                        maximo = pedir_numero("Ingresa el máximo del rango: ")
                        print(en_rango_recursivo(numero,minimo,maximo))

                    case _:
                        print("Inválido")

            case "2":
                print("Has elegido la opción Tablas")

            case "3":
                print("Has elegido la opción Variables")

            case "4":
                print("Has elegido la opción Mostrar tablas")
                if len(tablas) == 0:
                    print("No hay tablas disponibles.")
                else:
                    print("Tablas disponibles:")
                    for tabla in tablas:
                        print("\n Nombre:", tabla[0])
                        print("Columnas:", tabla[1])
                        for fila in tabla[2]:
                            print(fila)

            case "5":
                print("Has elegido la opción Estadísticas")

            case "6":
                print("Has elegido la opción Salir. \n Saliste del programa")
                salir = True

            case _:
                print("Opción incorrecta.")