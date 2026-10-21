import csv
import os

MEDIA_MINIMA = 7      
MAX_ALUNOS = 300


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("  -> Este campo não pode ficar vazio.")


def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem).strip().replace(",", "."))
        except ValueError:
            print("  -> Digite um número válido (ex.: 7.5).")
            continue
        if 0 <= nota <= 10:
            return nota
        print("  -> A nota deve estar entre 0 e 10.")


def formatar(numero):
    return f"{numero:.2f}".replace(".", ",")


alunos = []
ras_cadastrados = set()

print("=== ANÁLISE DE ALUNOS ===")
print(f"Você pode cadastrar até {MAX_ALUNOS} alunos.")

while len(alunos) < MAX_ALUNOS:
    print(f"\n--- Aluno {len(alunos) + 1} de {MAX_ALUNOS} ---")
    nome = ler_texto("Nome: ")

    ra = ler_texto("R.A: ")
    while ra in ras_cadastrados:
        print("  -> Este R.A já foi cadastrado. Digite outro.")
        ra = ler_texto("R.A: ")

    nota1 = ler_nota("Nota 1: ")
    nota2 = ler_nota("Nota 2: ")

    media = (nota1 + nota2) / 2
    if media >= MEDIA_MINIMA:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"

    print("\nResultado:")
    print(f"Aluno: {nome} (R.A {ra})")
    print(f"Média: {formatar(media)}")
    print(f"Situação: {situacao}")

    alunos.append({"nome": nome, "ra": ra, "nota1": nota1,
                   "nota2": nota2, "media": media, "situacao": situacao})
    ras_cadastrados.add(ra)

    if len(alunos) == MAX_ALUNOS:
        print(f"\nLimite de {MAX_ALUNOS} alunos atingido.")
        break

    outro = input("\nCadastrar outro aluno? (s/n): ").strip().lower()
    if outro not in ("s", "sim"):
        break


total = len(alunos)
aprovados = sum(1 for a in alunos if a["situacao"] == "APROVADO")
reprovados = total - aprovados
media_turma = sum(a["media"] for a in alunos) / total

print("\n" + "=" * 60)
print(f"{'Nome':<28} {'R.A':<10} {'Média':>6}  Situação")
print("-" * 60)
for a in alunos:
    print(f"{a['nome'][:28]:<28} {a['ra']:<10} {formatar(a['media']):>6}  {a['situacao']}")
print("=" * 60)
print(f"Total de alunos: {total}")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")
print(f"Média da turma: {formatar(media_turma)}")


pasta = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(pasta, "resultado_alunos.csv")
with open(caminho, "w", newline="", encoding="utf-8-sig") as arquivo:
    escritor = csv.writer(arquivo, delimiter=";")
    escritor.writerow(["Nome", "R.A", "Nota 1", "Nota 2", "Média", "Situação"])
    for a in alunos:
        escritor.writerow([a["nome"], a["ra"], formatar(a["nota1"]),
                           formatar(a["nota2"]), formatar(a["media"]), a["situacao"]])
print(f"\nResultados salvos em: {caminho}")
    