# PROGRAMA DE REGISTRO DE GASTOS DIARIOS
#
# La finalidad del programa es de tener un registro de los gastos del usuario, pidiendo que
# ingrese los datos requeridos y categorizando de una manera conveniente cada gasto. Se añade a
# una versión anterior la capacidad de tener múltiples entradas de gastos, con implementación de funciones
# y manejo de errores
#
# ################## PSEUDOCÓDIGO ########################
# FUNCIÓN menú (lista_de_opciones)
#     MIENTRAS VERDADERO
#         POR cada opción en la lista de opciones
#             MOSTRAR número y opción
#         LEER elección del usuario
#         SI la elección es numérica
#             CONVERTIR elección a entero
#             SI la elección está en el rango de opciones válidas
#                 DEVOLVER elección
#             MOSTRAR "opción inválida"
#
# FUNCIÓN corrección (datos_ingresados)
#     MIENTRAS VERDADERO
#         MOSTRAR los datos ingresados
#         LEER confirmación del usuario si los datos son correctos
#         SI la respuesta es afirmativa
#             DEVOLVER VERDADERO
#         SINO SI la respuesta es negativa
#             DEVOLVER FALSO
#         SINO
#             MOSTRAR "Opción inválida, intente nuevamente."
#
# FUNCIÓN ingreso de monto
#     MIENTRAS VERDADERO
#         INTENTAR
#             LEER ingreso de monto como número flotante, almacenando en variable
#             SI monto > 0
#               DEVOLVER monto ingresado
#             SINO
#               MOSTRAR "Monto debe ser positivo"
#         SI ERROR
#             MOSTRAR "Monto inválido."
#
# FUNCIÓN ingreso de categoria
#     CREAR lista de categorías de 8 opciones
#     MIENTRAS VERDADERO
#         LLAMAR a función menu con la lista de categorías como parámetro, almacenar opción elegida como variable
#         OBTENER categoría según el índice
#         SI opción elegida es 8 (Cancelar)
#         DEVOLVER FALSO
#         SI al llamar a función corrección con categoría elegida devuelve verdadero
#             DEVOLVER cat_elegida
#         SINO
#             CONTINUAR con el bucle
#
# FUNCIÓN ingreso de descripción
#     MIENTRAS VERDADERO
#         LEER ingreso de descripción del usuario, almacenando en variable
#         SI LLAMAR a función corrección con la descripción ingresada devuelve verdadero
#             DEVOLVER descripción ingresada
#
# FUNCIÓN ingreso de año
#     MIENTRAS VERDADERO
#         LEER año ingresado por el usuario, almacenando en variable
#         SI es numérico y entre 1901 y 2025
#             SI LLAMAR a función corrección con el año ingresado devuelve verdadero
#                 DEVOLVER año como entero
#         SINO
#             MOSTRAR mensaje de año inválido
#
# FUNCIÓN ingreso de mes
#     MIENTRAS VERDADERO
#         LEER mes ingresado por usuario, almacenando en variable
#         SI es numérico entre 1 y 12
#             SI LLAMAR a función corrección da verdadero
#                 DEVOLVER mes (convertido a entero)
#         SINO
#             MOSTRAR mensaje de mes inválido
#
# FUNCIÓN ingreso_fecha()
#     LLAMAR a ingreso_anio y guardar en variable
#     LLAMAR a ingreso_mes y guardar en variable
#     DEFINIR dias_x_mes como un diccionario con los días de cada mes
#     SI mes es igual a 2 y la comprobación de si año es bisiesto da verdadera
#         ASIGNAR 29 como valor al mes 2 en el diccionario
#     MIENTRAS VERDADERO
#         LEER día ingresado por usuario, almacenando en variable
#         SI día es numérico Y está entre 1 y días del mes correspondiente
#             SI LLAMAR a función corrección da verdadero
#                 DEVOLVER día convertido a entero, mes, año
#         MOSTRAR mensaje de día inválido
#
# FUNCIÓN registrar_gasto()
#     LLAMAR a ingreso_monto y guardar en variable
#     LLAMAR a ingreso_categoria y guardar en variable
#     SI categoria devuelve FALSO
#       MOSTRAR "Operación cancelada"
#       DEVOLVER FALSO
#     LLAMAR a ingreso_descripcion y guardar en variable
#     MOSTRAR mensaje de carga de fecha
#     LLAMAR a ingreso_fecha y guardar en variables correspondientes
#     CREAR diccionario gasto con los datos
#     DEVOLVER diccionario gasto
#
# FUNCIÓN consultar_gasto_fecha
#     LLAMAR a ingreso_fecha y guardar en variables
#     DEFINIR variable encontrado como FALSO
#     POR cada gasto en lista de gastos
#             SI el día, mes y año coinciden
#                 ASIGNAR VERDADERO a variable encontrado
#                 MOSTRAR gasto
#     SI encontrado es igual a FALSO
#         MOSTRAR mensaje de falta de datos para esa fecha
#
# FUNCIÓN consultar_gasto_mes
#     LLAMAR a ingreso_mes y guardar en variable
#     DEFINIR encontrado como FALSO
#     POR cada gasto en lista de gastos
#         SI el mes ingresado coincide
#             ASIGNAR VERDADERO a encontrado
#             MOSTRAR gasto
#     SI encontrado es igual a FALSO
#         MOSTRAR "No se encontraron gastos para ese mes."
#
# FUNCIÓN consultar_gasto_anio
#     LLAMAR a ingreso_anio y guardar en variable
#     DEFINIR encontrado como FALSO
#     POR cada gasto en lista de gastos
#         SI año ingresado coincide
#             ASIGNAR VERDADERO a encontrado
#             MOSTRAR gasto
#     SI encontrado es igual a FALSO
#         MOSTRAR "No se encontraron gastos para ese año."
#
# FUNCIÓN consultar_gasto_categoria
#     LLAMAR a ingreso_categoria y guardar en variable
#     DEFINIR encontrado como FALSO
#     POR cada gasto en gastos_lista
#         SI categoría ingresada coincide
#             ASIGNAR VERDADERO a encontrado
#             MOSTRAR gasto
#     SI encontrado es igual a FALSO
#         MOSTRAR mensaje de no encontrado
#
# FUNCIÓN mostrar_total
#     SUMAR todos los montos de la lista de gastos y guardar en variable
#     MOSTRAR cantidad de gastos registrados
#     MOSTRAR el total de la suma de los gastos
#     MOSTRAR el promedio de los gastos de la lista
#
# FUNCIÓN mostrar_lista_completa
#     MOSTRAR "Gastos registrados: "
#     POR cada número y gasto en lista de gastos, empezando desde 1
#         MOSTRAR los valores almacenados en la lista, con sus datos correspondientes formateados
#
# FUNCIÓN eliminar_gasto(lista de gastos)
#     SI la lista está vacía:
#         MOSTRAR "No hay gastos registrados"
#         DEVOLVER vacío
#     LLAMAR a mostrar_lista_completa()
#     MIENTRAS VERDADERO:
#         LEER el gasto a eliminar
#         SI la entrada es numérica
#             GUARDAR entrada como entero
#             SI el número es 0:
#                 MOSTRAR "Eliminación cancelada"
#                 retornar
#             SINO SI el número está dentro del rango de la lista:
#                 ASIGNAR el gasto seleccionado a una variable
#                 SI LLAMAR a la función correccion da VERDADERO:
#                     ELIMINAR el gasto de la lista
#                     MOSTRAR "Gasto eliminado"
#                     DEVOLVER vacío
#                 SI NO confirma:
#                     MOSTRAR "Eliminación cancelada"
#                     DEVOLVER vacío
#         MOSTRAR "Opción inválida"
#
###########################################################################################
# PROGRAMA PRINCIPAL
# INICIO
#
#      MOSTRAR mensaje de bienvenida
#      LEER nombre del usuario, almacenando en una variable
#      MOSTRAR mensaje personalizado
#      CREAR lista de gastos vacía
#
#      BUCLE PRINCIPAL
#          LLAMAR a función menú, con los parámetros:
#              1 - Registrar gasto
#              2 - Consultar gasto
#              3 - Salir
#
#          SELECCIONAR CASO:
#            CASO 1:
#                LLAMAR a función para registrar gasto, guardando en una variable
#                SI la variable devuelve el gasto:
#                    GUARDAR los datos del gasto en la lista de gastos
#                    MOSTRAR mensaje de éxito al registrar datos
#
#            CASO 2:
#                SI hay registros en la lista de gastos:
#                    LLAMAR a la función menú con los parámetros:
#                         1 - Por fecha exacta
#                         2 - Por mes
#                         3 - Por año
#                         4 - Por categoría
#                         5 - Total y promedio
#                         6 - Mostrar lista completa de gastos
#                         7 - Volver
#                    SELECCIONAR CASO:
#                         1 - LLAMAR a la función consultar_gasto_fecha
#                         2 - LLAMAR a la función consultar_gasto_mes
#                         3 - LLAMAR a la función consultar_gasto_anio
#                         4 - LLAMAR a la función consultar_gasto_categoria
#                         5 - LLAMAR a la función mostrar_total
#                         6 - LLAMAR a la función mostrar_lista_completa
#                         7 - CONTINUAR
#                SI NO
#                    MOSTRAR "No hay gastos registrados"
#
#            CASO 3:
#                LLAMAR a la función eliminar gasto con parámetro la lista de gastos
#
#            CASO 4:
#                MOSTRAR mensaje de despedida
#                TERMINAR
#
#            SI opción inválida
#                MOSTRAR "Opción inválida", volver al bucle
#
#      FIN BUCLE
# FIN
#
#################################################################################################
# FUNCIONES
#
#Muestra cualquier menú y devuelve la elección válida
def menu(opciones):
    ''':param opciones:
    toma una lista de opciones como parámetro
    mientras verdadero:
        muestra las opciones enumerándolas con formato ("1- Ejemplo")
        lee la elección que toma el usuario
        si es un número:
            si es un número dentro de las opciones:
                :return: elección validada del usuario
        mostrar mensaje de elección inválida'''
    while True:
        for nro, opcion in enumerate(opciones, start=1):
            print(f"{nro} - {opcion}")
        eleccion = input("Ingrese su elección (por ej.: 1): ").strip()
        if eleccion.isdigit():
            eleccion = int(eleccion)
            if 1 <= eleccion <= len(opciones):
                return eleccion
        print("Opción inválida. Intente nuevamente.\n")

