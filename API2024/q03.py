def main():

    qtd_alunos = 0
    qtd_mulher = 0
    qtd_homem = 0
    somatorio = 0
    somatorio_m = 0
    somatorio_h = 0
    menor_nota = 11
    maior_nota = -1

    while True:
        show_menu()
        opcao = str(input("Digite uma opção: "))

        if opcao != "H" and opcao != "M":
            break

        nota = obter_nota("Digite sua nota: ")
        somatorio += nota
        qtd_alunos += 1

        if nota < menor_nota:
            menor_nota = nota
        if nota > maior_nota:
            maior_nota = nota

        if opcao == "M":
            qtd_mulher += 1
            somatorio_m += nota

        if opcao == "H":
            qtd_homem += 1
            somatorio_h += nota

    if qtd_alunos > 0:
        media_geral = somatorio / qtd_alunos
        situacao = calcular_situacao(media_geral)
        resultado = f'''
        ===== RESULTADO FINAL =====
        Total de alunos: {qtd_alunos}
        Homens: {qtd_homem} | Mulheres: {qtd_mulher}
        Média geral: {media_geral:.2f}
        Situação geral: {situacao}
        Maior nota: {maior_nota}
        Menor nota: {menor_nota}
        '''
        print(resultado)
        if qtd_homem > 0:
            media_homens = somatorio_h / qtd_homem
            performance_h = (somatorio_h / (qtd_homem * 10)) * 100
            print(f"\nHomens:")
            print(f"  Média: {media_homens:.2f} ({calcular_situacao(media_homens)})")
            print(f"  Performance: {performance_h:.1f}%")

        if qtd_mulher > 0:
            media_mulheres = somatorio_m / qtd_mulher
            performance_m = (somatorio_m / (qtd_mulher * 10)) * 100
            print(f"\nMulheres:")
            print(
                f"  Média: {media_mulheres:.2f} ({calcular_situacao(media_mulheres)})"
            )
            print(f"  Performance: {performance_m:.1f}%")
    else:
        print("Nenhum dado registrado.")


def calcular_situacao(media):

    if media < 2:
        return "Pessimo"
    elif media < 4:
        return "Ruim"
    elif media < 7:
        return "Regular"
    elif media < 8:
        return "Bom"
    elif media >= 8:
        return "Excelente"


def obter_nota(label: str):
    entrada = input(label)

    try:
        numero = float(entrada)
        if numero < 0 or numero > 10:
            print("A nota deve estar entre 0 e 10")
            return obter_nota(label)
        return numero
    except ValueError:
        print("Digite um valor válido")
        return obter_nota(label)


def show_menu():
    menu = """
======= NOTA =======
M - Mulher
H - Homem
....
0 - Sair
"""
    print(menu)


main()
