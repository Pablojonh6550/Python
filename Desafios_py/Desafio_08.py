# Faça um conversor de medidas, onde receberá o valor em metros e o converterá em centimetros e milimetros.

data = float(input('Digite um valor em metros: '))

cm = data * 100
mm = data * 1000
km = data / 1000

print('A medida em cm é: {:.0f}'.format(cm))
print('A medida em mm é: {:.0f}'.format(mm))
print('A medida em km é: {:.3f}'.format(km))
