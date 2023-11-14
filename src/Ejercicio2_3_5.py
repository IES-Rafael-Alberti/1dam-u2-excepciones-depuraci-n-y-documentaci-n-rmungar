contraseña_guardada = "rmungar1209"
try:
    contraseña_introducida = input("Ingrese la contraseña: ")
    if contraseña_guardada != contraseña_introducida:
        raise NameError("Incorrect Password!!")
    print("WELCOME!!")
except NameError as e:
    print(e)
