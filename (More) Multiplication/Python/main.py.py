import sys

def multiplication(A, B):

    if A == 0 or B == 0:
        return
    
    R = A*B
    As = str(A)
    Bs = str(B)
    Rs = str(R)
    c = 0
    Alen =(len(As))
    Blen=(len(Bs))
    Rlen = (len(Rs))
    if Alen > Blen:
        carry = Rlen-Alen
    else:
        carry = Rlen-Blen
    arr = []

    for i in range(Blen):
        a = []
        for j in range(Alen):
            a.append(int(Bs[i]) * int(As[j]))
        arr.append(a)

    # Lína 1
    print("+", end="")
    print("---",end="")
    for j in range(Alen):
        print("----", end="")
    print("+")

    #Lína 2
    print("|", end="")
    for j in range(Alen):
        print(f'   {As[j]}', end="")
    print("   |")

    # Miðja
    for i in range(Blen):

        print("| ", end="")
        for j in range(Alen):
            print("+---", end="")
        print("+ |")

        if carry-Blen+i > 0:
            print("|/", end="")
        else:
            print("| ",end="")

        for j in range(Alen):
            value = str(arr[i][j])
            if len(value) < 2:
                num = 0
            else:
                num = value[0]
            print(f"|{num} /", end="")
        print("| |")

        print("| ", end="")
        for j in range(Alen):
            print("| / ", end="")
        print(f"|{Bs[i]}|")

        if Rlen > Alen+Blen-1-i:
            print(f"|{Rs[c]}", end="")
            c += 1
        else:
            print("| ", end="")

        for j in range(Alen):
            value = str(arr[i][j])
            if len(value) < 2:
                num = value[0]
            else:
                num = value[1]
            print(f"|/ {num}", end="")
        print("| |")

    print("| ", end="")
    for j in range(Alen):
        print("+---", end="")
    print("+ |")

    print("|", end="")
    for k in range(Alen):
        if k == 0:
            if Rlen > Alen:
                print(f"/ {Rs[c]}", end="")
            else:
                print(f"  {Rs[c]}", end="")
        else:
                    print(f" / {Rs[k+c]}", end="")
    print("    |")

    print("+", end="")
    print("---",end="")
    for j in range(Alen):
        print("----", end="")
    print("+")
 
for line in sys.stdin:
    a, b = map(int, line.strip().split())
    multiplication(a,b)