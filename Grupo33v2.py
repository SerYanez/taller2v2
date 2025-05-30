# PROGRAMA DE REGISTRO DE GASTOS DIARIOS
#
# La finalidad del programa es de tener un registro de los gastos del usuario, pidiendo que
# ingrese los datos requeridos y categorizando de una manera conveniente cada gasto. Se añade a
# una versión anterior la capacidad de tener múltiples entradas de gastos, con implementación de funciones
# y manejo de errores
#
# ################## PSEUDOCÓDIGO ########################
'''
DEFINIR función menú
    MIENTRAS VERDADERO
        POR cada opción en la lista de opciones
            MOSTRAR número y opción
        LEER elección del usuario
        SI la elección es equivalente a un número
            CONVERTIR elección a número
            SI la elección es mayor o igual a 1 y menor o igual al número de opciones
                DEVOLVER elección
            MOSTRAR "opción inválida"

DEFINIR función corrección
    MIENTRAS VERDADERO
        MOSTRAR los datos ingresados
        LEER la respuesta del usuario a si los datos son correctos
        SI la respuesta es afirmativa
            DEVOLVER VERDADERO
        SI la respuesta es negativa
            DEVOLVER FALSO
        SINO
            MOSTRAR "Opción inválida, intente nuevamente."

DEFINIR función ingreso de monto
    MIENTRAS VERDADERO
        INTENTAR
            LEER ingreso de monto, convertir a número flotante, almacenando en variable
            DEVOLVER monto ingresado
        EXCEPTO ingreso no sea número válido
            MOSTRAR "Monto inválido."

DEFINIR función ingreso de categoria
    CREAR lista de categorías
    MIENTRAS VERDADERO
        LLAMAR a función menu con la lista de categorías como parámetro, almacenar opción elegida como variable interna
        DEFINIR categoría elegida como el elemento de opción elegida
        SI al llamar a función corrección con categoría elegida devuelve verdadero
            DEVOLVER cat_elegida
        SINO
            CONTINUAR con el bucle

DEFINIR función ingreso de descripción
    MIENTRAS VERDADERO
        LEER ingreso de descripción del usuario, almacenando en variable
        SI LLAMAR a función corrección con la descripción ingresada devuelve verdadero
            DEVOLVER descripción ingresada

DEFINIR función ingreso de año
    MIENTRAS VERDADERO
        LEER año ingresado por el usuario, almacenando en variable
        SI año equivale a un número y es mayor a 1900 y menor o igual a 2025
            SI LLAMAR a función corrección con el año ingresado devuelve verdadero
                DEVOLVER año convertido a entero
        SINO
            MOSTRAR mensaje de año inválido

DEFINIR función ingreso de mes
    MIENTRAS VERDADERO
        LEER mes ingresado por usuario, almacenando en variable
        SI mes equivale a un número Y 1 <= mes (convertido a entero) <= 12
            SI LLAMAR a función corrección con "El mes ingresado es: ${mes}"
                DEVOLVER mes (convertido a entero)
        SINO
            MOSTRAR mensaje de mes inválido

DEFINIR función ingreso_fecha()
    DEFINIR año como el resultado de llamar a la función de ingreso de año
    DEFINIR mes como el resultado de llamar a la función de ingreso de mes
    DEFINIR dias_x_mes como un diccionario con los días de cada mes
    SI mes es igual a 2 y la comprobación de si año es bisiesto da verdadera
        ASIGNAR 29 como valor al mes 2 en el diccionario
    MIENTRAS VERDADERO
        LEER día ingresado por usuario, almacenando en variable
        SI día equivale a un número Y 1 <= día (convertido a entero) <= dias_x_mes[mes]
            SI LLAMAR a función corrección con la fecha ingresada como parámetro
                DEVOLVER día convertido a entero, mes, año
        MOSTRAR mensaje de día inválido

DEFINIR función registrar_gasto()
    DEFINIR monto como el resultado de llamar a la función ingreso de monto
    DEFINIR categoria como el resultado de llamar a la función ingreso de categoria
    DEFINIR descripción como el resultado de llamar a la función ingreso de descripción
    MOSTRAR mensaje de carga de fecha
    DEFINIR día, mes, año como el resultado de llamar a la función ingreso de fecha
    DEFINIR gasto como un diccionario con "Monto", "Categoría", "Descripción", "Día", "Mes", "Año"
    DEVOLVER gasto

DEFINIR función consultar gasto por fecha específica
    DEFINIR día, mes, año como el resultado de llamar a ingreso de fecha
    DEFINIR variable encontrado como FALSO
    POR cada gasto en lista de gastos
            SI el día, mes y año ingresado es igual a día, mes y año en gasto de la lista
                ASIGNAR VERDADERO a variable encontrado
                MOSTRAR gasto
    SI encontrado es igual a FALSO
        MOSTRAR mensaje de falta de datos para esa fecha

DEFINIR función consultar gasto por mes
    DEFINIR mes como el resultado de llamar a ingreso de mes
    DEFINIR encontrado como FALSO
    POR cada gasto en lista de gastos
        SI el mes ingresado es igual a mes del gasto en la lista
            ASIGNAR VERDADERO a encontrado
            MOSTRAR gasto
    SI encontrado es igual a FALSO
        MOSTRAR "No se encontraron gastos para ese mes."

DEFINIR función consultar gasto por año
    DEFINIR año como el resultado de llamar a ingreso de año
    DEFINIR encontrado como FALSO
    POR cada gasto en lista de gastos
        SI año ingresado es igual a año de gasto en la lista
            ASIGNAR VERDADERO a encontrado
            MOSTRAR gasto
    SI encontrado es igual a FALSO
        MOSTRAR "No se encontraron gastos para ese año."

DEFINIR función consultar gasto por categoria
    DEFINIR categoria como el resultado de llamar a ingreso de categoria
    DEFINIR encontrado como FALSO
    POR cada gasto en gastos_lista
        SI categoría ingresada es igual a categoría de gasto en la lista
            ASIGNAR VERDADERO a encontrado
            MOSTRAR gasto
    SI encontrado es igual a FALSO
        MOSTRAR mensaje de no encontrado

DEFINIR función mostrar total
    DEFINIR variable total como la suma de los montos de cada gasto en la lista de gastos
    MOSTRAR cantidad de gastos registrados
    MOSTRAR el total de la suma de los gastos
    MOSTRAR el promedio de los gastos de la lista

DEFINIR función mostrar lista completa formateada
    POR cada gasto en lista de gastos
        MOSTRAR los valores almacenados en la lista, con sus datos correspondientes
##########################################################################################

INICIO del programa

    MOSTRAR mensaje de bienvenida
    LEER nombre del usuario, almacenando en una variable
    CREAR lista de gastos vacía

    BUCLE PRINCIPAL
        LLAMAR a función menú, con los parámetros:
            1 - Registrar gasto
            2 - Consultar gasto
            3 - Salir

        SI elige opción 1 ENTONCES
            LLAMAR a función para registrar gasto
            GUARDAR los datos del gasto en la lista de gastos
            MOSTRAR mensaje de éxito al registrar datos

        SI elige opción 2 ENTONCES
            SI hay registros en la lista de gastos:
                LLAMAR a la función menú con los parámetros:
                    1 - Por fecha exacta
                    2 - Por mes
                    3 - Por año
                    4 - Por categoría
                    5 - Total y promedio
                    6 - Mostrar lista completa de gastos
                SEGÚN opción elegida
                    LLAMAR a la función correspondiente
            SI NO
                MOSTRAR "No hay gastos registrados"

        SI elige opción 3 ENTONCES
            MOSTRAR mensaje de despedida
            TERMINAR

        SI opción inválida
            MOSTRAR "Opción inválida", volver al bucle

FIN BUCLE
'''

