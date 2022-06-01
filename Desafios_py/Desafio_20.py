# Faça um programa onde leia o nome de quatro alunos e mostre a ordem sorteada

import random

nomes = []

while True:
    nome = str(input('Digite o nome do aluno: '))
    nomes.append(nome)
    aux = str(input('Deseja continuar? S ou N: ')).upper()
    if(aux == 'N'):
        random.shuffle(nomes)
        print('A ordem de embaralhada é {}'.format(nomes))
        break
