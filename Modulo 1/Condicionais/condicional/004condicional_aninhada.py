# Tipo de triangulo
# Crie um programa que receba tres lados de um triangulo
# verifique se os lados realmente podem formar um triangulo
# e determine o triangulos em:
# Equilatro (Todos os lados são iguais)
# Isóceles (dois lados iguais)
# Escaleno (todos os lados diferentes)

lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1 :
    if lado1 == lado2:
        if lado2 == lado3:
            print(f"Os lados do Triangulo são {lado1}, {lado2}, {lado3}: Triangulo Equilátero.")
        else:
            print(f"Os lados do Triangulo são {lado1}, {lado2}, {lado3}: Triangulo isóceles.")
else: # não é possivel formar um triangulo
    if lado2 == lado3 or lado1 == lado3:
        print(f"Os lados do Triangulo são {lado1}, {lado2}, {lado3}: Triangulo isóceles.")
    else:
        print(f"Os lados do Triangulo são {lado1}, {lado2}, {lado3}: Triangulo Escaleno.")
