from tabulate import tabulate
from typing import List

def filtrar_por_fecha():
    """
    busca un registro de las compras y la filtra por fecha.

    post: devuelve el registro de la compra de una fecha especifica.
    """
    pass


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
            print("Busca la compra filtrada por fecha.")
            filtrar_por_fecha()

        else:
            print("Opcion invalida")

def main():
    menu()

if __name__ == "__main__":
    main()