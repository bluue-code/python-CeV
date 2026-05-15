print(""" <<< Desafio 026 >>>
      Faça um programa que leia uma frase pelo teclado e mostre:
      > Quantas vezes aparece a letra "A".
      > Em que posição ela aparece a primeira vez.
      > Em que posição ela aparece a última vez.

""")

frase = str(input("Uma frase: ")).strip().lower()
print(f"Quantas vezes aparece a letra 'a'? {frase.count('a')} vezes")
print(f"Em que posição ela aparece pela primeira vez? {frase.find('a') + 1}º")
print(f"A última posição onde 'a' foi encontrado? {frase.rfind('a') + 1}º")