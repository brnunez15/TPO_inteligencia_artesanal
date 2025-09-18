from tabulate import tabulate

def ver_descuentos():
    """ Muestra todos los descuentos disponibles

        pre: Ninguna

        post: Muestra una lista con los descuentos disponibles

    """
    pass

def agregar_descuento(porcentaje: int, descripcion: str):
    """ Agrega un nuevo descuento
    
        pre: porcentaje es un numero entre 0 y 100 y descripcion representa el medio de pago por el cual se aplica el descuento
    
        post: Agrega el descuento a la base de datos
    """
    pass

def eliminar_descuento(descuento_id: int):
    """ Elimina un descuento existente
    
        pre: descuento_id entero que representa el id del descuento a eliminar
    
    
        post: Elimina el descuento del archivo 
    """
    pass

def mostrar_opciones():
    opciones = [
        ["1", "Ver Descuentos"],
        ["2", "Agregar Descuento"],
        ["3", "Eliminar Descuento"],
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
            ver_descuentos()
            pass

        elif op == "2":
            agregar_descuento()
            pass

        elif op == "3":
            eliminar_descuento()
            pass

        else:
            print("Opcion invalida")

def main():
    menu()

if __name__ == "__main__":
    main()
