from tabulate import tabulate
import json

def ver_descuentos():
    """ Muestra todos los descuentos disponibles
 
        pre: Ninguna
 
        post: Muestra una lista con los descuentos disponibles
    """
    with open("descuentos.json") as contenido:
            descuentos = json.load(contenido)

    lista_descuentos = descuentos["descuentos_semanales"]

    for descuento in lista_descuentos:
        print(f"{descuento["nombre_dia"]}, {descuento["descuento"]}, {descuento["metodo_de_pago"]}")

def modificar_descuento(dia: str, nuevo_descuento: int, nuevo_metodo_de_pago: str):
    """ Modifica un descuento existente
    
        pre: dia es un string que representa el dia de la semana, nuevo_descuento es un numero entre 0 y 100 y nuevo_metodo_de_pago representa el medio de pago por el cual se aplica el descuento
    
        post: Modifica el descuento en la base de datos
    """
    with open("descuentos.json", "r", encoding='utf-8') as contenido:
            descuentos = json.load(contenido)

    lista_descuentos = descuentos["descuentos_semanales"]

    dia_encontrado = False
    
    for descuento in lista_descuentos:
        if descuento["nombre_dia"].lower() == dia.lower():
            descuento["descuento"] = nuevo_descuento
            descuento["metodo_de_pago"] = nuevo_metodo_de_pago
            dia_encontrado = True
            print(f"Datos para {dia} actualizados")
            break

    if dia_encontrado == True:
        with open("descuentos.json", "w", encoding='utf-8') as contenido:
            json.dump(descuentos, contenido, indent=4, ensure_ascii=False)
        print(f"Archivo '{"descuentos.json"}' guardado con éxito")
    else:
        print(f"No se encontró el día {dia} El archivo no fue modificado")

def mostrar_opciones():
    opciones = [
        ["1", "Ver Descuentos"],
        ["2", "Modificar Descuento"],
        ["0", "Salir"]
    ]
        
    return (tabulate(opciones, headers=["Opción", "Descripción"], tablefmt='fancy_grid', colalign=("center", "left")))

def menu():

    while True:

        opciones = mostrar_opciones()
        print(opciones)

        op = input("Ingrese una opcion: ")

        if op == "0":
            print("Saliendo...")
            break


        elif op == "1":
            ver_descuentos()
            

        elif op == "2":
            dia = input("Ingrese el dia a modificar: ")
            nuevo_descuento = int(input("Ingrese el nuevo descuento (entre 0 y 100): "))
            nuevo_metodo_de_pago = input("Ingrese el nuevo metodo de pago: ")
            modificar_descuento(dia, nuevo_descuento, nuevo_metodo_de_pago)
            

        else:
            print("Opcion invalida")

def main():
    menu()

if __name__ == "__main__":
    main()