# FUNCIONES
#
#Muestra cualquier menú y retorna la elección válida
def menu(opciones):
    while True:
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i} - {opcion}")
        eleccion = input("Ingrese su elección (por ej.: 1): ").strip()

        if eleccion.isdigit():
            eleccion = int(eleccion)
            if 1 <= eleccion <= len(opciones):
                return eleccion
        print("Opción inválida. Intente nuevamente.\n")

# Confirmación de entrada
def correccion(datos_ingresados):
    while True:
        print(f"Los datos ingresados son: {datos_ingresados}")
        sel_correcta = input("Esto es correcto? S/N ").strip().lower()
        if sel_correcta == "s":
            return True
        elif sel_correcta == "n":
            return False
        else:
            print("Opción inválida, intente nuevamente.\n")

def ingreso_monto():
    # Comprobación de ingreso de monto
    while True:
        try:
            input_monto = float(input("Ingrese el monto gastado (ej.: 210.50): $").strip())
            if input_monto > 0:
                return input_monto
            else:
                print("El monto debe ser un número positivo.\n")
        except ValueError:
            print("Monto inválido.\n")

# Ingreso de categoría
def ingreso_categoria():
    while True:
        opcion_cat = ["Vivienda", "Alimentos", "Servicios", "Salud", "Transporte",
              "Entretenimiento y ocio", "Compras personales"] # Categorías posibles
        opcion_elegida = menu(opcion_cat) # Llama a función menu y guarda en una variable
        cat_elegida = opcion_cat[opcion_elegida - 1] # Coteja la opción ingresada con la lista de categorias. Poner -1 es para equiparar la elección del usuario con el sistema de conteo que arranca de 0
        if correccion(f"Categoría seleccionada {cat_elegida}"):
            return cat_elegida
        else:
            continue

