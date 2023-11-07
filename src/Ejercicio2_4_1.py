def burbuja():
    a = [8, 3, 1, 19, 14]
    print (len(a))
    x = 0
    while a[x] != len(a):
        if a[x] > a[x+1]:
            a[x] = a[x+1]
            a[x+1] = a[x]
        x += 1
    print(a)    

def main():
    burbuja()


if __name__ == "__main__":
    main()
