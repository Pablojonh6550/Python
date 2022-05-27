# Faça um programa que receba o salário de um funcionário e retorne o salário com um aumento ou redução de % definido
# pelo usuario

salario = float(input('Digite o valor do salario R$'))

opc = int(input('1 - Aumento \n2 - Redução\n'))

if (opc == 1):
    data = int(input('Digite quantos {} será acrescentado'.format('%')))
    resultado = salario * (data/100)
    novo_salario = salario + resultado
    
    print('O salário de {} com o aumento de {} será {}'.format(salario, data, novo_salario))
else:
    data = int(input('Digite quantos {} será acrescentado'.format('%')))
    resultado = salario * (data/100)
    novo_salario = salario - resultado
    
    print('O salário de {} com o aumento de {} será {}'.format(salario, data, novo_salario))

