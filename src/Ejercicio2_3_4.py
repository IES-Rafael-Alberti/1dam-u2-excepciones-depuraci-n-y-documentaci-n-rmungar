try:
    num=int(input("Dame un número: "))
    print(num+1)
except ValueError as e:
    print(f"ERROR {e}")