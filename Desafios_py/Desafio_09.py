# Faça um programa que retorne a tabuada de um número.

number = int(input('Digite um número inteiro: '))
value = range(1, 11)

print('A tabuada de {}'.format(number))

# Com FOR
print('Multiplicação\n--------------------')
for i in value:
    print('{} x {} = {}'.format(number, i, number*i))

print('Divisão\n--------------------')
for i in value:
    print('{} / {} = {}'.format(number*i, number, i))

# Com WHILE
print('\n')
i = 1
print('Multiplicação com while\n--------------------')
while (i < 10):
    i = i+1
    print('{} x {} = {}'.format(number, i, number*i))

print('Divisão\n--------------------')


