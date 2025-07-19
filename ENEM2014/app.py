from funcionalidades import *
from utils import *
import os


def main():

    escolas = carregar_arquivo("nota_por_escola.txt")
    limpar_tela()

    while True:
        show_menu()
        opcao = inteiro_positivo("Digite o número da opção desejada: ")
        limpar_tela()

        if opcao == 0:
            print("\nEncerrando o sistema. Obrigado por utilizar o SYS ESCOLAS.\n")
            break

        elif opcao == 1:
            print("\n========== TOP N ESCOLAS DO BRASIL (TODAS AS ÁREAS) ==========\n")
            pos = inteiro_positivo("Informe a quantidade de posições: ")
            n_todas_as_areas(escolas, "media_objetivas", "redacao", pos)

        elif opcao == 2:
            print("\n========== TOP N ESCOLAS DO BRASIL POR ÁREA ==========\n")
            resultado = opcoes_menu_dois()
            n = inteiro_positivo("Informe a quantidade de posições: ")
            if resultado:
                area = resultado
                top_n_escolas(escolas, area, n)

        elif opcao == 3:
            while True:
                print("\n========== TOP N ESCOLAS POR ESTADO ==========\n")
                uf = input("Sigla do estado (UF): ").strip().upper()

                uf_existe = False
                for escola in escolas:
                    if escola["uf"] == uf:
                        uf_existe = True
                        break

                if not uf_existe:
                    print(f"A UF '{uf}' não foi encontrada.\n")
                    continue

                resultado = opcoes_menu_dois()
                if resultado:
                    area = resultado
                    n = inteiro_positivo("Informe a quantidade de posições: ")
                    ordenar_estado_por_nota(escolas, area, uf, n)
                break

        elif opcao == 4:
            while True:
                print("\n========== TOP N ESCOLAS POR ESTADO E REDE ==========\n")
                uf = input("Sigla do estado (UF): ").strip().upper()
                rede = (
                    input("Tipo de rede (Federal, Estadual ou Privada): ")
                    .strip()
                    .capitalize()
                )

                estado_rede = filtrar(
                    escolas,
                    lambda escola: escola["uf"] == uf and escola["rede"] == rede,
                )

                if estado_rede:
                    listar_dados(estado_rede)
                    break
                else:
                    print(
                        "Nenhuma escola encontrada com esses critérios. Tente novamente.\n"
                    )

        elif opcao == 5:
            print("\n========== MÉDIA NACIONAL POR ÁREA DO CONHECIMENTO ==========\n")
            resultado = opcoes_menu_dois()
            if resultado:
                area = resultado
                media = media_por_area(escolas, area)
                print(f"Média nacional na área de {area}: {media:.2f}")

        elif opcao == 6:
            print("\n========== MELHOR ESCOLA POR ÁREA E ESTADO ==========\n")
            resultado = opcoes_menu_dois()
            estado = input("Sigla do estado (UF): ").strip().upper()
            
            uf_existe = False
            for escola in escolas:
                if escola["uf"] == estado:
                    uf_existe = True
                    break

            if not uf_existe:
                print(f"A UF '{estado}' não foi encontrada.\n")
                continue

            if resultado:
                area = resultado
                melhor_escola(escolas, area, estado)

        elif opcao == 7:
            print("\n========== ESCOLAS POR ESTADO (ORDENADAS POR RENDA) ==========\n")
            estado = input("Sigla do estado (UF): ").strip().upper()

            uf_existe = False
            for escola in escolas:
                if escola["uf"] == estado:
                    uf_existe = True
                    break

            if not uf_existe:
                print(f"A UF '{estado}' não foi encontrada.\n")
                continue

            ordenar_por_renda_estado(escolas, estado)

        elif opcao == 8:
            print("\n========== BUSCAR ESCOLA PELO NOME ==========\n")
            nome = input("Nome da Escola: ").strip().upper()
            nome_existe = False
            for escola in escolas:
                if escola["nome"] == nome:
                    nome_existe = True
                    break
 
            if not nome_existe:
                print(f"A escola '{nome}' não foi encontrada.\n")
                continue

            escola_por_nome = filtrar(
            escolas, lambda escola: escola["nome"] == nome )
            listar_dados(escola_por_nome)


        elif opcao == 9:
            print("\n========== ESTADO COM MAIOR MÉDIA POR ÁREA ==========\n")
            resultado = opcoes_menu_dois()
            if resultado:
                area = resultado
                estado, media = estado_com_maior_media(escolas, area)
                print(
                    f"O estado com maior média em {area} é {estado}, com média {media:.2f}"
                )

        elif opcao == 10:
            print(
                "\n========== ESCOLAS COM MÉDIA POR ÁREA ACIMA DE UM VALOR ==========\n"
            )
            resultado = opcoes_menu_dois()
            if resultado:
                area = resultado
                valor = inteiro_min_max("Informe o valor mínimo da média: ", 1, 1000)
                media_maior_que(escolas, valor, area)

        elif opcao == 11:
            print("\n========== MAIOR NOTA POR NÍVEL SOCIOECONÔMICO ==========\n")
            resultado = opcoes_menu_dois()
            if resultado:
                area = resultado
                escola_nivel = escola_com_maior_nota_nivel(escolas, area)
                for item in escola_nivel:
                    print(
                        f"Nível: {item['nivel_socio_economico']} | Escola: {item['escola']} | Nota: {item['nota']}"
                    )

        elif opcao == 12:
            print("\n========== ESCOLAS QUE INICIAM COM UMA LETRA ==========\n")
            caracter = input("Informe a letra de início do nome: ").strip().upper()
            contem_caracter(escolas, caracter)

        else:
            print("Opção inválida. Por favor, escolha uma das opções disponíveis.")

        input("\nPressione ENTER para continuar...")
        limpar_tela()


def show_menu():
    menu = """
===================== MENU PRINCIPAL – SYS ESCOLAS =====================

 1 - Top N Escolas do Brasil (todas as áreas)
 2 - Top N Escolas por Área do Conhecimento
 3 - Top N Escolas por Estado (todas as áreas)
 4 - Top N Escolas por Estado e Tipo de Rede
 5 - Média Nacional por Área do Conhecimento
 6 - Melhor Escola por Área e Estado
 7 - Lista de Escolas por Estado (ordenadas por Renda)
 8 - Buscar Escola pelo Nome(completo)
 9 - Estado com Maior Média por Área
10 - Escolas com Média por Área acima de um Valor
11 - Escolas com Maior Nota por Nível
12 - Listar Escolas que Iniciam com uma Letra

 0 - Sair

=======================================================================
"""
    print(menu)


def menu_opcao2():
    menu_dois = """
======================= ÁREAS DO CONHECIMENTO =======================

 1 - Linguagens
 2 - Matemática
 3 - Ciências da Natureza
 4 - Ciências Humanas
 5 - Redação
 6 - Voltar

======================================================================
"""
    print(menu_dois)


def opcoes_menu_dois():
    while True:
        menu_opcao2()
        opcao_dois = inteiro_positivo("Escolha uma das áreas (1 a 6): ")
        limpar_tela()
        area = None

        if opcao_dois == 1:
            area = "linguagens"
        elif opcao_dois == 2:
            area = "matematica"
        elif opcao_dois == 3:
            area = "ciencias_natureza"
        elif opcao_dois == 4:
            area = "humanas"
        elif opcao_dois == 5:
            area = "redacao"
        elif opcao_dois == 6:
            break
        else:
            print("Opção inválida. Tente novamente.")

        if area:
            return area


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


main()
