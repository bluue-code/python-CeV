print(""" <<< Desafio 23 >>>
      Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
      
      ex: Digite um número: 1834
            unidade: 4
            dezena: 3
            centena: 8
            milhar: 1

""")

num = int(input("Digite um número qualquer menor que 9999: "))

print(f"Unidade: {num % 10}")
print(f"Dezena: {num // 10 % 10}")
print(f"Centena: {num // 100 % 100}")
print(f"Milhar: {num // 1000 % 1000}")


