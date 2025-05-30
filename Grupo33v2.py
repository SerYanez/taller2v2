# PROGRAMA DE REGISTRO DE GASTOS DIARIOS
#
# La finalidad del programa es de tener un registro de los gastos del usuario, pidiendo que
# ingrese los datos requeridos y categorizando de una manera conveniente cada gasto. Se añade a
# una versión anterior la capacidad de tener múltiples entradas de gastos, con implementación de funciones
# y manejo de errores
#
# ################## PSEUDOCÓDIGO ########################
from os.path import split


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
        print("Opción inválida. Intente nuevamente.")

# Confirmación de entrada
def correccion(datos_ingresados):
    while True:
        print(f"Los datos ingresados son: {datos_ingresados}")
        sel_correcta = input("Esto es correcto? S/N").strip().lower()
        if sel_correcta == "s":
            return True
        elif sel_correcta == "n":
            return False
        else:
            print("Opción inválida, intente nuevamente.")

def ingreso_monto():
    # Comprobación de ingreso de monto
    while True:
        try:
            input_monto = float(input("Ingrese el monto gastado (ej.: 210.50): $").strip())
            return input_monto
        except ValueError:
            print("Monto inválido.")

# Ingreso de categoría
def ingreso_categoria():
    while True:
        opcion_cat = ["Vivienda", "Alimentos", "Servicios", "Salud", "Transporte",
              "Entretenimiento y ocio", "Compras personales"] # Categorías posibles
        opcion_elegida = menu(opcion_cat) # Llama a funcion menu y guarda en una variable
        cat_elegida = opcion_cat[opcion_elegida - 1] # Coteja la opción ingresada con la lista de categorias
        if correccion(f"Categoría seleccionada {cat_elegida}"):
            categoria_final = cat_elegida[1]
            return categoria_final
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
        if (anio.isdigit() and 1900 < int(anio) <= 2025):
            if correccion(f"El año ingresado es: {anio}"):
                return int(anio)
        else:
            print("Año inválido.")

# Ingreso de mes
def ingreso_mes():
    while True:
        mes = input("Mes (ej.: 03): ").strip()
        if (mes.isdigit() and 1 <= int(mes) <= 12):
            if correccion(f"El mes ingresado es: {mes}"):
                return int(mes)
        else:
            print("Mes inválido.")

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
        dia = input(f"Ingrese el día (ej.: 02): (1-{dias_x_mes[mes]})").strip()
        if dia.isdigit() and 1 <= int(dia) <= dias_x_mes[mes]:
            if correccion(f"Fecha ingresada: {int(dia):02}/{mes:02}/{anio}"):
                return int(dia), mes, anio
        print("Día inválido.")


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
            print(f"${gasto}\n")
        if not encontrado:
            print("No se encontraron gastos para esa fecha.")

# Consultar gasto por mes
def consultar_gasto_mes():
    mes = ingreso_mes()
    encontrado = False
    for gasto in gastos_lista:
        if (gasto["Mes"] == mes):
            encontrado = True
            print(f"${gasto}\n")
        if not encontrado:
            print("No se encontraron gastos para ese mes.")

# Consultar gasto por año
def consultar_gasto_anio():
    anio = ingreso_anio()
    encontrado = False
    for gasto in gastos_lista:
        if (gasto["Año"] == anio):
            encontrado = True
            print(f"${gasto}\n")
        if not encontrado:
            print("No se encontraron gastos para ese año.")

# Filtra gastos por categoría
def consultar_gasto_categoria():
    categoria = ingreso_categoria()
    encontrado = False
    for gasto in gastos_lista:
        if (gasto["Categoría"] == categoria):
            encontrado = True
            print(f"${gasto}\n")
        if not encontrado:
            print("No se encontraron gastos para esa categoría.")

# Muestra total, promedio y cantidad de gastos
def mostrar_total():
    total = sum(gasto["Monto"] for gasto in gastos_lista)
    print(f"Hay {len(gastos_lista)} gastos anotados")
    print(f"El total de gastos es de : ${total}")
    print("El gasto promedio es de : $", total / len(gastos_lista))
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
            opcion_submenu = menu(["1 -Consultar gasto por día específico", "2 -Consultar gasto por mes",
                              "3 -Consultar gasto por año", "4 -Consultar gasto por categoría",
                              "5 -Consultar gasto total","6 -Ver lista completa de gastos"])
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
                print(gastos_lista)

        else:
            print("No hay gastos registrados.")


    elif opcion == 3:
        print("Gracias por usar REVI. ¡Hasta la próxima!")
        break

    else:
        print("Opción inválida, por favor seleccione 1, 2 o 3.")