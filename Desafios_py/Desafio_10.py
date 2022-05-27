# Faça um conversor de moedas 

valor = float(input('Digite o valor que você possui: '))

dolar = valor / 4.72
dolar_c = valor / 3.71
iene = valor / 0.037

print('O que você pode comprar em: ')
print('Dolar: {:.2f}'.format(dolar))
print('Dolar Canadense: {:.2f}'.format(dolar))
print('Iene: {:.2f}'.format(iene))