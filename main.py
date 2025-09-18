from tabulate import tabulate
from cargar_compra import main as compra_main
from os import system, name

def limpiar_pantalla() -> None:
    """
    Pre: No hay condiciones previas.
    Post: Limpia la pantalla del terminal.
    """
    system("cls" if name == "nt" else "clear")


def mostrar_opciones():
    limpiar_pantalla()
    opciones = [
        ["1", "Cargar Compra"],
        ["2", "Ver Compras"],
        ["3", "Productos"],
        ["4", "Descuentos"],
        ["5", "Cierre de Caja"],
        ["0", "Salir"]
    ]
        
    return (tabulate(opciones, headers=["Opción", "Descripción"], tablefmt='fancy_grid', colalign=("center", "left")))

def menu():

    while True:

        opciones = mostrar_opciones()
        print(opciones)

        op = input("Ingrese una opcion: ")

        if op == "0":
            print("Saliendo...")
            break

        elif op == "1":
            compra_main()

        elif op == "2":
            pass

        elif op == "3":
            pass

        elif op == "4":
            pass

        elif op == "5":
            pass

        else:
            print("Opcion invalida")

def main():
    menu()

if __name__ == "__main__":
    main()