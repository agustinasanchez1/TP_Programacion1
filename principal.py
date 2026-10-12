from funciones import es_par , es_primo , es_multiplo, en_rango_recursivo , pedir_numero
from tablas import tablas
usuario = ""
contrasena = ""
usuario_registrado = ""
contrasena_registrada = ""
usuario_guardado = "pepe"
contrasena_guardada = "1234"
ingreso_exitoso = False

while ingreso_exitoso == False:
    registro = input("¡Hola! ¿Qué deseas hacer? \n [1] Registrarte  \n [2] Ingresar \n")
    if registro == "1":
            usuario = input("Ingrese un nombre de usuario para el registro: ")
            contrasena = input("Ingrese una contraseña para el registro: ")
            usuario_registrado = usuario
            contrasena_registrada = contrasena
            print("¡Registro exitoso! Ya puede ingresar")
    elif registro == "2":   
        usuario = input("Ingrese un nombre de usuario: ")
        contrasena = input("Ingrese una contraseña: ")

        if (usuario_registrado == usuario and contrasena_registrada == contrasena) or (usuario == usuario_guardado and contrasena == contrasena_guardada):
             print("Inicio de sesión correcto.")
             ingreso_exitoso = True
        else:
             print("Contraseña o usuario incorrecto.")

    else:
        print("Opción incorrecta.")

if ingreso_exitoso == True:
    salir = False
    while salir == False:
        opciones = input("\n ----- MENÚ PRINCIPAL ----- \n Ingrese una opción: \n [1] Proyectos \n [2] Tablas \n [3] Variables \n [4] Mostrar tablas \n [5] Estadísticas \n [6] Salir \n")
        match opciones:
            case "1":
                proyectos = int(input("Has elegido la opción de Proyectos. Los proyectos son: \n [1] Número par \n [2] Números primos \n [3] Múltiplos \n [4] Validación de rango \n"))
                match proyectos:

                    case 1:
                        numero = pedir_numero("Ingresa un número para comprobar si es par: ")
                        print(es_par(numero))

                    case 2:
                        primo = pedir_numero("Ingresa un número para comprobar si es primo: ")                      
                        print(es_primo(primo))

                    case 3:
                        numero = pedir_numero("Ingresa un número: ")
                        divisor = pedir_numero("Ingresa un número como divisor: ")
                        print(es_multiplo(numero,divisor))

                    case 4:
                        numero = pedir_numero("Ingresa un número: ")
                        minimo = pedir_numero("Ingresa el mínimo del rango: ")
                        maximo = pedir_numero("Ingresa el máximo del rango: ")
                        print(en_rango_recursivo(numero,minimo,maximo))

                    case _:
                        print("Inválido")

            case "2":
                print("Has elegido la opción Tablas")
               
                volver_tablas = False

                while volver_tablas == False:
                    print("\n ----- MENÚ DE TABLAS ----- \n [1] Crear tabla \n [2] Modificar tabla \n [3] Volver al menú principal")
                    
                    opcion_tablas = input("Seleccione una opción: ")

                    match opcion_tablas:
                        case "1":
                            nombre = input("Ingrese el nombre de la tabla: ")

                            existe = False

                            for tabla in tablas:
                                if tabla[0] == nombre:
                                    existe = True

                            if existe == True:
                                print("Ya existe una tabla con ese nombre.")
                            else:
                                columnas = []
                                filas = []

                                cantidad_columnas = int(input("¿Cuántas columnas tendrá la tabla? "))

                                for i in range(cantidad_columnas):
                                    columna = input("Ingrese el nombre de la columna: ")
                                    columnas.append(columna)

                                cantidad_filas = int(input("¿Cuántas filas tendrá la tabla? "))

                                for i in range(cantidad_filas):
                                    fila = []

                                    print("Cargando fila", i + 1)

                                    for j in range(cantidad_columnas):
                                        dato = input("Ingrese el dato de " + columnas[j] + ": ")
                                        fila.append(dato)

                                    filas.append(fila)

                                tablas.append([nombre, columnas, filas])

                                print("Tabla creada correctamente.")

                        case "2":
                            if len(tablas) == 0:
                                print("No hay tablas disponibles.")

                            else:
                                print("Tablas disponibles:")

                                for tabla in tablas:
                                    print(tabla[0])
    
                                nombre = input("¿Qué tabla desea modificar? ")

                                tabla_seleccionada = None

                                for tabla in tablas:
                                    if tabla[0] == nombre:
                                        tabla_seleccionada = tabla

                                if tabla_seleccionada == None:
                                    print("La tabla no existe.")                                
                                elif len(tabla_seleccionada[2]) == 0:
                                    print("La tabla no tiene filas para modificar.")
                                else:
                                    print("Columnas:")
                                    print(tabla_seleccionada[1])

                                    print("Filas:")

                                    for i in range(len(tabla_seleccionada[2])):
                                        print(i + 1, tabla_seleccionada[2][i])

                                    numero_fila = int(input("¿Qué fila desea modificar? "))

                                    numero_columna = int(input("¿Qué columna desea modificar? "))

                                    if (numero_fila >= 1 and numero_fila <= len(tabla_seleccionada[2]) and numero_columna >= 1 and numero_columna <= len(tabla_seleccionada[1])):
                                            nuevo_dato = input("Ingrese el nuevo dato: ")

                                            tabla_seleccionada[2][numero_fila - 1][numero_columna - 1] = nuevo_dato

                                            print("Dato modificado correctamente.")

                                    else:
                                        print("La fila o columna no existe.")

                        case "3":
                            volver_tablas = True

                        case _:
                            print("Opción incorrecta.")

            case "3":
                print("Has elegido la opción Variables")

            case "4":
                print("Has elegido la opción Mostrar tablas")
                if len(tablas) == 0:
                    print("No hay tablas disponibles.")

                else:
                    print("Tablas disponibles:")

                    for tabla in tablas:
                        print()
                        print("Nombre:", tabla[0])
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