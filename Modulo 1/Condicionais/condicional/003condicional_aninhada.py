#3. Classificação por idade
# Faça um programa que leia a idade de uma pessoa e classifique-a em:
# criança : menor que 12 anos
# adolescente: entre 12 e 17 anos
# adulto: maior ou igual a 18 anos
# Utilize a estrutura de condicional aninhada

idade = int(input("Digite a idade: "))

if idade < 18:
    if idade < 12:
        print("Classificação: Criança.")
    else:
        print("Classificação: Adolescente.")
else:
    print("Classificação: Adulto.")