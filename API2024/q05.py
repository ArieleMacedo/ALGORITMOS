from funcoes import *

def main():

    qtd = 0
    lista_itens = ""
    total = 0

    while True:
        show_menu()
        opcao = obter_opcao()

        if opcao == 0:
            break

        if opcao == 1:
            descricao = input("Adcione uma Descriçao: ")
            especificacao = input("Espeficação do Item: ")
            valor = float_positivo("Valor do Item: ")

            qtd += 1
            total += valor

            lista_itens += f"""{qtd} - {descricao}  -  {especificacao}  -  R${valor:.2f}
         """

        elif opcao == 2:
            if qtd == 0:
                print("Nenhum item adcionado ainda")
            else:
                print("\n------LISTA DE ITENS------")
                print(lista_itens)
                t_total = f"""VALOR TOTAL:            R${total}
            
            """
                print(t_total)
                parcelamento(total)
        else:
            print("Opção inválida.")


def show_menu():
    menu = """
 1 - INCLUIR ITEM
 2 - IMPRIMIR LISTA
 0 - SAIR
 """
    print(menu)


def parcelamento(total):
    print("\n--------Pagamento----------")
    print(f"Pagamento à vista: R$ {total:.2f}")

    if total > 30 and total <= 100:
        print("\n--------Parcelado Sem juros----------")
        i = 2
        while i <= 3:
            parcela = total / i
            print(f"{i} de R$ {parcela:.2f}")
            i += 1
    else:
        print("\n--------Parcelado Sem juros----------")
        i = 2
        while i <= 5:
            parcela = total / i
            print(f"{i}x de R$ {parcela:.2f}")
            i += 1

    print("Parcelamento com juros compostos (5% a.m.):")
    i = 1
    juros = 0.05
    while i <= 6:
        parcela_juros = total * ((1 + juros) ** i) / i
        print(f"{i}x de R$ {parcela_juros:.2f}")
        i += 1


def obter_opcao():
        opcao = n_int("Digite uma opção>>>> ")
        if opcao != 0 and opcao != 1 and opcao != 2:
            print("Opção inválida. Tente novamente.")
            return obter_opcao()
        return opcao



main()
