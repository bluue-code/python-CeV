import math

print('<<< Desafio 17 >>>')
print('Faça um programa que leia o comprimento do cateto adjacente de um triângulo retângulo, '
      'calcule e mostre o comprimento da hipotenusa.')

ca = float(input('Comprimento do cateto adjacente: '))
co = float(input('Comprimento do cateto oposto: '))

hip = math.hypot(co, ca)
print('Hipotenusa: {:.2f}'.format(hip))
