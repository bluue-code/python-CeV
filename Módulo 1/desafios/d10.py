print('<<< Desafio 10 >>>')
print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.')
#dolar atual = $5.38

real = float(input('Valor para trocar para dolar: '))
dolar = real / 5.38

print('O valor de R${:.2f} convertido para a cotação atual do dólar de R$5,38 é igual a US${:.2f}'.format(real, dolar))
