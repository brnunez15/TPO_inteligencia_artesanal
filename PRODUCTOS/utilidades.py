import json
from typing import List
from tabulate import tabulate

def leer_archivo(ruta_json: str) -> List[dict]:
    """
    Lee un archivo.

    Pre:
        - ruta_json: recibe la ruta donde se encuentra el archivo a leer.

    Post:
        - inventario: devuelve una lista de diccionarios. Donde cada elemento de la lista es el producto del inventario.
    """
    try:
        with open(ruta_json, 'rt', encoding='utf-8-sig') as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        print('ERROR: el archivo no existe.')
    except json.JSONDecodeError:
        print('ERROR: el archivo no es un JSON válido.')
    return inventario

def elegir_categoria() -> str:
    """
    El usuario elige una categoría de los productos.

    Post:
        - op_categoria: devuelve un string con la categoria que eligió el usuario.
    """
    opciones = opciones_categorias()
    mostrar_tabla(opciones, ['Opción','Categoría'])
    while True:
        try:
            op_categoria = int(input('\nIngrese una opción (1-5) para la categoría: '))
            if 5 >= op_categoria >= 1:
                op_categoria = opciones[op_categoria - 1][1]
                return op_categoria
            print('ERROR: debe seleccionar una opción entre 1 y el 5')
        except ValueError:
            print("Debe ingesar un número entero.")

def mostrar_tabla(mostrar: List[list], headers: List[str]) -> None:
    """
    Muestra en formato tabla una matríz.

    Pre:
        - mostrar: recibe la matríz que desea imprimir en formato tabla.
        - headers: recibe una lista con los headers que desea poner en la tabla.
    """
    try:
        print(tabulate(mostrar, headers=headers, tablefmt='fancy_grid', colalign=('center', 'left')))
    except IndexError:
        print("Error al mostrar la tabla")

def opciones_categorias() -> List[list[str]]:
    """
    Crea un menú de opciones de categorias de los productos en formato tabla.

    Post: 
        - opciones: retorna una lista de listas, en donde cada lista continene dos strings (opción numérica y nombre de la categoría).
    """
    opciones = [
        ['1', 'accesorios'],
        ['2', 'remeras'],
        ['3', 'pantalones'],
        ['4', 'buzo'],
        ['5', 'zapatos']
    ]
    return opciones

def ver_productos(ruta_json: str)-> List[dict]:
    """
    Filtra los productos de determinada categoría.

    Pre:
        - ruta_json: recibe la ruta donde se encuentra el archivo para buscar los productos.
    Post:
        - productos_filtrados: retorna una lista de diccionarios con los productos filtrados.
        Cada diccionario es un producto.
    """
    inventario = leer_archivo(ruta_json)
    categoria = elegir_categoria()
    productos_filtrados = [producto for producto in inventario if categoria == producto.get("categoria")]
    if not productos_filtrados:
        print(f"\nNo hay productos en la categoría '{categoria}'.\n")
        return []
    return productos_filtrados