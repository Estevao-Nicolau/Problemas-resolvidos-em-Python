n = int(input())    

originais =[]
for _ in range(n):
    originais.append(float(input()))

novas = []
for _ in range(n):
    novas.append(float(input()))

finais = []
qtd_alteradas = 0

for i in range(n):
    if novas[i] == 10 and originais[i] < 10:
        final = originais[i] + 2
        if final > 10:
            final = 10
        finais.append(final)
        qtd_alteradas += 1
    else:
        finais.append(originais[i])
        
print(f'NOTAS ALTERADAS: {qtd_alteradas}')

for i in range(n):
    if originais[i] != finais[i]:
        print(f'*({i+1:03}) original: {originais[i]:05.2f} | final: {finais[i]:05.2f}')
    else:
        print(f'-({i+1:03}) original: {originais[i]:05.2f} | final: {finais[i]:05.2f}')
