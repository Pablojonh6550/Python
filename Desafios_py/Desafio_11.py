# Faça um programa que leia a altura e largura de uma parede em metros e retorne a área e a quantidade de tinta
# necessaria para pinta-lá.

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
tinta = area / 2

print('A área da parede é: {:.2f}m²'.format(area))
print('A quantidade de tinta necessaria é: {}l'.format(tinta))
