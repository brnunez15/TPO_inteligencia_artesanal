from tabulate import tabulate
import json
from typing import Dict

def validar_metodos(metodo: str) -> bool:
    """
    Valida el metodo de pago recibido.

    Pre:
        -metodo: recibe el metodo a validar.

    Post:
        True: si el metodo se encuentra en la lista de metodos validos.
        False: en caso contrario.
    """
    metodos_de_pago = ["visa", "transferencia", "mastercard", "efectivo", "qr"]
    return metodo in metodos_de_pago

def leer_descuentos() -> Dict[str, list[dict]]:
    """ Lee los descuentos desde el archivo descuentos.json
 
        post: Devuelve un diccionario con los descuentos leidos del archivo
    """
    try:
        with open("archivos/JSON/descuentos.json", "r", encoding='utf-8') as contenido:
            descuentos = json.load(contenido)
            return descuentos
        
    except FileNotFoundError:
        print("El archivo descuentos.json no se encontro")
    except json.JSONDecodeError:
        print("Error al leer el archivo descuentos.json")

def ver_descuentos(dict_descuentos: dict[list[dict]]) -> None:
    """
    Muestra todos los descuentos semanales disponibles.

    Pre:
        - dict_descuentos: recibe un diccionario con todos los descuentos.
    """

    descuentos = dict_descuentos.get("descuentos_semanales", [])
    datos_tabla = []

    for descuento in descuentos:
        fila = [
            descuento.get("nombre_dia", "No Encontrado"),
            f'{descuento.get("descuento", 0)}%',
            descuento.get("metodo_de_pago", "No Encontrado")
        ]
        datos_tabla.append(fila)

    print("\n Descuentos Semanales Disponibles \n")
    if datos_tabla:
        print(tabulate(datos_tabla, headers=["Día", "Descuento", "Método de Pago"], tablefmt="fancy_grid"))
    else:
        print("No hay descuentos para mostrar.")

def modificar_descuento(dia: str, nuevo_descuento: int, nuevo_metodo_de_pago: str, dict_descuentos: list[dict]) -> None:
    """ Modifica un descuento de un determinado dia de la semana.
      Modifica el descuento en el arcghivo descuentos.json si el dia existe
    
        pre: dia es un string que representa el dia de la semana
        nuevo_descuento es un numero entre 0 y 100 que representa el valor del descuento
        y nuevo_metodo_de_pago representa el medio de pago por el cual se aplica el descuento
    """

    descuentos = dict_descuentos.get("descuentos_semanales", [])
    dia_encontrado = False

    for descuento in descuentos:
        if descuento["nombre_dia"].lower() == dia.lower():
            dia_encontrado = True
            descuento["descuento"] = nuevo_descuento
            descuento["metodo_de_pago"] = nuevo_metodo_de_pago
            print(f"\nDatos para {dia} actualizados\n")
            break

    if dia_encontrado:
        try:
            with open("archivos/JSON/descuentos.json", "wt", encoding='utf-8') as contenido:
                json.dump(dict_descuentos, contenido, indent=4, ensure_ascii=False)
            print("\nArchivo guardado con éxito\n")
        except FileNotFoundError:
            print("El archivo descuentos.json no se encontro")
        except json.JSONDecodeError:
            print("Error al leer el archivo descuentos.json")
        except IOError:
            print("Error al guardar el archivo descuentos.json")
        except Exception as e:
            print(f"error inesperado: {e}")
    else:
        print(f"No se encontró el día {dia} El archivo no fue modificado")

def mostrar_opciones() -> str:
    """
    Muestra las opciones del menu del modulo descuentos.py.

    Post:
        - devuelve un str en formato tabla de la matriz de opciones.
    """
    opciones = [
        ["1", "Ver Descuentos"],
        ["2", "Modificar Descuento"],
        ["0", "Salir"]
    ]
        
    return (tabulate(opciones, headers=["Opción", "Descripción"], tablefmt='fancy_grid', colalign=("center", "left")))

def menu() -> None:
    """
    Menu principal del modulo.
    """
    descuentos = leer_descuentos()
    while True:

        opciones = mostrar_opciones()
        print(opciones)

        op = input("Ingrese una opcion: ")

        if op == "0":
            print("Saliendo...")
            break

        elif op == "1":
            
            ver_descuentos(descuentos)

        elif op == "2":
            dias_validos = ["domingo", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
            
            while True:
                dia = input("Ingrese el nombre del dia a modificar: ").lower().strip()
                if dia in dias_validos:
                    break
                print("\nDia invalido. Vuelve a intentarlo\n")
            
            while True:
                nuevo_metodo_de_pago = input("Ingrese el nuevo metodo de pago: ").lower().strip()
                if validar_metodos(nuevo_metodo_de_pago):
                    break
                print("\nMetodo ingresado invalido. Vuelva a intentarlo.\n")

            while True:
                try:
                    nuevo_descuento = int(input("Ingrese el nuevo descuento (entre 0 y 100): "))
                except ValueError:
                    print("\nIngrese solo un número entero.\n")
                else:
                    if nuevo_descuento <= 100 and nuevo_descuento >= 0:
                        break
                    else:
                        print("El descuento debe estar entre 0 y 100")
            modificar_descuento(dia, nuevo_descuento, nuevo_metodo_de_pago, descuentos)
        else:
            print("Opcion invalida")

def main() -> None:
    """
    Funcion principal del programa.
    """
    menu()

if __name__ == "__main__":
    main()