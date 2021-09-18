i = int(input())
f = int(input())
primo = 0

for p in range(i, f+1):
    divisores = 0
    for a in range(1, p+1):
        if p % a == 0:
            divisores += 1
    if divisores == 2:
        print(p)
        primo +=1

print(f'primos: {primo}')
