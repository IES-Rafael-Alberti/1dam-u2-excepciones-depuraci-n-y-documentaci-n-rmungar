def disminuye(num):
    if num < 0:
        raise ValueError ("El número no puede ser menor que 1")
    cadena = ""
    while num >= 0:
        if num != 0:
            cadena += str(num) + ", "
        else:
            cadena += str(num)
        num -=1
    return cadena

def main():
    try:
        num = int(input("Dame un número: "))
        print(disminuye(num))
    except ValueError as e:
        print(f"ERROR {e}")

if __name__ == "__main__":
    main()    