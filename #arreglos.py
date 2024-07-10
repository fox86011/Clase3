#arreglos
import random
import webbrowser

nombres=[]
huellas=[]
codigo=[]
numPersona=0

def menu_opciones():
   
    print("Que accion desea realizar")
    print("1) Ingresar Usuario")
    print("2) Mostrar Usuario")
    print("3) Buscar y enviar codigo de recuperacion")
    print("4) Salir")
    return int(input("Ingresar la opcion: "))


def ingreso_personal(numPersona):
    for i in range(numPersona):
      if numPersona>0:
        print(f"Ingrese los datos de la persona {i+1}")
        nombreusuario=input("Ingrese el nombre: ")
        huellausuario=input("Ingrese la huella: ")
        nombres.append(nombreusuario)
        huellas.append(random.randrange(1000,9999))
      else:
        print("ERROR NUMERO NO VALIDO")



def mostrar_personal(numPersona):
    for i in range(numPersona):
        print("---------------------")
        print(f"Mostrar los datos de la persona {i+1}")
        print(f"* Nombre {nombres[i]}")
        print(f"* Huella {huellas[i]}")
        print(f"* Codigo {codigo[i]}")




def main():
    caso=menu_opciones()
    print("----------SISTEMA-DACTILAR-P60----------")
    print("--------------Bienvenid@---------")

    while caso!=4:
        if caso== 1:
            numPersona=int(input("Ingrese el numero de personas a registrar: "))
            ingreso_personal(numPersona)
            caso=menu_opciones()
           
        elif caso == 2:
            mostrar_personal(numPersona)
            caso = menu_opciones()
        elif caso == 3:
            print("Caso - 3")
            caso = menu_opciones()
    
    print("Muchas Gracias")



main()