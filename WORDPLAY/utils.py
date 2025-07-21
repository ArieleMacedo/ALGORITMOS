def contem_caracter(palavra, caracter):
    for letra in palavra:
        if letra == caracter:
            return True
    return False


def avoids(palavra, letras_proibidas):
    
    for letra in palavra: 
        if contem_caracter(letras_proibidas,letra):
            return False
    return True


def uses_only(palavra, letras_permitidas):
    
    for letra in palavra:
        if not contem_caracter(letras_permitidas,letra):
            return False
    return True


def uses_all(palavra, letras_obrigatorias):
    
    for letra in letras_obrigatorias:
        if not contem_caracter(palavra,letra):
            return False
    return True


def eh_abcd(palavra):
    anterior = palavra[0] 
    
    for i in range(1,len(palavra)):
        atual = palavra[i]
        if anterior > atual:
            return False
        
        anterior = atual
        
    return True


def eh_maiuscula(letra):
    return ord(letra) >= 65 and ord(letra) <=90

def eh_minuscula(letra):
    return ord(letra) >= 97 and ord(letra) <=122

def maiuscula(texto):
    novo_texto = ''
    
    for letra in texto:
        if eh_minuscula(letra):
            novo_texto += chr(ord(letra)- 32)
        else:
            novo_texto += letra
    return novo_texto


def minuscula(texto):
    novo_texto = ''
    
    for letra in texto:
        if eh_maiuscula(letra):
            novo_texto += chr(ord(letra)+32)
        else:
            novo_texto += letra
    return novo_texto
        
    


