def impares(num):
    if num<1:
        raise ValueError("El número no puede ser menor que 1")
    cont = 1
    cadena = "1, "
    if num == 1 or num == 2:
        return "1"
    while cont < num-1:
        cont +=2
        if cont < num-1:
            cadena += str(cont) + ", "
        elif cont == num-1:
            cadena += str(cont) + ""
        else: 
            cadena += str(cont) + ""
    return cadena

def main():
    try:
        num = int(input("Dime un número: "))
        print(impares(num))
    except ValueError as e:
        print(f"ERROR {e}")

if __name__ == "__main__":
    main()    