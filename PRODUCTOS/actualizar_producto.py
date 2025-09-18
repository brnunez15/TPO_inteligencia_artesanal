from tabulate import tabulate

def actualizar_precio():
    '''
    busca el producto que se quiera modificar y el cambia el dato precio.
    '''
    pass


def eliminar_producto():
    '''
    busca el producto que se quiera eliminar y lo elimina del diccionario de productos.
    '''
    pass


def actualizar_stock():
    '''
    busca el producto y modifica la cantidad.
    '''
    pass


def opciones_actualizar():
    '''
    muestra las opciones de la subpestaña actualizar.
    
    Pre:
        - no ingresa ningun valor como parametro.
    Post:
        - devuelve una matriz con las opciones del menu.
    '''
    opciones = [
        ['1', 'Actualizar Precio'],
        ['2', 'Eliminar producto'],
        ['3', 'Actualizar stock'],
        ['0', 'Salir']
    ]

    return tabulate(
        opciones, 
        headers=["Opción", "Descripción"], 
        tablefmt='fancy_grid', 
        colalign=("center", "left")
        )
        

def submenu_actualizacion():
    '''
    compara la opción que ingreso el usuario con las opciones del menu y llama a las funciones.
    '''

    while True:
        opciones = opciones_actualizar()
        print(opciones)

        op = input('ingrese una opcion: ')

        if op == '0':
            break
        elif op == '1':
            actualizar_precio()
        elif op == '2':
            eliminar_producto()
        elif op == '3':
            actualizar_stock()
        else:
            print('opcion incorrecta')


def main():
    '''
    funcion principal del modulo, llama al menu del producto.
    '''

    submenu_actualizacion()


if __name__ == '__main__':
    main()
