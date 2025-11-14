from tabulate import tabulate
from typing import List
from datetime import datetime

def leer_archivo() -> List[dict]:
    """
    Lee un archivo y transforma las lineas del mismo en una lista de diciconarios, donde cada diccionario es la una linea del archivo.

    Post:
        - devuelve la lista de diccionarios creada.
    """
    try:
        with open("archivos/CSV/registro_compras.csv", "rt", encoding="utf-8-sig") as contenido:
            lineas = [linea.strip() for linea in contenido.readlines()]
            encabezado = lineas[0].split(",")
            registros = []
            for linea in lineas[1:]:
                valores = linea.split(",")
                registro = dict(zip(encabezado, valores))
                registros.append(registro)
            return registros
    except FileNotFoundError:
        print("El archivo Json no se encontro.")
    except Exception:
        print("ERROR la leer el archivo Json.")


def calcular_cierre(lista_compras: list[dict], fecha:str) -> float:
    """
    Va a sumar todos los productos que se agregaron a la compra y si hay descuentos, los aplica.

    Pre:
        - lista_compras: recibe la lista de diccionarios de las compras que fueron realizadas.
        - fecha: recibe la fecha del dia de hoy.

    Post: retorna el resultado de la compra.
    """
    precios = [float(compra["Total"] )for compra in lista_compras if compra.get("Fecha") == fecha]
    return sum(precios)

def ver_total_cierre(lista_compras: list[dict], fecha:str) -> None:
    """
    Muestra el resumen de los productos vendidos del dia. Incluyendo el total de los productos.

    Pre:
        - lista_compras: recibe una lista de diccionarios de las compras realizadas del dia.
        -fecha: recibe la fecha del dia de hoy.
    
    """
    resumen = [compra for compra in lista_compras if compra.get("Fecha") == fecha]

    if not resumen:
        print("No se registraron compras en la fecha indicada.")
        return

    tabla = [
        [
            compra["Producto"],
            compra["Cantidad"],
            f"${compra['Precio Unitario']}",
            f"${compra['Subtotal']}",
            f"{compra["Descuento"]}%",
            f"${compra['Total']}"
        ]
        for compra in resumen
    ]

    print("\nResumen de compras del día:\n")
    print(tabulate(tabla, headers=["Producto", "Cantidad", "Precio Unitario", "Subtotal", "Descuento", "Total"], tablefmt="fancy_grid"))
    total = sum(float(c["Total"]) for c in resumen)
    print(f"\nTotal del día: ${total:.2f}\n")

def mostrar_opciones() -> List[list[str]]:
    """
    Muestra las opciones del menu en una matriz.
    Cada lista dentro de la matriz representa cada opcion del menu.

    Post: retorna una matriz con las opciones del menu.
    """
    opciones = [
        ["1", "Calcular Cierre de Caja."],
        ["2", "Ver Total Del Cierre."],
        ["0", "Salir"]
    ]
    return (tabulate(opciones, headers=["Opción", "Descripción"], tablefmt='fancy_grid', colalign=("center", "left")))

def menu() -> None:
    """
    Menu principal del modulo.
    """
    compras = leer_archivo()
    fecha_actual = datetime.now().date().strftime('%Y-%m-%d')
    hora_actual = datetime.now().time().strftime('%H:%M:%S')
    while True:

        opciones = mostrar_opciones()
        print(opciones)

        op = input("Ingrese una opcion: ")

        if op == "0":
            print("Saliendo...")
            break

        elif op == "1":
            print("\n----Calcula el cierre de caja----\n")

            cierre = calcular_cierre(compras, fecha_actual)
            print(f"\n----CIERRE DEL DIA {fecha_actual} a las {hora_actual}----\n")
            print(f"El total de las compras del dia es: ${cierre}")
            input("\nPresione Enter para continuar...")

        elif op == "2":
            print("Muestra el total del cierre de caja.")
            
            ver_total_cierre(compras, fecha_actual)

        else:
            print("Opcion invalida")

def main() -> None:
    """
    Funcion principal del programa.
    """
    menu()

if __name__ == "__main__":
    main()