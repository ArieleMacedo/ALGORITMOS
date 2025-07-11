import random
import os
from utils import *


def gerar_manual():
    tamanho = inteiro_positivo("Tamanho: ")

    while True:
        valor_minimo = obter_float("Valor do número mínimo: ")
        valor_maximo = obter_float("Valor do número máximo: ")

        if valor_minimo > valor_maximo:
            print("o mínimo não pode ser maior que máximo")
        else:
            break
    vetor = []
    for i in range(tamanho):
        numero = float_min_max("Digite um valor: ", valor_minimo, valor_maximo)
        vetor.append(numero)
    return vetor


def gerar_aleatorio():
    tamanho = inteiro_positivo("Tamanho: ")

    while True:
        valor_minimo = obter_float("Valor do número mínimo: ")
        valor_maximo = obter_float("Valor do número máximo: ")

        if valor_minimo > valor_maximo:
            print("o mínimo não pode ser maior que máximo")
        else:
            break

    vetor = []
    for i in range(tamanho):
        numero = sortear(valor_minimo, valor_maximo)
        vetor.append(numero)
    return vetor


def carregar_valores():
    while True:
        nome_do_arquivo = input("Nome do arquivo: ")
        try:
            arquivo = open(nome_do_arquivo, "r")
            vetor = []
            for linha in arquivo:
                numeros = linha.strip().split(",")
                converter = [float(valor) for valor in numeros]
                vetor += converter
            return vetor
        except FileNotFoundError:
            print("Arquivo não encontrado")


def mostrar_valores(vetor):
    if not vetor:
        print("O vetor está vazio.")
    else:
        print(f"Valores: ", vetor)


def resetar(vetor, valor_padrao):
    if not vetor:
        print("O vetor está vazio.")
        return vetor
    for numero in range(len(vetor)):
        vetor[numero] = valor_padrao

    return vetor


def qtd_items(vetor):
    return len(vetor)


def maior_valor(vetor):
    maior = vetor[0]
    posicao = 0

    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
            posicao = i

    return maior, posicao


def menor_valor(vetor):
    menor = vetor[0]
    posicao = 0
    for i in range(1, len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]
            posicao = i

    return menor, posicao


def somatorio(vetor):
    somatorio = 0
    for valor in vetor:
        somatorio += valor

    return somatorio


def media(vetor):
    qtd = qtd_items(vetor)
    if qtd == 0:
        print("Não é possivel calcular a média. Vetor vazio")
        return 0.0

    soma = somatorio(vetor)
    media = soma / qtd

    return media


def valores_positivos(vetor):
    postivos = filtrar(vetor, eh_positivo)
    qtd = qtd_items(postivos)

    return postivos, qtd


def valores_negativos(vetor):
    negativos = filtrar(vetor, eh_negativo)
    qtd = qtd_items(negativos)

    return negativos, qtd


def multiplicar_vetor(vetor, valor):
    colecao = mapear(vetor, lambda x: multiplicar(x, valor))

    return colecao


def elevar(vetor, valor):
    colecao = mapear(vetor, lambda x: x**valor)

    return colecao


def fracao():
    numerador = inteiro_positivo("Numerador: ")
    while True:
        denominador = inteiro_positivo("Demominador: ")
        if denominador == 0:
            print("Denominador não pode ser zero.")
        else:
            break
    return numerador / denominador


def reduzir_fracao(vetor):
    valor = fracao()
    colecao = mapear(vetor, lambda x: x * valor)
    return colecao


def substituir(vetor):
    while True:

        valor_minimo = obter_float("Valor do número mínimo: ")
        valor_maximo = obter_float("Valor do número máximo: ")

        if valor_minimo > valor_maximo:
            print("o mínimo não pode ser maior que máximo")
        else:
            break
    negativos, qtd = valores_negativos(vetor)

    if qtd == 0:
        print("O vetor não possui números negativos.")
        return vetor

    sorteado = sortear(valor_minimo, valor_maximo)
    for i in range(len(vetor)):
        if eh_negativo(vetor[i]):
            vetor[i] = sorteado
    print(f"Os números negativos foram alterados para o numero sorteado :{sorteado}")

    return vetor


def sortear(min, max):
    while True:
        if min > max:
            print("o mínimo não pode ser maior que máximo")
        else:
            break
    return round(random.uniform(min, max), 2)


def ordenar_valores_crescente(vetor):
    return sorted(vetor)


def ordenar_valores_decrescente(vetor):
    return sorted(vetor, reverse=True)


def embaralhar(vetor):
    random.shuffle(vetor)


def adicionar_valores(vetor):
    num = obter_float("Número para adicionar no vetor: ")
    vetor.append(num)
    print("Valor removido com sucesso.")

    return vetor


def remover_por_valor_exato(vetor):
    while True:
        valor = obter_float("Valor: ")
        if valor in vetor:
            vetor.remove(valor)
            print("Valor removido com sucesso.")
            break
        else:
            print("Valor não encontrado no vetor. Tente novamente.")
    return vetor


def validar_posicao(vetor, label):
    while True:
        posicao = inteiro_positivo(label)
        if 0 <= posicao < len(vetor):
            return posicao
        else:
            print(f"Posição inválida. Digite um número entre 0 e {len(vetor) - 1}.")


def remover_por_posicao(vetor):
    posicao = validar_posicao(vetor, "Posição a remover: ")
    vetor.pop(posicao)
    print("Valor removido com sucesso.")

    return vetor


def edita_valor(vetor):
    while True:
        posicao = inteiro_positivo("Informe a posição a editar: ")
        if 0 <= posicao < len(vetor):
            break
        else:
            print(f"Posição inválida. Informe um número entre 0 e {len(vetor)-1}.")

    novo_valor = obter_float("Digite o novo valor: ")
    vetor[posicao] = novo_valor
    print("Valor editado com sucesso.")
    return vetor



def salvar_valores(vetor, nome_arquivo):
    arquivo = open(nome_arquivo, "w")
    linha = ""
    for i in range(len(vetor)):
        linha += str(vetor[i])
        if i < len(vetor) - 1:
            linha += ","
    arquivo.write(linha + "\n")
    print("Dados gravados")


def mapear(colecao, funcao_transformadora):
    nova_colecao = []

    for item in colecao:
        item_transformado = funcao_transformadora(item)
        nova_colecao.append(item_transformado)

    return nova_colecao


def eh_positivo(valor):
    return valor > 0


def eh_negativo(valor):
    return valor < 0


def multiplicar(valor1, valor2):
    return valor1 * valor2


def somar(valor1, valor2):
    return valor1 + valor2


def filtrar(colecao, criterio):
    nova_colecao = []

    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)

    return nova_colecao


def reduzir(colecao, redutora, inicial):
    acumulado = inicial

    for item in colecao:
        acumulado = redutora(acumulado, item)

    return acumulado
