import os
from vetor_funcionalidades import *
from utils import *


def main():

    limpar_tela()
    inicializar()
    limpar_tela()

    while True:
        inicio = f"""
    ==============INICIALIZAR VETOR==============
    1 - VETOR COM DADOS AUTOMÁTICOS
    2 - VETOR COM DADOS MANUAIS
    3 - VETOR COM VALORES DE UM ARQUIVO
    =============================================
    """
        print(inicio)
        opcao = inteiro_positivo("Escolha uma opção: ")
        limpar_tela()
        if opcao == 1:
            vetor = gerar_aleatorio()
            print("Vetor carregado com sucesso!!")
            limpar_tela()
            break
        elif opcao == 2:
            vetor = gerar_manual()
            print("Vetor carregado com sucesso!!")
            limpar_tela()
            break
        elif opcao == 3:
            vetor = carregar_valores()
            print("Vetor carregado com sucesso!!")
            limpar_tela()
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")

    while True:

        menu_principal()
        opcao = opcoes_menu_principal()
        limpar_tela()

        if opcao == 1:
            mostrar_valores(vetor)

        elif opcao == 2:
            valor_padrao = obter_float("Resetar valores com o número: ")
            resetar(vetor, valor_padrao)

        elif opcao == 3:
            qtd = qtd_items(vetor)
            print(f"Quantidade de itens no vetor: {qtd}")

        elif opcao == 4:
            if not vetor:
                print("Vetor vazio.")
            else:
                maior, pos_maior = maior_valor(vetor)
                menor, pos_menor = menor_valor(vetor)
                print(f"Maior valor: {maior}, Posição: {pos_maior}")
                print(f"Menor valor: {menor}, Posição: {pos_menor}")

        elif opcao == 5:
            resultado_sum = somatorio(vetor)
            print(f"O Somatório dos valores: {resultado_sum}")

        elif opcao == 6:
            media_vetor = media(vetor)
            print(f"Média dos valores: {media_vetor}")

        elif opcao == 7:
            postivos, qtd_positivos = valores_positivos(vetor)
            if qtd_positivos == 0:
                print("O vetor não possui números negativos.")
            else:
                print(f"Valores positivos: {postivos} \nQuantidade: {qtd_positivos}")

        elif opcao == 8:
            negativos, qtd_negativos = valores_negativos(vetor)
            if qtd_negativos == 0:
                print("O vetor não possui números negativos.")
            else:
                print(f"Valores negativos: {negativos} \nQuantidade: {qtd_negativos}")

        elif opcao == 9:
            vetor = opcoes_menu_secundario(vetor)

        elif opcao == 10:
            vetor = adicionar_valores(vetor)

        elif opcao == 11:
            vetor = remover_por_valor_exato(vetor)

        elif opcao == 12:
            vetor = remover_por_posicao(vetor)

        elif opcao == 13:
            vetor = edita_valor(vetor)

        elif opcao == 14:
            nome_arquivo = input("Nome do arquivo para salvar: ")
            salvar_valores(vetor, nome_arquivo)

        elif opcao == 15:
            limpar_tela()
            print("=" * 40)
            print("   Obrigado por usar o PlayNumbers!")
            print("         Volte sempre :)")
            print("=" * 40)
            break

        input("Pressione ENTER para continuar...")
        limpar_tela()


def inicializar():
    print(
        """
=======================================
    Bem-vindo ao PlayNumbers!
  Seu gerenciador de vetores favorito
=======================================
"""
    )
    input("Pressione ENTER para começar...")


def menu_principal():
    menu = f"""
    =========MENU-PLAYNUMBERS========
    
    1-  MOSTRAR TODOS OS VALORES
    2-  RESETAR VETOR
    3-  QUANTIDADE DE ITENS NO VETOR
    4-  MAIOR E MENOR VETOR
    5-  SOMATÓRIO
    6-  MÉDIA
    7-  POSITVOS E QUANTIDADES
    8-  NEGATIVOS E QUANTIDADES
    9-  ATUALIZAR VALORES POR REGRA
    10- ADCIONAR NOVOS VALORES
    11- REMOVER ITENS POR VALOR EXATO
    12- REMOVER ITENS POR POSIÇÃO
    13- EDITAR VALOR ESPECIFICO POR POSIÇÃO
    14- SALVAR VALORES EM ARQUIVO
    15- SAIR
    
    """
    print(menu)


def menu_secundario():
    secundario = """
    1 - MULTIPLICAR POR UM VALOR
    2 - ELEVAR A UM VALOR
    3 - REDUZIR A UMA FRAÇÃO
    4 - TROCAR VALORES NEGATIVOS POR UM NÚMERO ALEATÓRIO DA FAIXA 
    5 - ORDENAR VALORES 
    6 - EMBARALHAR VALORES
    7 - VOLTAR AO MENU PRINCIPAL
    """
    print(secundario)


def opcoes_menu_secundario(vetor):
    while True:
        menu_secundario()
        opcao_secundaria = inteiro_positivo("Escolha uma opção: ")
        limpar_tela()

        if opcao_secundaria == 1:
            valor = obter_float("Multiplicar por: ")
            vetor = multiplicar_vetor(vetor, valor)

        elif opcao_secundaria == 2:
            valor = n_int("Elevar por: ")
            vetor = elevar(vetor, valor)

        elif opcao_secundaria == 3:
            vetor = reduzir_fracao(vetor)

        elif opcao_secundaria == 4:
            vetor = substituir(vetor)

        elif opcao_secundaria == 5:
            opcoes_ord = """
            1 - ORDEM CRESCENTE
            2 - ORDEM DECRESCENTE
                """
            print(opcoes_ord)
            while True:
                opcao_ord = inteiro_positivo("Escolha a opção:  ")
                if opcao_ord == 1:
                    vetor = ordenar_valores_crescente(vetor)
                    break
                elif opcao_ord == 2:
                    vetor = ordenar_valores_decrescente(vetor)
                    break
                else:
                    print(f"Opção inválida. Digite 1 ou 2")

        elif opcao_secundaria == 6:
            embaralhar(vetor)
        elif opcao_secundaria == 7:
            break
        else:
            print("Opção inválida.")
        input("Pressione ENTER para continuar...")
        limpar_tela()

    return vetor


def opcoes_menu_principal():
    while True:
        opcao_valida = {
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
        }
        opcao = inteiro_positivo("Escolha uma opção: ")
        if opcao in opcao_valida:
            return opcao
        else:
            print(f"Opção Invalida, digite {opcao_valida}")


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


main()
