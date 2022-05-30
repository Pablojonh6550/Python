# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
number = float(input('Digite um número decimal: '))

# Formatação - Jonh 
print('A porção inteira {} do número é {:.0f}'.format(number, number))

# Formatação - Guanabara
print('A porção inteira {} do número é {}'.format(number, trunc(number)))
