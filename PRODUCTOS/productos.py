from tabulate import tabulate 
from .actualizar_producto import main as actualizar_main


def ver_producto():
    '''
    muestra un diccionario con todos los datos de los productos actuales.
    '''
    pass


def agregar_producto():
    '''
    permite agregar un producto nuevo al diccionario de productos
    '''
    pass


def opciones_productos():
    '''
    muestra las opciones de la pestaña de productos.

    Pre:
        - no ingresa ningun valor como parametro.

    Post:
        - devuelve una matriz con las opciones del menu.
    '''

    opciones = [
        ['1', 'Ver productos'],
        ['2', 'Agregar productos'],
        ['3', 'Actualizar Producto'],
        ['0', 'Salir']
    ]

    return tabulate(
        opciones, 
        headers=["Opción", "Descripción"], 
        tablefmt='fancy_grid', 
        colalign=("center", "left")
        )


def menu_productos():
    '''
    compara la opción que ingreso el usuario con las opciones del menu y llama a las funciones.
    '''

    while True:
        opciones = opciones_productos()
        print(opciones)

        op = input('ingrese una opcion: ')

        if op == '0':
            break

        elif op == '1':
            ver_producto()

        elif op == '2':
            agregar_producto()

        elif op == '3':
            actualizar_main()

        else: 
            print('opcion incorrecta')


def main():
    '''
    funcion principal del modulo, llama al menu del producto.
    '''
    menu_productos()


if __name__ == '__main__':
    main()