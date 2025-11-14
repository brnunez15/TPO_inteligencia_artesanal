import json
from .utilidades import leer_archivo, mostrar_tabla, ver_productos
from typing import List

def mostrar_diccionario (diccionario: dict) -> None:
    """
    Muestra un diccionario con su clave y valor.

    Pre:
        - diccionario: recibe el diccionario que desea mostar.
    """
    for key, value in diccionario.items():
        print(f"{key}: {value}")

def ingresar_precio() -> int:
    """
    Funcion que permite ingresar el precio (entero).

    Post:
        - nuevo_precio: retorna el numero ingresado por el usuario.
    """
    while True:
        try:
            nuevo_precio = int(input("Ingresa un nuevo precio: "))
            break
        except ValueError:
            print("Debe ingresar un número entero válido.")
    return nuevo_precio

def ingresar_stock() -> int:
    """
    Funcion que permite ingresar un nuevo stock (entero).

    Post:
        - nuevo_stock: retorna el stock o numero ingresado.
    """
    while True:
        try:
            nuevo_stock = int(input("Ingrese un nuevo stock: "))
            break
        except ValueError:
            print("Debe ingresar un número entero válido: ")
    return nuevo_stock

def actualizar_precio() -> None:
    """
    Actualiza el precio de un producto dentro del archivo inventario.json.
    """
    while True:
        productos_filtrados = ver_productos()
        inventario = leer_archivo()
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
            with open("./archivos/JSON/inventario.json", 'wt', encoding='utf-8') as archivo:
                json.dump(inventario, archivo, indent=4)
        except FileNotFoundError as e:
            print(f'error: el archivo no existe. {e}')
    except ValueError:
        print('error: debe ingresar un numero entero')

def eliminar_producto() -> None:
    """
    Elimina un producto del archivo inventario.json.
    """

    while True:
        productos_filtrados = ver_productos()
        inventario = leer_archivo()
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
            with open("./archivos/JSON/inventario.json", 'wt', encoding='utf-8') as archivo:
                json.dump(inventario, archivo, indent=4)

        except FileNotFoundError as e:
            print(f'error: el archivo no existe. {e}')

    except ValueError:
        print('error: debe ingresar un numero entero')

def actualizar_stock():
    """
    Actualiza el stock de un producto que se encuentra dentro del archivo inventario.json.
    """
    while True:
        productos_filtrados = ver_productos()
        inventario = leer_archivo()
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
            with open("./archivos/JSON/inventario.json", 'wt', encoding='utf-8') as archivo:
                json.dump(inventario, archivo, indent=4)
        except FileNotFoundError as e:
            print(f'error: el archivo no existe. {e}')
    except ValueError:
        print('error: debe ingresar un numero entero')

def opciones_actualizar() -> List[list[str]]:
    '''
    muestra las opciones de la subpestaña actualizar.

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

def submenu_actualizacion() -> None:
    '''
    compara la opción que ingreso el usuario con las opciones del menu y llama a las funciones.
    '''

    while True:
        opciones = opciones_actualizar()
        mostrar_tabla(opciones, ['Opción', 'Descripción'])
        op = input('Ingrese una opción: ')

        if op == '0':
            print("Volviendo al menú de productos...\n")
            break
        if op == '1':
            actualizar_precio()
        elif op == '2':
            eliminar_producto()
        elif op == '3':
            actualizar_stock()
        else:
            print('Opción incorrecta')

def main() -> None:
    '''
    funcion principal del modulo, llama al menu del producto.
    '''
    submenu_actualizacion()

if __name__ == '__main__':
    main()