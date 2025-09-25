# Exclusivo para Windows
from datetime import date
import robot as robot, os as os

def limpiar():
    os.system("clear")

limpiar()
print("-------------------")
print("     LIMPIBOT      ")
print("-------------------")

input("> Presione cualquier botón para continuar...")

limpiar()
print("Limpibot es un robot de limpieza especializado con detectores de proximidad.\nEste programa permite controlarlo de forma remota.")
input("> Presione cualquier botón para continuar...")
limpiar()

color = str.lower(input("Elige un color!\nRojo, Amarillo o Verde\n> "))
if (color == "rojo" or color == "amarillo" or color == "verde"):
    pass
else:
    print("Color inválido! Color por default (Blanco)")
    color = "blanco"
limpiar()

limpibot = robot.robot("Limpibot", str(color), str(date.today()), "MARK-1", 1)

print(limpibot)
input("> Presione cualquier botón para continuar...")

while True:
    limpiar()
    print("-----MENU-----")
    print(limpibot.circuito.estado_circuito())
    print("(P)render - (A)pagar - (D)etectar - (S)alir")
    eleccion = str.upper(input("> "))

    if (eleccion == "S"):
        limpiar()
        print("Gracias por usar este sistema!\n Programado por Benitez, Gigli, Magne y Pacheco para 6°1° ETP")
        break
    elif (eleccion == "P"):
        limpibot.circuito.encender()
    elif (eleccion == "A"):
        limpibot.circuito.apagar()
    elif (eleccion == "D"):
        if (limpibot.circuito.get_estado() == "encendido"):
            limpibot.sensor.alertar(5)
            limpibot.circuito.consumir_energia(5)
        else:
            print("El robot está apagado!")
            input("> Presione cualquier botón para continuar...")
    else:
        print("Elección inválida")
