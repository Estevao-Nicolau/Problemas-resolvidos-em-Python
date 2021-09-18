def primo(n):
    for i in range(0,n):
        num = int(input())
        s = 0
        j=1
        while j <= num:
            if num % j == 0:
                s = s + 1
            j = j + 1
        if s > 2:
            num.append(n_primo)
        else:
            num.append(eh_primo)
            
n = int(input())
n_primo = []
eh_primo = []

print(n_primo)
print(eh_primo)

