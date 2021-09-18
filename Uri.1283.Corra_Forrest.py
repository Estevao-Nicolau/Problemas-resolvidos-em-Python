num = cont = soma = media = 0
num = int(input())
lista_numero = []
while num >=0:
    soma += num
    lista_numero.append(num)
    cont += 1    
    num = int(input())
media = soma / cont


print(f'MEDIA: {media:.2f}')
for num in lista_numero:
    if num < media:
        print(num)
         