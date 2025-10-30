print('<<< Digite um valor >>>')
print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.')

sal = float(input('Seu salário atual: '))

aum = (sal * 15) / 100

print('O coitado que recebe R${:.2f} agora vai passar a receber R${:.2f}'.format(sal, sal + aum))