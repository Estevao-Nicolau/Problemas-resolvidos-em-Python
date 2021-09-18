def premium(tabela):
    for canal in tabela:           
        bonus = canal[2] + (canal[1]//1000)*premi
        sbonus = canal[2] + (canal[1]//1000)*npremi           
        if canal[3] == True:
            print(f'{canal[0]}: R$ {bonus:.2f}')
        else:               
            print(f'{canal[0]}: R$ {sbonus:.2f}')
                
            
def preenche_tabela(qtd_canais):
    tabela = []
    for i in range(qtd_canais):
        canal = input().split(';')
        canal[1] = int(canal[1])
        canal[2] = float(canal[2])
        canal[3] = canal[3] == 'sim'
        tabela.append(canal)
    return tabela

n = int(input())
tabela = preenche_tabela(n)
premi = float(input())
npremi= float(input())
print('-----' '\nBÔNUS' '\n-----')
premium(tabela)
