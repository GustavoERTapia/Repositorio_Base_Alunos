# Peça ao usuário para digitar uma letra
# se for vogal informe qual vogal
# se for consoante, verifique se é maiúscula ou minúscula

# Solicitção de entrada de dados do tipo string (texto)
letra = input("Digite uma letra: ")

if letra.lower() in "aeiou": # .lower() transforma para minúscula
    print(f"Vogal:{letra}")
else:
    if letra.isupper(): # isupper identifica se a letra está em maiúscula
        print(f"Consoante maiúscula:{letra}")
    else:
        print(f"Consoante minúscula:{letra}")