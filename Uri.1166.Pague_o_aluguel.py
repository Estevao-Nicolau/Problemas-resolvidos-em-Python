div = int(input())
pag = int(input())
pgto = 1
while div > 0:
    if div <= pag:
        print(f'pagamento: {pgto}')
        pgto += 1
        print(f'antes = {div}')
        div = 0
        print(f'depois = {div}')
        print('-----')
    else:
        print(f'pagamento: {pgto}')
        pgto += 1
        print(f'antes = {div:.0f}')
        div = div - pag
        print(f'depois = {div:.0f}')
        print('-----')
    
    
    
