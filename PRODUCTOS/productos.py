from tabulate import tabulate 
import json
import os 
from actualizar_producto import main as actualizar_main


def opciones_categorias():
    '''
    muestra un menu de opciones de categorias de productos en formato de tabla y devuelve la lista de opciones.
    pre: 
        - no ingresa ningun valor como parametro.
    post: 
        - retorna una lista de listas, en donde cada lista continene dos strings (opcion numerica y nombre de la categoria).
    '''

    opciones = [
        ['1', 'accesorios'],
        ['2', 'remeras'],
        ['3', 'pantalones'],
        ['4', 'buzo'],
        ['5', 'zapatos']
    ]

    print( tabulate(
        opciones,
        headers=['opcion', 'categoria'],
        tablefmt= 'fancy_grid',
        colalign=('center', 'left')
    ))
    return opciones


def ver_producto(ruta_json: str)-> None:
    '''
    pide al usuario que seleccione una categoria y muestre los productos de esa categoria desde un archivo JSON en formato de tabla.

    Pre:
        - recibe la ruta del archivo json.
        - la categoria en el JSON deben coincidir con las opciones disponibles.

    post:
        - muestra por consola una tabla con los productos filtrados por la categoria seleccionada, o un mensaje si no hay productos o si hay errores.
    '''

    opciones = opciones_categorias()


    while True:
        try:
            op_categoria = int(input('ingrese una opcion (1-5) para la categoria: '))
            if op_categoria >= 1 or op_categoria <= 5:
                break
            else:
                print('error: debe seleccionar una opcion entre el 1 y el 5')
        except ValueError:
            print('error: debe ingresar un numero entero')


    try: 
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        print('error: el archivo no existe.')
        return
    except json.JSONDecodeError:
        print('error: el archivo no es un JSON valido.')


    categoria_elegida = opciones[op_categoria -1][1]
    productos_filtrados = [producto for producto in inventario if producto.get('categoria') == categoria_elegida]

    if not productos_filtrados:
        print('no hay productos en la categoria seleccionada.')
        return 

    headers = ['ID', 'CATEGORIA', 'NOMBRE', 'STOCK', 'PRECIO']
    dato_tabla = []
    
    for producto in productos_filtrados:
        dato_tabla.append ([
            producto['id'],
            producto['categoria'],
            producto['nombre'],
            producto['stock'],
            f'${producto['precio']:.2f}'
        ])
        
    print(f"\nproductos en la categoria ' {categoria_elegida}':")
    print(tabulate(dato_tabla, headers=headers, tablefmt='grid'))


def generar_id(ruta_json):
    '''
    genera un id para un producto que se va incrementando.
    
    pre:
        - recibe la ruta del json.

    post:
        - retorna un int del valor del id.
    '''
    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        inventario = json.load(archivo)

    if inventario:
        ultimo_id = max(producto['id'] for producto in inventario)
        return ultimo_id + 1


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
            seleccion_categoria = int(input('seleccione la categoria (del 1 al 5) del producto que quiere ingresar: '))
            if seleccion_categoria >= 1 or seleccion_categoria <= 5:
                break
            else:
                print('error: debe seleccionar una opcion entre el 1 y el 5')
        except ValueError:
            print('error: debe ingresar un numero entero')

    if seleccion_categoria == 1:
        return 'accesorios'
    elif seleccion_categoria == 2:
        return 'remeras'
    elif seleccion_categoria == 3:
        return 'pantalones'
    elif seleccion_categoria == 4:
        return 'buzo'
    else:
        return 'zapatos'


def ingresar_producto(ruta_json:str) -> tuple:
    '''
    solicita al usuario que ingrese los datos de un nuevo producto.

    pre:
        - recibe un str de la ruta del archivo json.

    post:
        - retorna una tupla con los datos el producto ingresado.
    '''

    id_producto = generar_id(ruta_json)
    categoria = elegir_categoria()
    nombre_producto = input('ingrese el nombre del producto: ')
    stock_producto = int(input('ingrese el stock de la prenda: '))
    precio_entero = int(input('ingrese el precio de la prenda: '))
    precio_en_decimal = float(precio_entero)
    
    return(id_producto, categoria, nombre_producto,precio_en_decimal,stock_producto)


def agregar_producto(ruta_json) -> None:
    '''
    agregar un producto al archivo json (inventario).

    Pre:
        - el json debe existir y contener una lista de diccionarios.
        - ingresan 5 parametros (2 enteros, 2 strings y 1 float)
    
    Post:
        - muestra un mensaje por consola confirmando que el producto se agrego.
        - muestra por consola una tabla con todos los datos del produucto ingresado.
    '''

    id_producto, categoria, nombre_producto, precio_en_decimal, stock_producto = ingresar_producto(ruta_json)

    nuevo_producto = {
        'id': id_producto,
        'categoria': categoria,
        'nombre': nombre_producto,
        'precio': precio_en_decimal,
        'stock': stock_producto
    }
    
    try:
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        inventario = [nuevo_producto]
    
    inventario.append(nuevo_producto)

    try: 
        with open(ruta_json, 'w', encoding='utf-8') as archivo:
            json.dump(inventario, archivo, indent=4)
    except IOError as e:
        print(f'error al escribir en el archivo: {e}')
        
    print(f'Producto {nombre_producto} se agrego al inventario.')

    headers = ['ID', 'CATEGORIA', 'NOMBRE', 'STOCK', 'PRECIO']
    dato_tabla = []
    
    dato_tabla.append ([
        nuevo_producto['id'],
        nuevo_producto['categoria'],
        nuevo_producto['nombre'],
        nuevo_producto['stock'],
        f'${nuevo_producto['precio']:.2f}'
    ])
    
    print(tabulate(dato_tabla, headers=headers, tablefmt='grid'))


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

    try:
        opciones = opciones_productos()
        print(opciones)

        op = input('ingrese una opcion: ')

        if op == '0':
            exit()

        elif op == '1':
            carpeta_actual = os.path.dirname(__file__)
            ruta_json = os.path.join(carpeta_actual, '..', 'inventario.json')
            ver_producto(ruta_json)

        elif op == '2':
        
            carpeta_actual = os.path.dirname(__file__)
            ruta_json = os.path.join(carpeta_actual, '..', 'inventario.json')
            agregar_producto(ruta_json)

        elif op == '3':
            actualizar_main()

    except IndexError: 
        print('opcion invalida')


def main():
    '''
    funcion principal del modulo, llama al menu del producto.
    '''
    menu_productos()


if __name__ == '__main__':
    main()