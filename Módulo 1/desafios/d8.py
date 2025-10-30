print('<<< Desafio 008 >>>')
print('Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros')

n = int(input('Digite um valor em metros: '))

cm = n * 100
mm = n * 1000

print('| Metros | Centímetros | Milímetros |\n| {:^6} | {:^11} | {:^10} |'.format(n, cm, mm))