from tabulate import tabulate
from typing import List
from datetime import datetime

def calcular_cierre(dict_compras, fecha):#resumen
    """
    Va a sumar todos los productos que se agregaron a la compra y si hay descuentos, los aplica.

    Post: retorna el resultado de la compra.
    """
    precios = [compra.get("precio") for compra in dict_compras.values() if compra.get("fecha") == fecha]
    return sum(precios)

def ver_total_cierre(dict_compras, fecha):
    """
    Muestra el resumen de los productos vendidos del dia.

    Post: retorna el resumen detallado simulando un ticket o comprobante de compra.
    """
    resumen = [compra for compra in dict_compras.values() if compra.get("fecha") == fecha]

    if not resumen:
        print("No se registraron compras en la fecha indicada.")
        return

    tabla = [
        [compra["cliente"], compra["producto"], compra["cantidad"], compra["precio"]]
        for compra in resumen
    ]

    print(tabulate(tabla, headers=["Cliente", "Producto", "Cantidad", "Precio"], tablefmt="fancy_grid"))
    print(f"\nTotal del día: ${sum([c['precio'] for c in resumen])}\n")


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
    while True:

        opciones = mostrar_opciones()
        print(opciones)

        op = input("Ingrese una opcion: ")

        if op == "0":
            print("Saliendo...")
            break

        elif op == "1":
            print("\n----Calcula el cierre de caja----\n")
            fecha_actual = datetime.now()
            fecha_hoy = (fecha_actual.day, fecha_actual.month, fecha_actual.year)
            cierre = calcular_cierre(compras, fecha_hoy)
            print(f"\n----CIERRE DEL DIA {fecha_actual.strftime('%d/%m/%Y')} a las {fecha_actual.strftime('%H:%M:%S')}----\n")
            print(f"El total de las compras del dia es: ${cierre}")

        elif op == "2":
            print("Muestra el total del cierre de caja.")
            fecha_actual = datetime.now()
            fecha_hoy = (fecha_actual.day, fecha_actual.month, fecha_actual.year)
            ver_total_cierre(compras, fecha_hoy)

        else:
            print("Opcion invalida")

compras = {
    1: {"cliente" : "Brisa Nuñez", "producto": 1, "cantidad": 1, "fecha": (1,10,2025), "precio": 15000},
    2: {"cliente" : "Natalia Lescano", "producto": 2, "cantidad": 3, "fecha": (1,1,2012), "precio": 50000},
    3: {"cliente" : "Luka Peralta", "producto": 3, "cantidad": 1, "fecha": (1,10,2025), "precio": 70000},
    4: {"cliente" : "Sebastian Carini", "producto": 4, "cantidad": 2, "fecha": (15,9,2025), "precio": 5000},
    5: {"cliente" : "Sebastian Carini", "producto": 4, "cantidad": 2, "fecha": (31,10,2025), "precio": 5000},
    6: {"cliente" : "Luka Peralta", "producto": 3, "cantidad": 1, "fecha": (31,10,2025), "precio": 70000}

}

productos = {
    1: {"nombre": "remera", "descripcion": "roja"},
    2: {"nombre": "short", "descripcion": "jean"},
    3: {"nombre": "buzo", "descripcion": "negro"},
    4: {"nombre": "cinto", "descripcion": "marron"}
}

def main() -> None:
    menu()

if __name__ == "__main__":
    main()