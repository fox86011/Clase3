# Ejercicio 5
# Crear un sistema online que les permita a los clientes recibir de premio un viaje por el promedio de compras.

# Se solicitan los datos.
# Nombre
name = input("Enter your name please: ")

# Edad
age = int(input("Enter your age please: "))

# Promedio de compras realizadas (valor en dólares)
average = int(input("Enter the average amount of your purchases: "))

# Si el cliente es mayor a 18 años y la compra realizada supera los $500 o más gana a un viaje a los EE.UU.
if age >= 18 and average >= 500:
    print("Congratulations, you won a trip to the United States!")
    print("Have a nice trip!")

# Si el cliente es mayor a 18 años y la compra realizada esta entre el rango de los $300 a $499 gana un viaje a España.
if age >= 18 and 300 <= average <= 499:
    print("Congratulations, you won a trip to Spain!")
    print("Have a nice trip!")

# Si el cliente es mayor a 18 años y la compra realizada está entre el rango de los $200 a $299 gana un viaje a
# Colombia.
if age >= 18 and 200 <= average <= 299:
    print("Congratulations, you won a trip to Colombia!")
    print("Have a nice trip!")

# Por otra parte, si el cliente es mayor a 18 años y la compra realizada esta entre el rango de los $100 a $199 gana
# un viaje a Galápagos.
if age >= 18 and 100 <= average <= 199:
    print("Congratulations, you won a trip to Galapagos!")
    print("Have a nice trip!")

# Si el cliente es menor a 18 años y la compra realizada esta entre el rango de los $50 a $99 gana un viaje a Guayaquil.
if age < 18 and 50 <= average <= 99:
    print("Congratulations, you won a trip to Guayaquil!")
    print("Have a nice trip!")

# Finalmente, si el total de las compras son menores a $49 sin importar la edad no recibe un premio.
if average <= 49:
    print("Sorry, you didn't win a trip.")
    print("Have a nice day!")

print("Bye!")