# Ingreso descripción
def ingreso_descripcion():
    while True:
        descripcion_input = input("Describa en qué se gastó: ").strip()
        if correccion(f"Descripción ingresada: {descripcion_input}"):
            return descripcion_input

# Ingreso de año
def ingreso_anio():
    while True:
        anio = input("Ingrese el año (ej.: 2022): ").strip()
        if anio.isdigit() and 1900 < int(anio) <= 2025:
            if correccion(f"El año ingresado es: {anio}"):
                return int(anio)
        else:
            print("Año inválido.\n")

# Ingreso de mes
def ingreso_mes():
    while True:
        mes = input("Mes (ej.: 03): ").strip()
        if mes.isdigit() and 1 <= int(mes) <= 12:
            if correccion(f"El mes ingresado es: {mes}"):
                return int(mes)
        else:
            print("Mes inválido.\n")

# Ingreso fecha exacta
def ingreso_fecha():
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
                return int(dia), mes, anio
        print("Día inválido.\n")

# Ejecuta el proceso de carga y validación de gastos
def registrar_gasto():
    # Ingreso de monto
    monto = ingreso_monto()
    # Ingreso categoría
    categoria = ingreso_categoria()
    # Ingreso de descripción
    descripcion = ingreso_descripcion()
    #Ingreso de fecha
    print("Excelente! Ahora anotemos la fecha en la que se realizó el gasto")
    dia, mes, anio = ingreso_fecha()
    gasto = {"Monto" : monto, "Categoría" : categoria,
                     "Descripción" : descripcion, "Día" : dia, "Mes" : mes, "Año" : anio
             }
    return gasto

# Filtra gastos por fecha específica
def consultar_gasto_fecha():
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
        if not encontrado:
            print("No se encontraron gastos para esa fecha.\n")

