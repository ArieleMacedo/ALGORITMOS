
def main():

    texto = input("Texto: ").lower()
    chave_c = int(input("Chave C: "))
    cripto = vogals_consoantes(texto,chave_c)
    print(f"Texto criptografado: {cripto}")

def vogals_consoantes(texto,chave_c):
    novo_texto = ''
    vogais = ["a","e","i","o","u"]
    consoante = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

    for letra in texto:
     if letra in vogais:
        posicao = vogais.index(letra)
        nova_posicao = girar_posicao(posicao,chave_c, len(vogais))
        novo_texto += vogais[nova_posicao]
        
     elif letra in consoante:
        posicao = consoante.index(letra)
        nova_posicao = girar_posicao(posicao,chave_c*2, len(consoante))
        novo_texto += consoante[nova_posicao]
        
     else:
         novo_texto += letra
         
    return novo_texto
    
    
def girar_posicao(posicao,chave,tamanho):
    nova = posicao + chave
    while nova >= tamanho:
        nova -= tamanho
    
    return nova



main()