print(""" <<< Desafio 027 >>>
    Faça um programa que leia o nome completo de uma pessoa, mostrando em 
    seguida o primeiro e o último nome separadamente.
      
      ex: Ana Maria de Souza
      primeiro = Ana
      último = Souza
""")

nome = str(input('Seu nome: ')).strip().title()
n = nome.split()
print(f"Prazer em te conhecer ^^)\n")
print(f"Primeiro nome: {n[0]}")
print(f"Último nome: {n[-1]}") # ou nome[len(nome) - 1]