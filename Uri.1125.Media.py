nota_de_trabalho = float(input())
prova = float(input())
media = (nota_de_trabalho+prova)/2
media_sub = (nota_de_trabalho + 10.00)/2
if media >=6:
    print('aprovado')
elif media_sub >=6:
    print('talvez com a sub')
else:print('reprovado')

