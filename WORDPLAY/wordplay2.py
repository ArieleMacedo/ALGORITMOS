from utils import *

from str_utils import *


def main():
    palavras = load_palavras()
    while True:
        show_menu()
        opcao = int(input("Opção: "))
        if opcao == 0:
            break
        elif opcao == 1:
            palavra_pelo_tamanho(palavras)
        elif opcao == 2:
            palavras_sem_a_letra(palavras)
        elif opcao == 3:
            letras_proibidas = input("Letras Proibidas: ")
            mostrar_palavras_sem_letras_proibidas(palavras,letras_proibidas)
        elif opcao == 4:
            letras_permitidas = input("Letras Permitidas: ")
            mostrar_palavra_com_letras_permitidas(palavras,letras_permitidas)
        elif opcao == 5:
            letras_obrigatorias = input("Letras Obrigatorias: ")
            palavras_com_letras_obrigatorias(palavras,letras_obrigatorias)
        elif opcao == 6:
            palavras_em_ordem_alfabetica(palavras)
            
        input(">>>> continue...")


def show_menu():

    menu = """
    ===========WORDPLAY=============
    1- Palavras com N caracteres:
    2 -Palavras sem a Letra:
    3- Palavras sem Letras Proibidas
    4- Palavras com Letras Permitidas
    5- Palavras com Letras Obrigatórias
    6- Palavras em Ordem Alfabetica
    
    0 - Sair
    
    """
    print(menu)


def palavras_com_n_caracteres(caracter, palavra):
    return len(palavra) >= caracter


def palavra_pelo_tamanho(palavras):
    tamanho = int(input("Qtd minima de Caracteres:"))
    
    palavras_filtradas = filtrar(palavras, lambda x: len(x) >= tamanho)
    show_words(palavras_filtradas)
    
    contador = len(palavras)
    contador_filtro = len(palavras_filtradas)

    porcentagem = contador_filtro / contador * 100
    print(f"Total/Filtro: {contador_filtro}/{contador} ({porcentagem:.3f}) %")


def mostrar_palavra_sem_a_letra(palavra, letra):

    for caracter in palavra:
        if caracter == letra:
            return False

    return True

def show_words(palavras):
  for word in palavras:
    print(word)

def palavras_sem_a_letra(palavras):
    proibida = input("Qual é a letra proibida? ")
    
    palavras_filtradas = filtrar(palavras, lambda palavra: mostrar_palavra_sem_a_letra(palavra, proibida))
    show_words(palavras_filtradas)

    contador = len(palavras)
    contador_filtro = len(palavras_filtradas)

    porcentagem = contador_filtro / contador * 100
    print(f"Total/Filtro: {contador_filtro}/ {contador} ({porcentagem:.3f}) %")


def mostrar_palavras_sem_letras_proibidas(palavras,letras_proibidas):
    
    palavras_filtradas = filtrar(palavras, lambda palavra: avoids(palavra,letras_proibidas))
    show_words(palavras_filtradas)

    contador = len(palavras)
    contador_filtro = len(palavras_filtradas)

    porcentagem = contador_filtro / contador * 100
    print(f"Total/Filtro: {contador_filtro}/ {contador} ({porcentagem:.3f}) %")


def mostrar_palavra_com_letras_permitidas(palavras,letras_permitidas):
    
    palavras_filtradas = filtrar(palavras, lambda palavra: uses_only(palavra,letras_permitidas))
    show_words(palavras_filtradas)

    contador = len(palavras)
    contador_filtro = len(palavras_filtradas)

    porcentagem = contador_filtro / contador * 100
    print(f"Total/Filtro: {contador_filtro}/ {contador} ({porcentagem:.3f}) %")


def palavras_com_letras_obrigatorias(palavras,mandatory_letters):
    
    palavras_filtradas = filtrar(palavras, lambda palavra: uses_all(palavra,mandatory_letters))
    show_words(palavras_filtradas)

    contador = len(palavras)
    contador_filtro = len(palavras_filtradas)

    porcentagem = contador_filtro / contador * 100
    print(f"Total/Filtro: {contador_filtro}/ {contador} ({porcentagem:.3f}) %")


def palavras_em_ordem_alfabetica(palavras):
    arquivo = open("br-sem-acentos.txt")
    palavras_filtradas = filtrar(palavras, lambda palavra: eh_abcd(palavra))
    show_words(palavras_filtradas)

    contador = len(palavras)
    contador_filtro = len(palavras_filtradas)
            
    porcentagem = contador_filtro / contador * 100
    print(f"Total/Filtro: {contador_filtro}/ {contador} ({porcentagem:.3f}) %")
    
def load_palavras():
  return mapear(open('br-sem-acentos.txt').readlines(), lambda x:x.strip())

main()
