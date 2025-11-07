import math

print('<<< Desafio 18 >>>')
print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ânulo.')

ang = int(input('Forneça um ângulo qualquer: '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Ângulo fornecido {:.0f}º\nCosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}'.format(ang, cos, sen, tan))