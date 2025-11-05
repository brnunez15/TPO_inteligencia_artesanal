from tabulate import tabulate
import json
import os


def leer_archivo(ruta_json):
    
    try: 
        with open(ruta_json, 'rt', encoding='utf-8-sig') as archivo:
            inventario = json.load(archivo)
            return inventario
    except FileNotFoundError:
        print('error: el archivo no existe.')
        return
    except json.JSONDecodeError:
        print('error: el archivo no es un JSON valido.')



def elegir_categoria() -> str:
    '''
    muestra una tabla de opciones de categorias de productos y devuelve un string segun la opcion seleccionada.
    
    pre:
        - no recibe nada como parametro.

    post:
        - devuelve un str del nombre de la categoria del producto.
    '''
    
    categorias = [
        ['1', 'accesorios'],
        ['2', 'remeras'],
        ['3', 'pantalones'],
        ['4', 'buzo'],
        ['5', 'zapatos']
    ]

    print( tabulate(
        categorias,
        headers=['opcion', 'categoria'],
        tablefmt= 'fancy_grid',
        colalign=('center', 'left')
    ))

    while True:
        try:
            op_categoria = int(input('seleccione la categoria (del 1 al 5) del producto que quiere ingresar: '))
            if op_categoria >= 1 or op_categoria <= 5:
                break
            else:
                print('error: debe seleccionar una opcion entre el 1 y el 5')
        except ValueError:
            print('error: debe ingresar un numero entero')

    if op_categoria == 1:
        return 'accesorios'
    elif op_categoria == 2:
        return 'remeras'
    elif op_categoria == 3:
        return 'pantalones'
    elif op_categoria == 4:
        return 'buzo'
    else:
        return 'zapatos'


def actualizar_precio(ruta_json):


    lista_productos = []
    categoria_elegida = elegir_categoria()

    inventario = leer_archivo(ruta_json)

    for producto in inventario:
        if categoria_elegida == producto.get('categoria'):
            lista_productos.append(producto)


    try:
        id_a_buscar = int(input('seleccione el ID del producto que desee modificar: '))
        for producto in inventario:
            if id_a_buscar == producto.get('id'):
                nuevo_precio = int(input('ingrese un nuevo precio: '))
                producto['precio'] = nuevo_precio
        print(producto)
    except ValueError:
        print('error: debe ingresar un numero entero')

    
    
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

        carpeta_actual = os.path.dirname(__file__)
        ruta_json = os.path.join(carpeta_actual, '..', 'inventario.json')

        op = input('ingrese una opcion: ')

        if op == '0':
            from productos import main as productos_main
            productos_main()
        elif op == '1':
            actualizar_precio(ruta_json)
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
