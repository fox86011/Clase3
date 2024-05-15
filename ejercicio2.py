
def aplicar_aumento(nivel):
    if nivel == "inicial":
        aumento_porcentaje = 3
        nuevo_salario = salario_base * (1 + (aumento_porcentaje / 100))
        return aumento_porcentaje, nuevo_salario
    elif nivel == "medio":
        aumento_porcentaje = 10
        nuevo_salario = salario_base * (1 + (aumento_porcentaje / 100))
        return aumento_porcentaje, nuevo_salario
    elif nivel == "intermedio":
        aumento_porcentaje = 25
        nuevo_salario = salario_base * (1 + (aumento_porcentaje / 100))
        return aumento_porcentaje, nuevo_salario
    elif nivel == "avanzado":
        aumento_porcentaje = 45
        nuevo_salario = salario_base * (1 + (aumento_porcentaje / 100))
        return aumento_porcentaje, nuevo_salario
    else:
        aumento_porcentaje = "ninguno"
        nuevo_salario = "Nivel no valido"
        return aumento_porcentaje, nuevo_salario

# Mensaje de bienvenida
print("\n")
print("¡Bienvenido al sistema de cálculo de salario!".center(80))

# Solicitar nombre del usuario
nombre = input("\nPor favor, ingresa tu nombre: ")

# Saludo personalizado
print("\n")
print(f"Hola {nombre}!".center(80))

# Definir el salario base
salario_base = float(input("\nPor favor, ingresa tu salario base: "))

# Solicitar nivel
nivel = input("\nPor favor, ingresa tu nivel (inicial, medio, intermedio o avanzado): ").lower()

# Calcular salario actualizado
aumento_porcentaje, nuevo_salario = aplicar_aumento(nivel)

# Mostrar el salario actualizado
if nuevo_salario == "Nivel no válido":
    print("Error:", nuevo_salario)
else:
    print("\nTu nuevo salario es:", nuevo_salario)
    print("\nEl porcentaje de aumento es del ",aumento_porcentaje, "%")

print(f"\nGracias por usar este sistema {nombre}.".center(80))
print("\n")