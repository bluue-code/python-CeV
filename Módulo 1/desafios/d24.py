print(""" <<< Desafio 024 >>>
      
      Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
      com o nome "SANTO".

""")

city = str(input('Nome da sua cidade: ')).strip()
k = city.upper().find('SANTO' or 'SANTOS')
if k == 0:
    print(f"Você cumpriou os nossos requisitos! :-)")
else:
    print(f"Vaza 0_0")