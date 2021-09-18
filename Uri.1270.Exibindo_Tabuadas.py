def desenho_tabuada(numero):
    for i in range(1,11):
        print(f'{numero} x {i} = {i*numero}')
    print("-" *10)

def pegar_numeros(a,b):
    numeros = []
    for x in range(a,b+1):
        numeros.append(x)
    return numeros 


n1 = int(input())
n2 = int(input())
if n2<n1:
    print('Nenhuma tabuada no intervalo!')
else:
    seguencia = pegar_numeros(n1,n2)
    n=0
    while (n < len(seguencia)):
        desenho_tabuada(seguencia[n])
        n +=1
        






