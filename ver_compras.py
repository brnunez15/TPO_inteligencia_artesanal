from tabulate import tabulate
from typing import List

def filtrar_por_fecha(compras: dict, d: int, m: int, a: int):
    """
    busca un registro de las compras y la filtra por fecha.

    post: devuelve el registro de la compra de una fecha especifica.
    """

    """suponiendo que compra es un diccionario con todas las compras realizadas y una de sus claves es fecha. 
    Compara la fecha de la compra con la compra ingresada por el usuario.
    Si coincide, retorna la compra seleccionada"""

    fecha = (d,m,a)
    compras_encontradas = list()

    for compra in compras.values():
        if compra.get("fecha") == fecha:
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

def menu() -> None:
    while True:

        opciones = mostrar_opciones()
        print(opciones)

        op = input("Ingrese una opcion: ")

        if op == "0":
            print("Saliendo...")
            break

        elif op == "1":
            print("\nBusca la compra filtrada por fecha.\n")
            print("INGRESA LA FECHA DE LA COMPRA\n")

            dia = int(input("Ingrese el dia: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))

            compra_filtrada = filtrar_por_fecha(compras, dia, mes, anio)
            
            if compra_filtrada:
                print(compra_filtrada)
            else:
                print(f"No se encontro una compra en la fecha {dia, mes, anio}")

        else:
            print("Opcion invalida")

compras = {
        1: {"cliente" : "Brisa Nuñez", "producto": "Remera", "descripcion": "roja", "cantidad": 1, "fecha": (1,10,2025)},
        2: {"cliente" : "Natalia Lescano", "producto": "Short", "descripcion": "jean", "cantidad": 3, "fecha": (1,1,2012)},
        3: {"cliente" : "Luka Peralta", "producto": "Buzo", "descripcion": "Negro", "cantidad": 1, "fecha": (1,10,2025)},
        4: {"cliente" : "Sebastian Carini", "producto": "cinto", "descripcion": "marron", "cantidad": 2, "fecha": (15,9,2025)},
    }

def main():
    menu()

if __name__ == "__main__":
    main()