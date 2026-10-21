

URL_FORM = "https://docs.google.com/forms/d/11VmcaKl2d6eWo_A5anVbkLTIn53ALj8Ak-6_9Izb858/formResponse"
nome = input("Nome: ")
ra = input("R.A: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

print("\n--- Resultado ---")
print(f"Aluno: {nome} (R.A {ra})")
print(f"Média: {media:.2f}")

if media >= 7:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")


    