import json
import os
from PRODUCTOS.utilidades import leer_archivo, mostrar_tabla, ver_productos

def mostrar_diccionario (diccionario: dict) -> None:
    for key, value in diccionario.items():
        print(f"{key}: {value}")

def ingresar_precio() -> int:
    while True:
        try:
            nuevo_precio = int(input("Ingresa un nuevo precio: "))
            break
        except ValueError:
            print("Debe ingresar un número entero válido.")
    return nuevo_precio

def ingresar_stock():
    while True:
        try:
            nuevo_stock = int(input("Ingrese un nuevo stock: "))
            break
        except ValueError:
            print("Debe ingresar un número entero válido: ")
    return nuevo_stock

def actualizar_precio(ruta_json: str) -> None:
    """
    Actualiza el precio de un producto.

    Pre: 
        - ruta_json: Recibe la ruta del archivo donde se modificará el producto.
    """
    while True:
        productos_filtrados = ver_productos(ruta_json)
        inventario = leer_archivo(ruta_json)
        if productos_filtrados:
            mostrar = [[producto['id'], producto['categoria'], producto['nombre'], producto['stock'], f'${producto['precio']:.2f}'] for producto in productos_filtrados]
            mostrar_tabla(mostrar, ['ID', 'CATEGORÍA', 'NOMBRE', 'STOCK', 'PRECIO'])
            break

    try:
        id_a_buscar = int(input('\nSeleccione el ID del producto que desee modificar: '))
        for producto in inventario:
            if id_a_buscar == producto.get('id'):
                nuevo_precio = ingresar_precio()
                producto['precio'] = nuevo_precio
                print("\n¡Producto actualizado con éxito!\n")
                mostrar_diccionario(producto)
        try:
            with open(ruta_json, 'wt', encoding='utf-8') as archivo:
                json.dump(inventario, archivo, indent=4)
        except FileNotFoundError as e:
            print(f'error: el archivo no existe. {e}')
    except ValueError:
        print('error: debe ingresar un numero entero')

def eliminar_producto(ruta_json: str) -> None:
    """
    Elimina un producto del archivo recibido.

    Pre:
        - ruta_json: recibe la ruta donde se eliminará el producto.

    """

    while True:
        productos_filtrados = ver_productos(ruta_json)
        inventario = leer_archivo(ruta_json)
        if productos_filtrados:
            mostrar = [[producto['id'], producto['categoria'], producto['nombre'], producto['stock'], f'${producto['precio']:.2f}'] for producto in productos_filtrados]
            mostrar_tabla(mostrar, ['ID', 'CATEGORÍA', 'NOMBRE', 'STOCK', 'PRECIO'])
            break

    producto_a_eliminar = {}

    try:
        id_a_buscar = int(input('seleccione el ID del producto que desee eliminar: '))
        for producto in inventario:
            if id_a_buscar == producto.get('id'):
                producto_a_eliminar = producto

        if producto_a_eliminar:
            inventario.remove(producto_a_eliminar)
            print("\n¡Producto eliminado exitosamente!\n")
        else:
            print("No se encontró el producto.")

        try:
            with open(ruta_json, 'wt', encoding='utf-8') as archivo:
                json.dump(inventario, archivo, indent=4)

        except FileNotFoundError as e:
            print(f'error: el archivo no existe. {e}')

    except ValueError:
        print('error: debe ingresar un numero entero')


def actualizar_stock(ruta_json):
    """
    Actualiza el stock de un producto.

    Pre: 
        - ruta_json: Recibe la ruta del archivo donde se modificará el producto.
    """
    while True:
        productos_filtrados = ver_productos(ruta_json)
        inventario = leer_archivo(ruta_json)
        if productos_filtrados:
            mostrar = [[producto['id'], producto['categoria'], producto['nombre'], producto['stock'], f'${producto['precio']:.2f}'] for producto in productos_filtrados]
            mostrar_tabla(mostrar, ['ID', 'CATEGORÍA', 'NOMBRE', 'STOCK', 'PRECIO'])
            break
    try:
        id_a_buscar = int(input('\nSeleccione el ID del producto que desee modificar: '))
        for producto in inventario:
            if id_a_buscar == producto.get('id'):
                nuevo_stock = ingresar_stock()
                producto['stock'] = nuevo_stock
                print("\n¡Producto actualizado con éxito!\n")
                mostrar_diccionario(producto)
        try:
            with open(ruta_json, 'wt', encoding='utf-8') as archivo:
                json.dump(inventario, archivo, indent=4)
        except FileNotFoundError as e:
            print(f'error: el archivo no existe. {e}')
    except ValueError:
        print('error: debe ingresar un numero entero')

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
    return opciones

def submenu_actualizacion():
    '''
    compara la opción que ingreso el usuario con las opciones del menu y llama a las funciones.
    '''

    while True:
        opciones = opciones_actualizar()
        mostrar_tabla(opciones, ['Opción', 'Descripción'])

        carpeta_actual = os.path.dirname(__file__)
        ruta_json = os.path.join(carpeta_actual, '..', 'inventario.json')
        op = input('Ingrese una opción: ')

        if op == '0':
            print("Volviendo al menú de productos...\n")
            break
        if op == '1':
            actualizar_precio(ruta_json)
        elif op == '2':
            eliminar_producto(ruta_json)
        elif op == '3':
            actualizar_stock(ruta_json)
        else:
            print('Opción incorrecta')

def main():
    '''
    funcion principal del modulo, llama al menu del producto.
    '''
    submenu_actualizacion()

if __name__ == '__main__':
    main()