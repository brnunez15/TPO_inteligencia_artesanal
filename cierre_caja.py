from tabulate import tabulate
from typing import List

def calcular_cierre():
    """
    Va a sumar todos los productos que se agregaron a la compra y si hay descuentos, los aplica.

    Post: retorna el resultado de la compra.
    """
    pass

def ver_total_cierre():
    """
    Muestra el total del cierre de la caja.

    Post: retorna un entero/flotante en representacion del total de la caja.
    """
    pass

def mostrar_opciones() -> List[list[str]]:
    """
    Muestra las opciones del menu en una matriz.
    Cada lista dentro de la matriz representa cada opcion del menu.

    Post: retorna una matriz con las opciones del menu.
    """
    opciones = [
        ["1", "Calcular Cierre de Caja."],
        ["2", "Ver Total Del Cierre."],
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
            print("Calcula el cierre de caja")
            calcular_cierre()

        elif op == "2":
            print("Muestra el total del cierre de caja.")
            ver_total_cierre()

        else:
            print("Opcion invalida")

def main() -> None:
    menu()

if __name__ == "__main__":
    main()