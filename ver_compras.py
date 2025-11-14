from tabulate import tabulate
from typing import List, Tuple

def mostrar_compras(lista_compras: list[dict]) -> None:
    """
    Muestra todas las compras realizadas del dia de hoy.

    Pre:
        - lista_compras: lista de diccionarios de todas las compras realizadas.
    """
    if not lista_compras:
        print("No hay registros de compras.")
        return

    tabla = [
        [
            compra["Fecha"],
            compra["Hora"],
            compra["Producto"],
            compra["Cantidad"],
            f"${compra['Precio Unitario']}",
            f"${compra['Subtotal']}",
            f"{compra["Descuento"]}%",
            f"${compra['Total']}"
        ]
        for compra in lista_compras
    ]

    print(tabulate(
        tabla,
        headers=["Fecha", "Hora", "Producto", "Cantidad", "Precio Unitario", "Subtotal", "Descuento", "Total"],
        tablefmt="fancy_grid"
    ))

def leer_archivo() -> List[dict]:
    """
    Lee un archivo y transforma las lineas del mismo en una lista de diciconarios, donde cada diccionario es la una linea del archivo.

    Post:
        - devuelve la lista de diccionarios creada.
    """
    try:
        with open("archivos/CSV/registro_compras.csv", "rt", encoding="utf-8-sig") as contenido:
            lineas = [linea.strip() for linea in contenido.readlines()]
            encabezado = lineas[0].split(",")
            registros = []
            for linea in lineas[1:]:
                valores = linea.split(",")
                registro = dict(zip(encabezado, valores))
                registros.append(registro)
            return registros
    except FileNotFoundError:
        print("El archivo, no se encontro.")
    except Exception:
        print("ERROR la leer el archivo.")

def filtrar_por_fecha(lista_compras: list[dict], desde: Tuple[int,int,int], hasta: Tuple[int,int,int]) -> List[dict]:
    """
    busca un registro de las compras y la filtra por un rango de fechas.

    pre:
        - lista_compras: lista de diccionarios, donde cada diccionario son todas las compras registradas.
        - desde: tupla con una fecha (numeros enteros)
        - hasta: tupla con una fecha (numeros enteros)

    post: 
        - compras_encontradas: devuelve una lista con el/los registros de las compras de un rango de fechas.

    """

    fecha_desde = (desde[2], desde[1], desde[0])
    fecha_hasta = (hasta[2], hasta[1], hasta[0])

    compras_encontradas = []

    for compra in lista_compras:
        fecha_str = compra["Fecha"]
        anio, mes, dia = map(int, fecha_str.split("-"))
        fecha_compra = (anio, mes, dia)

        if fecha_desde <= fecha_compra <= fecha_hasta:
            compras_encontradas.append(compra)

    return compras_encontradas


def mostrar_opciones() -> List[list[str]]:
    """
    Muestra las opciones del menu en una matriz.
    Cada lista dentro de la matriz representa cada opcion del menu.

    Post: retorna una matriz con las opciones del menu.
    """
    opciones = [
        ["1", "Buscar compras por fecha."],
        ["0", "Salir"]
    ]

    return (tabulate(opciones, headers=["Opción", "Descripción"], tablefmt='fancy_grid', colalign=("center", "left")))

def validar_fecha(fecha: Tuple[int, int, int]) -> bool:
    """
    Valida una fecha recibida como tupla (día, mes, año).

    Pre: 
        - Recibe una tupla de 3 enteros positivos.
    Post: 
        - Devuelve True si la fecha es válida.
    """
    dia, mes, anio = fecha

    es_valida = True
    
    if not (1900 <= anio <= 2025):
        es_valida = False

    elif not (1 <= mes <= 12):
        es_valida = False

    else:
        if mes in (1, 3, 5, 7, 8, 10, 12):
            es_valida = 1 <= dia <= 31

        elif mes in (4, 6, 9, 11):
            es_valida = 1 <= dia <= 30

        elif mes == 2:
            if es_bisiesto(anio):
                es_valida = 1 <= dia <= 29
            else:
                es_valida = 1 <= dia <= 28
    
    return es_valida

def es_bisiesto (anio: int) -> bool:
    """
    Verifica si un año ingresado es bisiesto, o no.

    Pre: El número ingresado tiene que ser un entero positivo.

    Post: Retornará (True) si el año es bisiesto. Por lo contrario retorna (False).
    """
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0

def menu() -> None:
    """
    Menu de cer compras.
    """
    compras = leer_archivo()

    while True:

        opciones = mostrar_opciones()
        print(opciones)

        op = input("Ingrese una opcion: ")

        if op == "0":
            print("Saliendo...")
            break

        if op == "1":
            print("\nBusca la compra filtrada por fecha.\n")
            print("INGRESA LA FECHA DE LA COMPRA\n")

            while True:
                try:
                    print("FECHA DESDE:")
                    dia1 = int(input("Ingrese el dia: "))
                    mes1 = int(input("Ingrese el mes: "))
                    anio1 = int(input("Ingrese el año: "))

                except ValueError:
                    print("Fecha invalida. Debe ingresar un entero.\n")
                    continue

                fecha1 = (dia1, mes1, anio1)
                if validar_fecha(fecha1):
                    break
                print(f"La fecha {dia1}/{mes1}/{anio1} es inválida.\n")

            while True:
                try:
                    print("\nFECHA HASTA: ")
                    dia2 = int(input("Ingrese el dia: "))
                    mes2 = int(input("Ingrese el mes: "))
                    anio2 = int(input("Ingrese el año: "))
                except ValueError:
                    print("Fecha invalida. Debe ingresar un entero.\n")
                    continue

                fecha2 = (dia2, mes2, anio2)
                if validar_fecha(fecha2):
                    break
                print(f"La fecha {dia2}/{mes2}/{anio2} es inválida.\n")

            if (anio1, mes1, dia1) > (anio2, mes2, dia2):
                anio1, mes1, dia1, anio2, mes2, dia2 = anio2, mes2, dia2, anio1, mes1, dia1

            compra_filtrada = filtrar_por_fecha(compras, (fecha1), (fecha2))

            if compra_filtrada:
                mostrar_compras(compra_filtrada)
            else:
                print(f"No se encontro una compra entre las fechas {dia1}/{mes1}/{anio1} y {dia2}/{mes2}/{anio2}")

        elif op == "2":
            archivo = leer_archivo()
            print(archivo)
        else:
            print("Opcion invalida")

def main() -> None:
    """
    Funcion principal del programa.
    """
    menu()

if __name__ == "__main__":
    main()