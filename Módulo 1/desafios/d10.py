print('<<< Desafio 10 >>>')
print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.')
#dolar atual = $5.38

real = float(input('Valor para conversão: '))
dolar = real / 5.38
euro = real / 6.19
kwanza_angolano = real / 0.0059
libra = real / 7.03
rublo_russo = real / 0.067
ien = real / 0.035
print('O valor de R${:.2f} convertido para a cotação atual do dólar de R$5,38 é igual a US${:.2f}'.format(real, dolar))
print('O valor de R${:.2f} convertido para a cotação atual do euro de R$6,19 é igual a €${:.2f}'.format(real, euro))
print('O valor de R${:.2f} convertido para a cotação atual do Kwanza Angolano de R$0.0059 é igual a Kz${:.2f}'.format(real, kwanza_angolano))
print('O valor de R${:.2f} convertido para a cotação atual da Libra de R$7,03 é igual a £${:.2f}'.format(real, libra))
print('O valor de R${:.2f} convertido para a cotação atual do Rublo Russo de R$0,067 é igual a 	₽${:.2f}'.format(real, rublo_russo))
print('O valor de R${:.2f} convertido para a cotação atual do Ien de R$0,035 é igual a JP¥{:.2f}'.format(real, ien))

print('<<< Data do dia em que pesquisei a cotação de cada moeda: 04/11/2025 >>>')
