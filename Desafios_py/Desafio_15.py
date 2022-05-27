#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.

dia = int(input('Quantidades de dias que você passou com o carro: '))
km = float(input('Quantidade de KM rodados: '))

valor_total = (dia * 60) + (km * 0.15)

print('O valor total a pagar pelo aluguel do carro é: {:.2f}'.format(valor_total))