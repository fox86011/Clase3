print("**********ELECTROMEGA**********\n")
print("Ingrese los datos para la placa de su Dron\n")
# Solicitar datos al cliente
base = float(input("Ingrese la base de la placa de circuito (en cm): "))
altura = float(input("Ingrese la altura de la placa de circuito (en cm): "))
altura2 = float(input("Ingrese la altura menor de la placa de circuito (en cm): "))
# Cálculo del área 
area = ((base * (altura-altura2)) / 2)+(base+altura2)
# Impresión del resultado
print("El área de la placa de circuito es:", area, "cm²")