# Confirmación de entrada
def correccion(datos_ingresados):
    '''
    toma como parámetro cualquier dato ingresado
    mostrar datos ingresados
    leer si es correcto
    si es correcto:
        :return True
    si no es correcto:
        :return: False
    si no:
        mostrar mensaje de error
    '''
    while True:
        print(f"Los datos ingresados son: {datos_ingresados}")
        sel_correcta = input("Esto es correcto? S/N ").strip().lower()
        if sel_correcta == "s":
            return True
        elif sel_correcta == "n":
            return False
        else:
            print("Opción inválida, intente nuevamente.\n")

# Comprobación de ingreso de monto
def ingreso_monto():
    '''
    mientras verdadero:
        intentar:
            leer monto ingresado como float
            si el monto ingresado es mayor a 0:
                :return: monto ingresado
            si no:
                mostrar mensaje de error
        excepto error de valor:
            mostrar mensaje de error
    '''
    while True:
        try:
            input_monto = float(input("Ingrese el monto gastado (ej.: 210.50): $").strip())
            print()
            if input_monto > 0:
                return input_monto
            else:
                print("El monto debe ser un número positivo.\n")
        except ValueError:
            print("Monto inválido.\n")

# Ingreso de categoría
def ingreso_categoria():
    '''
    crear lista de opciones de categoría
    Mientras verdadero:
        llamar a la función menú, almacenando en una variable
        asignar la opción elegida a la opcion de la lista correspondiente
        si la opción elegida es 8:
            :return: False
        si llamar a funcion correccion da True:
            :return: categoría elegida
        si no:
            volver al bucle
    '''
    opcion_cat = ["Vivienda", "Alimentos", "Servicios", "Salud", "Transporte",
                  "Entretenimiento y ocio", "Compras personales", "Cancelar"]  # Categorías posibles
    while True:
        opcion_elegida = menu(opcion_cat) # Llama a función menu y guarda en una variable
        cat_elegida = opcion_cat[opcion_elegida - 1] # Coteja la opción ingresada con la lista de categorias. Poner -1 es para equiparar la elección del usuario con el sistema de conteo que arranca de 0
        if opcion_elegida == 8:
            return False
        elif correccion(f"Categoría seleccionada {cat_elegida}"):
            print()
            return cat_elegida
        else:
            continue

