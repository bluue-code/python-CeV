print('<<< Desafio 008 >>>')
print('Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros')

n = float(input('Digite um valor em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000

print('| Quilômetros | Hectometros | Descâmetros | Metros | Decímetros | Centímetros | Milímetros |\n'
      '| {:^11} | {:^11} | {:^11} | {:^6} | {:^10} | {:^11} | {:^10} |'.format(km, hm, dam, n, dm, cm, mm))