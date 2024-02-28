#!/usr/bin/python3
import subprocess, sys






def main():
    limpiar_pantalla()
    mostrar_fecha()




def limpiar_pantalla():
    subprocess.run("clear")


def mostrar_fecha():


    fecha = subprocess.run(["date"],text=True, capture_output=True)
    if fecha.returncode != 0:
        print("Ha habido un problema")
        sys.exit(1)
   
    dia = fecha.stdout.strip().split(" ")[2]
    mes = fecha.stdout.strip().split(" ")[1]
    mes = convertir_mes(mes)
    año = fecha.stdout.strip().split(" ")[5]
   
    print(f"{dia}/{mes}/{año}")
   


def convertir_mes(mes):
    match mes:
        case "Jan":
            return "01"
        case "Feb":
            return "02"
        case "Mar":
            return "03"
        case "Apr":
            return "04"
        case "May":
            return "05"
        case "Jun":
            return "06"
        case "Jul":
            return "07"
        case "Aug":
            return "08"
        case "Sept":
            return "09"
        case "Oct":
            return "10"
        case "Nov":
            return "11"
        case "Dec":
            return "12"
        case _:
            return None


if __name__ == '__main__':
    main()
    