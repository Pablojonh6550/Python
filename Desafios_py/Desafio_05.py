# Faça um programa que leia um número inteiro e mostre seu sucessor e antecessor respesctivamente.
number = int(input('Digite um número: '))

antecessor = number - 1
sucessor = number + 1

print('O valor que antecede o número {} é {} e seu sucessor é {}'.format(number, antecessor, sucessor))
