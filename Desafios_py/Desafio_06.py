# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

number = int(input('Digite um número inteiro: '))

dobro = number * 2
triplo = number * 3
raiz = pow(number, 0.5)

print('O dobro do número é: {}'.format(dobro))
print('O triplo do número é: {}'.format(triplo))
print('A raiz do número é: {}'.format(raiz))

