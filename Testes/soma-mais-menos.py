# quando o usuário digitar '0' o programa irá somar todos os números, positivos e negativos,
# fornecidos anteriormente
nmais = 0
nmenos = 0
num = int(input('Forneça um número: '))
while num != 0 :
    if num > 0 :
        nmais += num
    elif num < 0 :
        nmenos += num
    num = int(input('Forneça um número: '))

print(f"Soma de todos os números positivos: {nmais}")
print(f"Soma de todos os números negativos: {nmenos}")