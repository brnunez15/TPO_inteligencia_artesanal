from tabulate import tabulate
from cierre_caja import main as cierre_main
from ver_compras import main as compras_main
from cargar_compra import main as cargar_main
from PRODUCTOS.productos import main as productos_main
from descuentos import main as descuentos_main

def mostrar_opciones() -> str:
    """
    Muestra todas las opciones del menú principal.

    Post:
        - retorna un strin que muestra la matriz de opciones en formato tabla.
    """
    opciones = [
        ["1", "Cargar Compra"],
        ["2", "Ver Compras"],
        ["3", "Productos"],
        ["4", "Descuentos"],
        ["5", "Cierre de Caja"],
        ["0", "Salir"]
    ]

    return (tabulate(opciones, headers=["Opción", "Descripción"], tablefmt='fancy_grid', colalign=("center", "left")))

def menu() -> None:
    """
    Menú principal del programa.
    """
    while True:

        opciones = mostrar_opciones()
        print(opciones)

        op = input("Ingrese una opcion: ")

        if op == "0":
            print("Saliendo...")
            break

        elif op == "1":
            cargar_main()

        elif op == "2":
            compras_main()

        elif op == "3":
            productos_main()

        elif op == "4":
            descuentos_main()

        elif op == "5":
            cierre_main()

        else:
            print("Opcion invalida")

def main() -> None:
    """
    Función principal del programa.
    """
    menu()

if __name__ == "__main__":
    main()