# Faça um programa que calcule descontos de valores 

valor = float(input('Digite um valor: '))
desconto = int(input('Digite o valor do desconto: '))

desconto_aplicado = valor * (desconto/100)
novo_valor = valor - desconto_aplicado

print('O desconto aplicado de {}%, aplicado no valor de {} é {}'.format(desconto, valor, novo_valor))