# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

number = int(input('Digite um número entre 1 e 9999: '))
str_number = str(number).strip()

print('O número {} é dividido em:'.format(number))
print('Unidade: {}'.format(str_number[3]))
print('Dezena: {}'.format(str_number[2]))
print('Centena: {}'.format(str_number[1]))
print('Milhar: {}'.format(str_number[0]))
