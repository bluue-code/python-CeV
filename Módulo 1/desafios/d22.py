print(""" <<< Desafio 022 >>>
      Crie um programa que leia o nome completo de uma pessoa a mostra:
      . O nome com todas as letras maiúsculas;
      . O nome com todas minúsculos;
      . Quantas letras ao todo (sem considerar espaços);
      . Quantas letras tem o primeiro nome.
""")
nome = str(input("Nome completo para analise: ")).strip()
M = nome.upper()
print(f"--> {M}")
m = nome.lower()
print(f'--> {m}')
n = len(nome) - nome.count(' ') #o número de letras menos a quantidade de espaços
print(f'Contagem de letras: {n}')
g = nome.split()
p = len(g[0]) # ou nome.find(' ')
print(f'Quantidade de letras do seu primeiro nome: {p}')