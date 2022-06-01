# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, 
# lendo o nome deles e escrevendo o nome do escolhido.

import random
alunos = []

while True:
    nome = str(input("Digite o nome do aluno: ")) 
    alunos.append(nome)
    aux = str(input('Deseja continuar S ou N?')).upper()
    if(aux == 'N'):
        aux1 = random.choice(alunos)
        print('O aluno sorteado foi {}'.format(aux1))   
        break