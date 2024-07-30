import random

detalleCompra =[[],[],[],[],[],[],[],[]]


def menuOpciones():
  print("¿Que acción desea realizar?")
  print('*  1) Registrar pedidos')
  print('*  2) Mostrar pedidos')
  print('*  3) Mostrar detalle de un pedido')
  print('*  4) Salir del sistema')
  while True:
    valor = input("Ingresa un número: ")
    if valor.isdigit():  # Verifica si el valor ingresado es un número
        numero = float(valor)
        break  # Sale del bucle si se ingresó un número válido
    else:
        print("Por favor, ingresa solo números. Inténtalo de nuevo.")

  return numero 
   


def ingresarPedido():
  print("\n\t\t Ingresar los datos del cliente \n")
  #nombre_cliente=input("Nombre: ")
  while True:
    nombre_cliente=str(input("Nombre: "))
    if len(nombre_cliente)<=10 and len(nombre_cliente)>=3:
        detalleCompra[0].append(nombre_cliente)
        break
    elif nombre_cliente.isdigit():
        print("ERROR")
        print("Ingresar un nombre y no un numero")
    else :
        print("ERROR")
        print("Ingrese un nombre valido")

  while True:  
    apellido_cliente=str(input("Apellido: "))
    if len(apellido_cliente)<=10 and len(apellido_cliente)>=3:
        detalleCompra[1].append(apellido_cliente)
        break
    elif apellido_cliente.isdigit():
        print("ERROR")
        print("Ingresar un apellido y no un numero")
    else :
        print("ERROR")
        print("Ingrese un apellido valido")  
    
  while True:
    telefono_cliente = input("Telefono: ")

    if telefono_cliente.isdigit() and len(telefono_cliente) >= 10:
        detalleCompra[2].append(telefono_cliente)
        break  
    else:
        print("Por favor, ingresa un número de teléfono válido.") 


  print("\n\t\t Ingresar los datos de la policrush\n")
  while True:
    nombre_policrush=str(input("Nombre: "))
    if len(nombre_policrush)<=10 and len(nombre_policrush)>=3:
        detalleCompra[3].append(nombre_policrush)
        break
    elif nombre_policrush.isdigit():
        print("ERROR")
        print("Ingresar un nombre y no un numero")
    else :
        print("ERROR")
        print("Ingrese un nombre valido")

  while True:  
    lugar_policrush=str(input("Dependencia: "))
    if len(lugar_policrush)<=15 and len(lugar_policrush)>=5:
        detalleCompra[4].append(lugar_policrush)
        break
    elif lugar_policrush.isdigit():
        print("ERROR")
        print("Ingresar una dependencia y no un numero")
    else :
        print("ERROR")
        print("Ingrese una dependencia valido")  
    
  while True:
    celular_policrush = input("Telefono: ")

    if celular_policrush.isdigit() and len(celular_policrush) >= 10:
        detalleCompra[5].append(celular_policrush)
        break  
    else:
        print("Por favor, ingresa un número de teléfono válido.") 

  detalleCompra[6].append(random.randrange(1000, 9999)) 

  print("\n\t\t Selección del regalo \n")
  print("1) Opción 1: Poliflor + Polipeluche = $2.50")
  print("2) Opción 2: Poliflor + Policarta = $1.50")
  print("3) Opción 3: Poliflor + Polillavero = $2.00")
  print("4) Opción 4: Poliflor + Polivaso = $2.75")

  opcion= int(input("Ingrese la opción: "))
  if   opcion==1:
   detalleCompra[7].append(2.50+(0.1*2.50))
  elif opcion==2:
   detalleCompra[7].append(1.50+(0.1*1.50))
  elif opcion==3:
   detalleCompra[7].append(2.00+(0.1*2.00))
  elif opcion==4:
   detalleCompra[7].append(2.75+(0.1*2.75))

  print("\n-------- Pedido registrado con éxito --------\n") 



def mostrarPedido(i):
    print("\t\n\n Datos del cliente")
    print("\t\t\t * Nombre:", detalleCompra[0][i])
    print("\t\t\t * Apellido:", detalleCompra[1][i])
    print("\t\t\t * Teléfono:", detalleCompra[2][i])
    print("\t\t\n Datos de la entrega")
    print("\t\t\t * Nombre:", detalleCompra[3][i])
    print("\t\t\t * Dependencia:", detalleCompra[4][i])
    print("\t\t\t * Teléfono:", detalleCompra[5][i])
    print("\t\t\n Datos del pago")
    print("\t\t\t * Código del pedido:", detalleCompra[6][i])      
    print("\t\t\t * Pago final: $", detalleCompra[7][i])





print("------------ MI POLICRUSH -------------")
print("\n\t\t *** Bienvenido(a) ***\n")
opcion= menuOpciones()
while opcion !=4:
  
  if opcion==1:
    print("\n----- Nuevo pedido -----")
    ingresarPedido()
    opcion= menuOpciones()
  
  elif opcion==2:
    if len(detalleCompra[0]) == 0:
      print("-------------------------------------\n")
      print("No existen pedidos registrados\n")
      print("-------------------------------------\n")
      opcion= menuOpciones() 
    else:
      print("\n------- Detalle de todos los pedidos ----------\n")
      for i in range(len(detalleCompra[0])):
        print("-------------------------------------")
        print("Detalle del pedido", i + 1)
        mostrarPedido(i)
        print("-------------------------------------")
      opcion= menuOpciones()  

  elif opcion==3:
    codigo=int(input("\n Ingrese el código del pedido: "))
    
    if codigo in detalleCompra[6]:
      dato = detalleCompra[6].index(codigo)
      for i in range(len(detalleCompra[0])):
        if i == dato:
          print("\t\t\t\n Pedido encontrado")
          print("-------------------------------------")
          print("Detalle")
          mostrarPedido(i)
          print("-------------------------------------")
    else:
      print("\n\n ******* ERROR *****\n")
      print("No existe ese código de pedido registrado\n")
    
    opcion= menuOpciones()

print("Muchas gracias")