print('<<< Desafio 19 >>>')
print('Um professor quer sortar um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, '
      'lendo o nome deles e escrevendo o nome do escolhido.')
import random

alun1 = input('Qual o nome do primeiro aluno? ')
alun2 = input('Qual o nome do segundo aluno? ')
alun3 = input('Qual o nome do terceiro aluno? ')
alun4 = input('Qual o nome do quarto aluno? ')

lista = [alun1, alun2, alun3, alun4]
escolhido = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))