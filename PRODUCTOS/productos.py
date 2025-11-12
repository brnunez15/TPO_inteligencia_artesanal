import json
import os
from typing import List, Tuple
from PRODUCTOS.actualizar_producto import main as actualizar_main
from PRODUCTOS.utilidades import leer_archivo, elegir_categoria, mostrar_tabla, ver_productos

def opciones_productos() -> List[list[str]]:
    """
    Crea las opciones de la pestaña de productos en una matríz.

    Post:
        - opciones: devuelve una matríz con las opciones del menú.
    """

    opciones = [
        ['1', 'Ver productos'],
        ['2', 'Agregar productos'],
        ['3', 'Actualizar Producto'],
        ['0', 'Salir']
    ]
    return opciones

def ingresar_id(ruta_json: str) -> int:
    """
    El usuario ingresa un id para asignarle a un nuevo producto.

    Pre:
        - ruta_json: recibe la ruta donde se encuentra el archivo con los productos ingresados.
        Esto es para validar que el id ingresado por el usuario no coincida con uno ya existente.
    Post:
        - id_producto: devuelve el id que el usuario eligió para el nuevo producto.
    """
    inventario = leer_archivo(ruta_json)
    while True:
        try:
            id_producto = int(input('Ingrese el ID del producto: '))
            existe = False
            for producto in inventario:
                if id_producto == producto.get("id"):
                    print(f"\nEl ID {id_producto} ya existe. Intente otra vez.\n")
                    existe = True
                    break
            if not existe:
                return id_producto
        except ValueError:
            print("\nDebe ingresar un número entero válido.\n")

def ingresar_producto(ruta_json: str) -> Tuple[int, str, str, float, int]:
    """
    Solicita al usuario que ingrese los datos de un nuevo producto.

    Pre:
        - ruta_json: recibe un str de la ruta del archivo json para ingresar el id del producto.
    Post:
        - TUPLA: retorna una tupla con los datos el producto ingresado.
            - id_producto: entero que representa el id del nuevo producto.
            - categoria: string de la categoría elegida.
            - nombre_producto: string del nombre del producto.
            - precio: flotante que representa el precio del nuevo producto.
            - stock_producto: entero que representa el stock del producto.
    """
    while True:
        id_producto = ingresar_id(ruta_json)
        categoria = elegir_categoria()
        nombre_producto = input('Ingrese el nombre del producto: ')
        while True:
            try:
                stock_producto = int(input('Ingrese el stock de la prenda: '))
                break
            except ValueError:
                print("\nDebe ingresar un número entero válido.\n")
        while True:
            try:
                precio = float(input('Ingrese el precio de la prenda: '))
                break
            except ValueError:
                print("\nDebe ingresar un número válido.\n")
        break
    return id_producto, categoria, nombre_producto, precio, stock_producto

def agregar_producto(ruta_json: str) -> None:
    """
    Agrega el producto (diccionario) previamente ingresado al archivo de la ruta recibida.

    Pre:
        - ruta_json: recibe la ruta de la cual se le agregará el producto ingresado.
    """
    id_producto, categoria, nombre_producto, precio, stock_producto = ingresar_producto(ruta_json)

    nuevo_producto = {
        'id': id_producto,
        'categoria': categoria,
        'nombre': nombre_producto,
        'precio': precio,
        'stock': stock_producto
    }

    inventario = leer_archivo(ruta_json)
    inventario.append(nuevo_producto)

    try:
        with open(ruta_json, 'wt', encoding='utf-8') as archivo:
            json.dump(inventario, archivo, indent=4)
    except FileNotFoundError as e:
        print(f"ERROR: No se encontró el archivo: {e}")
    except IOError as e:
        print(f'ERROR: hubo un error al escribir sobre el archivo: {e}')

    print("\n¡Producto agregado con exito!\n")
    mostrar = [[nuevo_producto['id'], nuevo_producto['categoria'], nuevo_producto['nombre'], nuevo_producto['stock'], f'${nuevo_producto['precio']:.2f}']]
    mostrar_tabla(mostrar, ['ID', 'CATEGORÍA', 'NOMBRE', 'STOCK', 'PRECIO'])

def menu_productos() -> None:
    """
    Menú principal de productos.
    """

    while True:
        carpeta_actual = os.path.dirname(__file__)
        ruta_json = os.path.join(carpeta_actual, '..', 'inventario.json')

        opciones = opciones_productos()
        mostrar_tabla(opciones, ['Opción', 'Descripción'])

        op = input('Ingrese una opción: ')

        if op == '0':
            print("Saliendo...")
            break

        if op == '1':
            productos = ver_productos(ruta_json)
            mostrar = [[producto['id'], producto['categoria'], producto['nombre'], producto['stock'], f'${producto['precio']:.2f}'] for producto in productos]
            mostrar_tabla(mostrar, ['ID', 'CATEGORÍA', 'NOMBRE', 'STOCK', 'PRECIO'])

        elif op == '2':
            agregar_producto(ruta_json)

        elif op == '3':
            actualizar_main()

        else:
            print("Opción inválida. Intentelo de nuevo.")

def main() -> None:
    """
    Función principal del módulo, llama al menú del producto.
    """
    menu_productos()

if __name__ == '__main__':
    main()