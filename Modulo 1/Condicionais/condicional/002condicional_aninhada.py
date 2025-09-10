# 2. Paridade e tamanho do número

# crie um código que receba um número inteiro e informe:
# - se é par ou ímpar
# - e, ao mesmo tempo, se é maior que 10 ou menor ou igual a 10
# Utilize  condicionais aninhadas para organizar as verificações

numero = int(input("Digite o número iteiro: "))

if numero % 2 == 0 :
    if numero >=10 :
        print(f"O número {numero} é par e maior que 10.")
    else:
        print(f"O número {numero} é par e menor que 10.")
else:
    if numero >= 10:
        print(f"o número {numero} é impar e maior que 10.")
    else:
        print(f"o número {numero} é impar e menor que 10.")