# Consultar gasto por mes
def consultar_gasto_mes():
    mes = ingreso_mes()
    encontrado = False
    for gasto in gastos_lista:
        if gasto["Mes"] == mes:
            encontrado = True
            print(f"Monto: ${gasto['Monto']}, Categoría: {gasto['Categoría']}, "
                  f"Descripción: {gasto['Descripción']}, "
                  f"Fecha: {gasto['Día']:02}/{gasto['Mes']:02}/{gasto['Año']}\n")
        if not encontrado:
            print("No se encontraron gastos para ese mes.\n")

# Consultar gasto por año
def consultar_gasto_anio():
    anio = ingreso_anio()
    encontrado = False
    for gasto in gastos_lista:
        if gasto["Año"] == anio:
            encontrado = True
            print(f"Monto: ${gasto['Monto']}, Categoría: {gasto['Categoría']}, "
                  f"Descripción: {gasto['Descripción']}, "
                  f"Fecha: {gasto['Día']:02}/{gasto['Mes']:02}/{gasto['Año']}\n")
        if not encontrado:
            print("No se encontraron gastos para ese año.\n")

# Filtra gastos por categoría
def consultar_gasto_categoria():
    categoria = ingreso_categoria()
    encontrado = False
    for gasto in gastos_lista:
        if gasto["Categoría"] == categoria:
            encontrado = True
            print(f"Monto: ${gasto['Monto']}, Categoría: {gasto['Categoría']}, "
                  f"Descripción: {gasto['Descripción']}, "
                  f"Fecha: {gasto['Día']:02}/{gasto['Mes']:02}/{gasto['Año']}\n")
        if not encontrado:
            print("No se encontraron gastos para esa categoría.\n")

# Muestra total, promedio y cantidad de gastos
def mostrar_total():
    total = sum(gasto["Monto"] for gasto in gastos_lista)
    print(f"Hay {len(gastos_lista)} gastos anotados")
    print(f"El total de gastos es de : ${total}")
    print("El gasto promedio es de : $", total / len(gastos_lista),"\n")

# Muestra toda la lista de gastos, formateada
def mostrar_lista_completa():
    for gasto in gastos_lista:
        print((f"Monto: ${gasto['Monto']}, Categoría: {gasto['Categoría']}, "
                  f"Descripción: {gasto['Descripción']}, "
                  f"Fecha: {gasto['Día']:02}/{gasto['Mes']:02}/{gasto['Año']}\n"))
########################################################################################

# Bienvenida al programa
print("Hola, bienvenido a REVI, tu ayudante para registrar y revisar tus gastos!")

# Ingreso de nombre del usuario
nombre_usuario = input("Me dirías tu nombre? ")

# Ingreso al menú de opciones
print(f"Un placer {nombre_usuario.strip()}! Por favor selecciona una opción para continuar:")

gastos_lista = [] #lista donde se van a almacenar los datos

# Inicio de bucle para el menú
while True:
    # Llamado a la función menú
    opcion = menu(["Registrar gasto", "Consultar gasto", "Salir"])

    if opcion == 1:
        gasto = registrar_gasto()
        gastos_lista.append(gasto)
        print("El gasto fue registrado exitosamente!")

    elif opcion == 2:
        if gastos_lista:
            opcion_submenu = menu(["Consultar gasto por día específico", "Consultar gasto por mes",
                              "Consultar gasto por año", "Consultar gasto por categoría",
                              "Consultar gasto total","Ver lista completa de gastos"])
            if opcion_submenu == 1:
                consultar_gasto_fecha()
            if opcion_submenu == 2:
                consultar_gasto_mes()
            if opcion_submenu == 3:
                consultar_gasto_anio()
            if opcion_submenu == 4:
                consultar_gasto_categoria()
            if opcion_submenu == 5:
                mostrar_total()
            if opcion_submenu == 6:
                mostrar_lista_completa()

        else:
            print("No hay gastos registrados.\n")


    elif opcion == 3:
        print(f"Gracias por usar REVI, {nombre_usuario}. ¡Hasta la próxima!")
        break

    else:
        print("Opción inválida, por favor seleccione 1, 2 o 3.\n")