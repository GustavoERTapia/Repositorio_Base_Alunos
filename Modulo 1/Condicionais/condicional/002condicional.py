# Crie im código que receba 3 notas, calcule a média
# e informe se o aluno está, aprovado , em recuperação
# ou reprovado

# OBS: Aprovad média>=7
# Recuperção média >4
# Reprovado média <4

# Etapas
# 1) solicitar as notas ao usuário
# 2) calcular a média
# 3) checar a condição do aluno
# 4) informar o resultado

nota1 = float(input("Digite a Primeira nota: "))
nota2 = float(input("Digite a Segunda nota:"))
nota3 = float(input("Digite a Terceira nota: "))
média = (nota1 + nota2 +nota3)/3
if média>=7:
    print(f"O aluno tem média {média:.2} e está aprovado.")
elif média > 4:
    print(f"O aluno teve média {média:.2} e está em recuperação.")
    print(f"O aluno teve média {média:.2} e está em recuperação.")
else:
    print(f"O aluno teve média  {média:.2} e está reprovado.")