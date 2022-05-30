# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
import math

print('---- Calcular Hipotenusa ----')
cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

# hipotenusa = ((cateto_oposto**2) + (cateto_adjacente**2))
hipotenusa = math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2)

print('O valor da hipotenusa do triangulo de catetos {} e {} é {}'.format(
    cateto_adjacente, cateto_oposto, math.pow(hipotenusa, 1/2)))