# Ingreso descripción
def ingreso_descripcion():
    '''
    mientras verdadero:
        leer descripcion ingresada
        si llamar a funcion correccion da True:
            :return: descripción
    '''
    while True:
        descripcion_input = input("Describa en qué se gastó: ").strip()
        if correccion(f"Descripción ingresada: {descripcion_input}"):
            print()
            return descripcion_input

# Ingreso de año
def ingreso_anio():
    '''
    mientras verdadero:
        leer ingreso de año
        si año es un número y mayor a 1900 y menor o igual a 2025:
            si llamar a funcion correccion da True:
            :return: año
        si no:
        mostrar mensaje de error
    '''
    while True:
        anio = input("Ingrese el año (ej.: 2022): ").strip()
        if anio.isdigit() and 1900 < int(anio) <= 2025:
            if correccion(f"El año ingresado es: {anio}"):
                print()
                return int(anio)
        else:
            print("Año inválido.\n")

# Ingreso de mes
def ingreso_mes():
    '''
    mientras verdadero:
        leer mes ingresado
        si mes es un número y entre 1 y 12 inclusive:
            si llamar a funcion correccion da True:
            :return: mes
        si no:
        mostrar mensaje de error
    :return:
    '''
    while True:
        mes = input("Mes (ej.: 03): ").strip()
        if mes.isdigit() and 1 <= int(mes) <= 12:
            if correccion(f"El mes ingresado es: {mes}"):
                print()
                return int(mes)
        else:
            print("Mes inválido.\n")

