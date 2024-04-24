
MOD = 10**9+7

MEM = [1]
for x in range(499999):
    MEM.append((MEM[x]*2) % MOD)

def inversions(s):
    # total number of inversions
    total = 0
    # count zeros
    z = 0
    # count questionmarks
    q = 0

    for x in reversed(s):
        if x == '1':
            a = z * MEM[q]
            b = 0 if q == 0 else q * (MEM[q-1] % MOD)
            total = (total + a + b) % MOD
        elif x == '0':
            z += 1
        else:
            total *= 2
            a = z * MEM[q]
            b = 0 if q == 0 else q * (MEM[q-1] % MOD)
            total = (total + a + b) % MOD
            q += 1
    return total

def main():
    print(inversions(input()))

if __name__ == "__main__":
    main()

