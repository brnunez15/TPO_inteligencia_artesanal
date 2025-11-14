from tabulate import tabulate
from os import system, name
import os
from datetime import datetime
import json
from typing import List
from descuentos import validar_metodos, leer_descuentos, ver_descuentos

def limpiar_pantalla() -> None:
    """
    Pre: No hay condiciones previas.
    Post: Limpia la pantalla del terminal.
    """
    system("cls" if name == "nt" else "clear")

def leer_archivo() -> List[dict]:
    """
    Lee un archivo json.

    Post:
        - ropa: devuelve una lista de diccionarios con todos los productos registrados en inventario.json.
    """
    try:
        with open("archivos/JSON/inventario.json", "rt", encoding="utf-8-sig") as contenido:
            productos = json.load(contenido)
            return productos

    except FileNotFoundError:
        print("El archivo Json no se encontro.")
        return
    except json.JSONDecodeError:
        print("ERROR la leer el archivo Json.")
        return

def mostrar_opciones() -> str:
    """
    Muestra las opciones de este modulo cargar_compra.py.

    Post:
        - devuelve la matriz en formato tabla.
    """
    opciones = [
        ["1", "Agregar Producto"],
        ["2", "Ver Total de Compra"],
        ["3", "Finalizar Compra"],
        ["0", "Salir"]
    ]
   
    return (tabulate(opciones, headers=["Opción", "Descripción"], tablefmt='fancy_grid', colalign=("center", "left")))

def agregar_producto() -> List[dict]:
    """
    Permite cargar productos existentes al carrito de compra. Descuenta el stock si se agrega un producto.

    Post:
        - retorna la lista de diccionarios de las compras realizadas.
    """
    productos = leer_archivo()
    if productos is None:
        return []

    compras = []

    while True:
        print("\nProductos disponibles:")
        tabla = [[p["id"], p["nombre"], f"${p['precio']}", p["stock"]] for p in productos]
        print(tabulate(tabla, headers=["ID", "Descripción", "Precio", "Stock"], tablefmt="fancy_grid"))
    
        try:
            id_seleccionado = int(input("\nIngrese el ID del producto que desea comprar (0 para salir): "))
            if id_seleccionado == 0:
                break
            while True:
                cantidad = int(input("Cantidad a comprar: "))
                if cantidad > 0:
                    break
                print("\nDebe ingresar una cantidad correcta.")
        except ValueError:
            print("Entrada inválida.")
            continue

        for producto in productos:
            if producto["id"] == id_seleccionado:
                if producto["stock"] >= cantidad:
                    producto["stock"] -= cantidad
                    compras.append({
                        "descripcion": producto["nombre"],
                        "precio_unitario": producto["precio"],
                        "cantidad": cantidad,
                        "subtotal": producto["precio"] * cantidad
                    })
                    print(f"{cantidad} unidad(es) de '{producto['nombre']}' agregadas.")
                else:
                    print("Stock insuficiente.")
                break
        else:
            print("Producto no encontrado.")

    try:
        with open("archivos/JSON/inventario.json", "w", encoding="utf-8") as archivo:
            json.dump(productos, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al actualizar el stock: {e}")
    return compras

def total_compra(compras: list[dict]) -> None:
    """
    Calcula y muestra por pantalla el total de la compra realizada.
    
    Pre:
        - recibe una lista de diccionarios con las compras que cargo el usuario.
    
    """
    
    if not compras:
        print("\nNo hay productos en la compra.\n")
        return
    tabla = [[item["descripcion"], item["cantidad"], f"${item['precio_unitario']}", f"${item['subtotal']}"] for item in compras]
    print("\nDetalle de la compra:")
    print(tabulate(tabla, headers=["Producto", "Cantidad", "Precio Unitario", "Subtotal"], tablefmt="fancy_grid"))

    total = sum(item["subtotal"] for item in compras)
        
    print(f"\nTotal acumulado: ${total}")
    input("\nPresione Enter para continuar...")

def finalizar_compra(compras: list[dict], metodo:str, dict_descuentos: dict[list[dict]]) -> None:
    """
    Finaliza la compra y la registra en un archivo csv. Muestra por pantalla el ticket final de la compra

    Pre:
        -compras: lista de diccionarios de todas las compras cargadas.
        - metodo: metodo de pago que ingresa el usuario.
        - dict_descuentos: recibe el diccionario con todos los descuentos semanales.
    """
    if not compras:
        print("\nNo hay productos en la compra.\n")
        input("Presione Enter para continuar...")
        return

    fecha = datetime.now().date()
    hora = datetime.now().strftime("%H:%M:%S")
    dia = fecha.weekday()

    descuentos = dict_descuentos.get("descuentos_semanales", [])
    descuento_aplicado = 0

    for desc in descuentos:
        if desc["dia"] == dia and desc["metodo_de_pago"].lower() == metodo.lower():
            descuento_aplicado = desc["descuento"]
            break

    print("\nTicket de compra:")
    tabla = [[item["descripcion"], item["cantidad"], f"${item['precio_unitario']}", f"${item['subtotal']}"] for item in compras]

    total_original = sum(item["subtotal"] for item in compras)
    monto_descuento = round(total_original * descuento_aplicado / 100, 2)
    total_final = round(total_original - monto_descuento, 2)

    tabla.append(["DESCUENTO", "-", f"{descuento_aplicado}%", f"-${monto_descuento}"])
    tabla.append(["TOTAL", "-", "-", f"${total_final}"])

    print(tabulate(
        tabla,
        headers=["Producto", "Cantidad", "Precio Unitario", "Subtotal"],
        tablefmt="fancy_grid"
    ))

    try:
        archivo_existe = os.path.exists("archivos/CSV/registro_compras.csv")
        with open("archivos/CSV/registro_compras.csv", "a", encoding="utf-8") as archivo:
            if not archivo_existe:
                archivo.write("Fecha,Hora,Producto,Cantidad,Precio Unitario,Subtotal,Descuento,Total\n")

            for item in compras:
                archivo.write(
                    f"{fecha},{hora},{item['descripcion']},{item['cantidad']},"
                    f"{item['precio_unitario']},{item['subtotal']},{descuento_aplicado},{total_final}\n"
                )

        print("Compra registrada en 'registro_compras.csv'.")
    except Exception as e:
        print(f"Error al guardar el ticket: {e}")

    compras.clear()
    input("Presione Enter para continuar...")

def menu() -> None:
    """
    Verifica la opción del usuario.
    
    """
    compras = []

    while True:
        limpiar_pantalla()
        opciones = mostrar_opciones()
        print(opciones)

        op = input("Ingrese una opcion: ")

        if op == "0":
            print("Saliendo...")
            break

        elif op == "1":
            nuevas_compras = agregar_producto()
            compras.extend(nuevas_compras)

        elif op == "2":
            total_compra(compras)

        elif op == "3":
            diccionario_descuentos = leer_descuentos()
            while True:
                ver_descuentos(diccionario_descuentos)
                metodo_pago = input("Ingrese el metodo de pago: ")
                if validar_metodos(metodo_pago):
                    break
                print("\nMetodo ingresado invalido. Vuelva a intentarlo.\n")
            
           
            finalizar_compra(compras, metodo_pago, diccionario_descuentos)

        else:
            limpiar_pantalla()
            print("Opcion invalida")

def main() -> None:
    """"
    Funcion principal del programa.
    
    """
    menu()
if __name__ == "__main__":
    main()