# Ingreso fecha exacta
def ingreso_fecha():
    '''
    llamar a la función de ingreso de año
    llamar a la función de ingreso de mes
    crear diccionario con claves de nro. de mes, y valores días en el mes
    crear condición de ajuste por año bisiesto para febrero
    mientras verdadero:
        leer ingreso de día
        si día es nro. y entre 1 y los días correspondientes al mes:
            si llamar a funcion correccion da True:
                :return: día, mes, año
        si no:
            mostrar mensaje de error
    '''
    anio = ingreso_anio()
    mes = ingreso_mes()
    # Días en cada mes
    dias_x_mes = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    # Ajuste por año bisiesto
    if mes == 2 and (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
        dias_x_mes[2] = 29
    # Bucle de ingreso de fecha
    while True:
        dia = input(f"Ingrese el día (ej.:(1-{dias_x_mes[mes]}): ").strip()
        if dia.isdigit() and 1 <= int(dia) <= dias_x_mes[mes]:
            if correccion(f"Fecha ingresada: {int(dia):02}/{mes:02}/{anio}"):
                print()
                return int(dia), mes, anio
        print("Día inválido.\n")

# Ejecuta el proceso de carga y validación de gastos
def registrar_gasto():
    '''
    llamar a la función de ingreso de monto, almacenando en una variable
    llamar a la función de ingreso de categoría, almacenando en una variable
    si categoría da FALSO:
        mostrar mensaje de operación cancelada
        volver a menú principal
    llamar a la función de ingreso de descripción, almacenando en una variable
    mostrar mensaje simpático
    llamar a la función de ingreso de fecha, almacenando en 3 variables correspondientes a dia, mes, año
    crear diccionario de gasto con todos los datos
    :return: diccionario de gasto
    '''
    # Ingreso de monto
    monto = ingreso_monto()
    # Ingreso categoría
    categoria = ingreso_categoria()
    if not categoria:
        print("Operación cancelada. Volviendo al menú principal.\n")
        return False
    # Ingreso de descripción
    descripcion = ingreso_descripcion()
    #Ingreso de fecha
    print("Excelente! Ahora anotemos la fecha en la que se realizó el gasto")
    dia, mes, anio = ingreso_fecha()
    gasto = {"Monto" : monto, "Categoría" : categoria, "Descripción" : descripcion,
             "Día" : dia, "Mes" : mes, "Año" : anio}
    return gasto

# Filtra gastos por fecha específica
def consultar_gasto_fecha():
    '''
    llamar a la función de ingreso de fecha, almacenando en 3 variables correspondientes a dia, mes, año
    declarar booleano "encontrado" como falso
    por cada gasto en lista de gastos:
        si día, mes y año coinciden con lo ingresado:
            "encontrado" pasa a verdadero
            mostrar el gasto con los datos formateados
            mostrar línea de separación entre gastos
    si "encontrado" sigue como falso:
        mostrar mensaje de gasto no encontrado
    '''
    dia, mes, anio = ingreso_fecha()
    encontrado = False
    for gasto in gastos_lista:
        if (gasto["Día"] == dia and
                gasto["Mes"] == mes and
                gasto["Año"] == anio):
            encontrado = True
            print(f"Monto: ${gasto['Monto']}, Categoría: {gasto['Categoría']}, "
                  f"Descripción: {gasto['Descripción']}, "
                  f"Fecha: {gasto['Día']:02}/{gasto['Mes']:02}/{gasto['Año']}\n")
            print("--------------------------------------------------------------------------------------")
    if not encontrado:
        print("No se encontraron gastos para esa fecha.\n")

# Consultar gasto por mes
def consultar_gasto_mes():
    '''
        llamar a la función de ingreso de mes, almacenando en una variable
        declarar booleano "encontrado" como falso
        por cada gasto en lista de gastos:
            si mes coincide con lo ingresado:
                "encontrado" pasa a verdadero
                mostrar el gasto con los datos formateados
                mostrar línea de separación entre gastos
        si "encontrado" sigue como falso:
            mostrar mensaje de gasto no encontrado
        '''
    mes = ingreso_mes()
    encontrado = False
    for gasto in gastos_lista:
        if gasto["Mes"] == mes:
            encontrado = True
            print(f"Monto: ${gasto['Monto']}, Categoría: {gasto['Categoría']}, "
                  f"Descripción: {gasto['Descripción']}, "
                  f"Fecha: {gasto['Día']:02}/{gasto['Mes']:02}/{gasto['Año']}\n")
            print("--------------------------------------------------------------------------------------")
    if not encontrado:
        print("No se encontraron gastos para ese mes.\n")

# Consultar gasto por año
def consultar_gasto_anio():
    '''
            llamar a la función de ingreso de año, almacenando en una variable
            declarar booleano "encontrado" como falso
            por cada gasto en lista de gastos:
                si año coincide con lo ingresado:
                    "encontrado" pasa a verdadero
                    mostrar el gasto con los datos formateados
                    mostrar línea de separación entre gastos
            si "encontrado" sigue como falso:
                mostrar mensaje de gasto no encontrado
            '''
    anio = ingreso_anio()
    encontrado = False
    for gasto in gastos_lista:
        if gasto["Año"] == anio:
            encontrado = True
            print(f"Monto: ${gasto['Monto']}, Categoría: {gasto['Categoría']}, "
                  f"Descripción: {gasto['Descripción']}, "
                  f"Fecha: {gasto['Día']:02}/{gasto['Mes']:02}/{gasto['Año']}\n")
            print("--------------------------------------------------------------------------------------")
    if not encontrado:
        print("No se encontraron gastos para ese año.\n")

# Filtra gastos por categoría
def consultar_gasto_categoria():
    '''
            llamar a la función de ingreso de categoría, almacenando en una variable
            declarar booleano "encontrado" como falso
            por cada gasto en lista de gastos:
                si categoría coincide con lo ingresado:
                    "encontrado" pasa a verdadero
                    mostrar el gasto con los datos formateados
                    mostrar línea de separación entre gastos
            si "encontrado" sigue como falso:
                mostrar mensaje de gasto no encontrado
            '''
    categoria = ingreso_categoria()
    encontrado = False
    for gasto in gastos_lista:
        if gasto["Categoría"] == categoria:
            encontrado = True
            print(f"Monto: ${gasto['Monto']}, Categoría: {gasto['Categoría']}, "
                  f"Descripción: {gasto['Descripción']}, "
                  f"Fecha: {gasto['Día']:02}/{gasto['Mes']:02}/{gasto['Año']}\n")
            print("--------------------------------------------------------------------------------------")
    if not encontrado:
        print("No se encontraron gastos para esa categoría.\n")

# Muestra total, promedio y cantidad de gastos
def mostrar_total():
    '''
    asignar el valor de la suma de cada monto de cada gasto en la lista de gastos a una variable
    mostrar la cantidad de gastos registrados
    mostrar el total de la suma de montos
    mostrar el promedio de los montos en la lista de gastos
    '''
    total = sum(gasto["Monto"] for gasto in gastos_lista)
    print(f"Hay {len(gastos_lista)} gastos registrados")
    print(f"El total de gastos es de : ${total}")
    print("El gasto promedio es de : $", total / len(gastos_lista),"\n")

# Muestra toda la lista de gastos, formateada
def mostrar_lista_completa():
    '''
    mostrar "gastos registrados"
    por cada nro, gasto en un conteo de elementos de la lista de gastos arrancando en 1:
        mostrar enumerando cada gasto formateado
        mostrar línea de separación entre gastos
    '''
    print("Gastos registrados: ")
    for nro, gasto in enumerate(gastos_lista, start=1):
        print(f"{nro}. Monto: ${gasto['Monto']}, Categoría: {gasto['Categoría']}, "
              f"Descripción: {gasto['Descripción']}, "
              f"Fecha: {gasto['Día']:02d}/{gasto['Mes']:02d}/{gasto['Año']}")
        print("--------------------------------------------------------------------------------------")

def eliminar_gasto(gastos_lista):
    '''
    toma como parámetro la lista de gastos
    si la lista está vacía
        mostrar mensaje de error
        :return:
    llamar a la función de mostrar lista completa
    mientras verdadero:
        leer qué gasto quiere eliminar el usuario
        si la selección es un nro.:
            convertir selección a int
            si la selección es 0:
                mostrar mensaje de eliminación cancelada
                :return:
            si no si la selección está entre 1 y la cantidad de items en la lista de gastos:
                asignar el gasto seleccionado a una variable
                si llamar a funcion correccion da True:
                    quitar el gasto seleccionado de la lista
                    mostrar mensaje de éxito
                    :return:
                si no:
                    mostrar mensaje de operación cancelada
                    :return:
        mostrar mensaje de operación inválida
    '''
    if not gastos_lista:
        print("No hay gastos registrados.\n")
        return
    mostrar_lista_completa()
    while True:
        seleccion = input("Ingrese el número del gasto que desea eliminar (0 para cancelar): ").strip()
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if seleccion == 0:
                print("Eliminación cancelada.\n")
                return
            elif 1 <= seleccion <= len(gastos_lista):
                gasto_a_eliminar = gastos_lista[seleccion - 1]
                if correccion(f"¿Está seguro de eliminar este gasto? {gasto_a_eliminar}"):
                    gastos_lista.pop(seleccion - 1)
                    print("Gasto eliminado.\n")
                    return
                else:
                    print("Eliminación cancelada.\n")
                    return
        print("Opción inválida. Intente nuevamente.\n")

########################################################################################

# Bienvenida al programa
print("Hola, bienvenido a REVI, tu ayudante para registrar y revisar tus gastos!")

# Ingreso de nombre del usuario
nombre_usuario = input("Me dirías tu nombre? ")

# Ingreso al menú de opciones
print(f"Un placer {nombre_usuario.strip()}! Por favor selecciona una opción para continuar:")

# Lista donde se van a almacenar los datos
gastos_lista = []

# Inicio de bucle para el menú
while True:
    # Llamado a la función menú
    opcion = menu(["Registrar gasto", "Consultar gasto", "Eliminar gasto","Salir"])
    match opcion:
        # Registro de gasto
        case 1:
            gasto = registrar_gasto()
            if gasto:
                gastos_lista.append(gasto)
                print("El gasto fue registrado exitosamente!")
        # Consultas
        case 2:
            if gastos_lista:
                opcion_submenu = menu(["Consultar gasto por día específico", "Consultar gasto por mes",
                                  "Consultar gasto por año", "Consultar gasto por categoría",
                                  "Consultar gasto total","Ver lista completa de gastos", "Volver"])
                match opcion_submenu:
                    case 1:
                        consultar_gasto_fecha()
                    case 2:
                        consultar_gasto_mes()
                    case 3:
                        consultar_gasto_anio()
                    case 4:
                        consultar_gasto_categoria()
                    case 5:
                        mostrar_total()
                    case 6:
                        mostrar_lista_completa()
                    case 7:
                        continue
            else:
                print("No hay gastos registrados.\n")
        # Eliminación
        case 3:
            eliminar_gasto(gastos_lista)
        # Salir del programa
        case 4:
            print(f"Gracias por usar REVI, {nombre_usuario}. ¡Hasta la próxima!")
            break

#################################################################################################
# POSIBLES MEJORAS:
#
# - Editar gastos ya cargados
# - Separación de las funciones y pseudocódigo en archivos distintos
# - Generar tests unitarios para cada función
# - Implementación de librería datetime para simplificar validación de día, mes, año
# - Implementación de base de datos para guardar los registros
# - Implementación de login de usuarios con la base de datos
# - Visualización de datos en gráficos
# - Implementación de alertas o recordatorios
# - Implementación de interfaz gráfica
# - Control de versiones con git (ya lo vengo haciendo)