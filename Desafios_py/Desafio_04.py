# Decodificar um dado - Desafio_04

data = input('Digite um valor: ')
print('capitalize() -> Retorna o primeiro caracter Maiusculo: {}'.format(data.capitalize()))
print('casefold() -> Retorna todos os caracteres minusculo: {}'.format(data.casefold()))
print('lower() -> Converte todos os caracteres em minúsculos: {}'.format(data.lower()))
print('count() -> Retorna a quantidade de vezes que um caracter aparece em uma string:', data.count('o'))
print('\n')
# is -----------------------------------------------------
print('O tipo primitivo desse dado é -> ', type(data))
print('Há espaços em branco: ', data.isspace())
print('Possui letras e numeros: ', data.isalnum())
print('Possui somente letras do alfabeto: ', data.isalpha())
print('O dado é somente decimal: ', data.isdecimal())
print('Todos os dados são digitos: ', data.isdigit())
print('Todos os caracteres são minúsculas: ', data.islower())
print('Todos os caracteres são números: ',data.isnumeric())
print('Todas as palavras iniciam com a letra maiuscula: ',data.istitle())
print('Todas os caracteres estão em maiusculo: ',data.isupper())
