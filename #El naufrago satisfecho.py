#El naufrago satisfecho
print("----Bienvenido al Naufrago Satisfecho----")

def menu(opcion):
    print("--------Menu-------")
    print("1) Ordenar")
    print("2) Salir")
    opcion=int(input("Ingrese la opcion:"))
    return opcion

def hamburguer(sp,dp,tp):
   print("Seleccione el tipo de hamburguesa")
   print("1) Sencillas")
   print("2) Dobles")
   print("3) Triples")
   hambur=int(input("Ingrese la opcion:"))
   if hambur == 1:
      s=int(input("Cuantas hamburguesas sencillas desea: "))
      sp=s*20
      print(f"El precio de sus: {s} hamburguesas es de: {sp}")
   elif hambur == 2:
      d=int(input("Cuantas hamburguesas sencillas desea: "))
      dp=d*25
      print(f"El precio de sus: {d} hamburguesas es de: {dp}")
   elif hambur == 3:
      t=int(input("Cuantas hamburguesas sencillas desea: "))
      tp=t*28
      print(f"El precio de sus: {t} hamburguesas es de: {tp}")
    
      return sp,dp,tp

def tarjeta():
   print("Seleccione su metodo de pago")
   

def main():
  sp=0
  dp=0
  tp=0
  opcion = 0
  while (opcion != 2):
      opcion = menu(opcion)
      if opcion == 1:
        hamburguer(sp,dp,tp)
      
  print("Muchas gracias por utilizar nuestro sistema")

main()