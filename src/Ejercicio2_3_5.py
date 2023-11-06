contraseña_guardada = "rmungar1209"
try:
    contraseña_introducida = input("Ingrese la contraseña: ")
    if contraseña_guardada != contraseña_introducida:
        raise ValueError("Incorrect Password!!")
    print("WELCOME!!")
except ValueError as e:
    print(e)
