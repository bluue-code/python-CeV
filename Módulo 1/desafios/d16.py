print('<<< Desafio 16 >>>')
print('Crie um programa que leia um número Real qualquer pelo teclado e mostre a tela a sua porção inteira.')

import math
real = float(input('Digite um número real (Como 5.43, 7.9): '))
inteiro = math.trunc(real)
print('A parte inteira de {} é {}'.format(real, inteiro))