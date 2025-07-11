from str_utils import minuscula, uses_all, uses_only, avoids, eh_abced


def main():
    while True:
        show_menu()
        opcao = int(input("Opção: "))
        if opcao == 0:
            break
        elif opcao == 1:
            palavra_pelo_tamanho()
        elif opcao == 2:
            palavras_sem_a_letra()
        elif opcao == 3:
            letras_proibidas = input("Letras Proibidas: ")
            mostrar_palavras_sem_letras_proibidas(letras_proibidas)
        elif opcao == 4:
            letras_permitidas = input("Letras Permitidas: ")
            mostrar_palavra_com_letras_permitidas(letras_permitidas)
        elif opcao == 5:
            letras_obrigatorias = input("Letras Obrigatorias: ")
            palavras_com_letras_obrigatorias(letras_obrigatorias)
        elif opcao == 6:
            palavras_em_ordem_alfabetica()
            
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


def palavra_pelo_tamanho():
    tamanho = int(input("Qtd minima de Caracteres:"))
    arquivo = open(
        "C:\\Users\\ariel\\Downloads\\Algoritmos (1)-20250523T183030Z-1-001\\Algoritmos (1)\\String\\palavrass.txt"
    )
    contador = 0
    contador_filtro = 0

    for linha in arquivo:
        palavra = linha.strip()
        contador += 1

        if len(palavra) >= tamanho:
            # if palavras_com_n_caracteres(tamanho, palavra):
            contador_filtro += 1
            print(palavra)

    porcentagem = contador_filtro / contador * 100
    print(f"Total/Filtro: {contador_filtro}/{contador} ({porcentagem:.3f}) %")


def mostrar_palavra_sem_a_letra(palavra, letra):

    for caracter in palavra:
        if caracter == letra:
            return False

    return True


def palavras_sem_a_letra():
    arquivo = open(
        "C:\\Users\\ariel\\Downloads\\Algoritmos (1)-20250523T183030Z-1-001\\Algoritmos (1)\\String\\palavrass.txt"
    )

    proibida = input("Qual é a letra proibida? ")

    contador = 0
    contador_filtro = 0

    for linha in arquivo:
        palavra = linha.strip()
        contador += 1
        if mostrar_palavra_sem_a_letra(palavra, proibida):
            contador_filtro += 1
            print(palavra)

    porcentagem = contador_filtro / contador * 100
    print(f"Total/Filtro: {contador_filtro}/ {contador} ({porcentagem:.3f}) %")


def mostrar_palavras_sem_letras_proibidas(letras_proibidas):
    arquivo = open("br-sem-acentos.txt")
    contador = 0
    contador_filtro = 0
    
    for linha in arquivo:
        palavra = linha.strip()
        contador += 1
        if avoids(palavra, letras_proibidas):
            contador_filtro += 1
            print(palavra)

    porcentagem = contador_filtro / contador * 100
    print(f"Total/Filtro: {contador_filtro}/ {contador} ({porcentagem:.3f}) %")


def mostrar_palavra_com_letras_permitidas(letras_permitidas):
    arquivo = open(
        "C:\\Users\\ariel\\Downloads\\Algoritmos (1)-20250523T183030Z-1-001\\Algoritmos (1)\\String\\palavrass.txt"
    )
    contador = 0
    contador_filtro = 0

    for linha in arquivo:
        palavra = linha.strip()
        contador += 1
        if uses_only(palavra, letras_permitidas):
            contador_filtro += 1
            print(palavra)

    porcentagem = contador_filtro / contador * 100
    print(f"Total/Filtro: {contador_filtro}/ {contador} ({porcentagem:.3f}) %")


def palavras_com_letras_obrigatorias(mandatory_letters):
    arquivo = open(
        "C:\\Users\\ariel\\Downloads\\Algoritmos (1)-20250523T183030Z-1-001\\Algoritmos (1)\\String\\palavrass.txt"
    )
    contador = 0
    contador_filtro = 0

    for linha in arquivo:
        palavra = linha.strip()
        contador += 1
        if uses_all(palavra, mandatory_letters):
            contador_filtro += 1
            print(palavra)

    porcentagem = contador_filtro / contador * 100
    print(f"Total/Filtro: {contador_filtro}/ {contador} ({porcentagem:.3f}) %")

def palavras_em_ordem_alfabetica():
    arquivo = open(
        "C:\\Users\\ariel\\Downloads\\Algoritmos (1)-20250523T183030Z-1-001\\Algoritmos (1)\\String\\palavrass.txt"
    )
    contador = 0
    contador_filtro = 0
    
    for linha in arquivo:
        palavra = minuscula(linha.strip())
        contador +=1
        
        if eh_abced(palavra):
            contador_filtro +=1
            print(palavra)
            
    porcentagem = contador_filtro / contador * 100
    print(f"Total/Filtro: {contador_filtro}/ {contador} ({porcentagem:.3f}) %")
main()
