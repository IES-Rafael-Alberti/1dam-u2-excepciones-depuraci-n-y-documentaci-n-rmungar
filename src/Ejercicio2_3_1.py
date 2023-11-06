def años(edad):
    if edad < 1:
        raise ValueError("Edad no puede ser menor que 1")
    cont = 0
    cadena = "0 "
    while cont < edad:
        cont +=1
        cadena += str(cont) + " "
    return cadena

def main():
    try:
        edad = int(input("Dime tu edad: "))
        print(años(edad))
    except ValueError as e:
        print(f"ERROR {e}")
        


if __name__ == "__main__":
    main()    