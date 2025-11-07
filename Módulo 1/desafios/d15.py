dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))

pagar = (0.15 * km) + (60 * dias)

print('Valor total a pagar:R${:.2f}'.format(pagar))
