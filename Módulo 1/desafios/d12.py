print('<<< Desafio 12 >>>')
print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')

preco = float(input('Valor do produto:R$ '))

des = (preco * 5) / 100
print('Parabéns você recebeu um desconto de 5%!!\nAgora o produto vale R${:.2f}'.format(preco - des))
