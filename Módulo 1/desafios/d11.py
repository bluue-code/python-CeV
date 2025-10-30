print('<<< Desafio 011 >>>')
print('Faça um programa que leia a largura e a altura de uma parede em metros, '
      'calcule a sua área e a quantidade de tinta necessária para pintá-la, '
      'sabendo que cada litro de tinta, pinta uma área de 2m^2')

altura = float(input('Valor da altura: '))
largura = float(input('Valor da largura: '))

area = altura * largura
tinta = area / 2

print('Uma parede de {}m^2 gasta {} litros de tinta.'.format(area, tinta))

