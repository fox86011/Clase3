print("Bienvenido a Facebook ")
print("Creacion de cuenta")
usuario=input("Crea un nombre de usuario: ")
contraseña=input("Crea una contraseña: ")
print("Ingrese a Facebook")
usua=input("Ingrese su usuario: ")
contra=input("Ingrese su contraseña: ")

if usua==usuario and contra == contraseña:
    print(f"Bienvenido al Metaverso {usuario} ")
elif usua!=usuario and contra != contraseña:
    print("Usuario o contraseña incorrecta")
elif usua==usuario and contra != contraseña:
    print("Usuario o contraseña incorrecta")
elif usua!=usuario and contra == contraseña:
    print("Usuario o contraseña incorrecta")

    