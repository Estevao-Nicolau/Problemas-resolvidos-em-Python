preco = float(input())
qtd = int(input())
valor_total = preco * qtd
desconto = valor_total*(10 + qtd) /100
valor_final = valor_total - desconto
print(f'{valor_total:.2f}')
print(f'{valor_final:.2f}')
