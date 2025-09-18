from tabulate import tabulate
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
        ["1", "Agregar Producto"],
        ["2", "Ver Total de Compra"],
        ["3", "Finalizar Compra"],
        ["0", "Salir"]
    ]
        
    return (tabulate(opciones, headers=["Opción", "Descripción"], tablefmt='fancy_grid', colalign=("center", "left")))

def agregar_producto():
    """
    Permite agregar productos al sistema.
    
    Pre:
        - Solicita informacion del producto (stock, precio, descripción).
    
    Post:
        -  Retorna la lista de productos actualizada. 
    """
    pass

def total_compra():
    """
    Calcula el total de la compra realizada.
    
    Pre:
        - Recibe los productos de la compra (precio, cantidad).
    
    Post:
        - Retorna el total de la compra.
    """
    
    pass

def finalizar_compra():
    """
    Muestra el detalle de la compra realizada.
    
    Pre:
        - Recibe el registro de la compra. 
    
    Post:
        - Retorna el ticket de la compra. 
    """
    pass


def menu():
    """
    Verifica la opción del usuario.
    
    """
    while True:

        opciones = mostrar_opciones()
        print(opciones)

        op = input("Ingrese una opcion: ")

        if op == "0":
            print("Saliendo...")
            break

        elif op == "1":
            pass

        elif op == "2":
            pass

        elif op == "3":
            pass

        else:
            limpiar_pantalla()
            print("Opcion invalida")

def main():
    """"
    Funcion principal del programa, el usuario ingresa los números solicitados.
    
    """
    menu()

if __name__ == "__main__":
    main()