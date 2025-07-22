import random
from funcoes import *
def main():
    print("Bem vindo ao gerador de senha!")
    tam = inteiro_positivo("Tamanho da senha: ")
    
    senha = gerar_senha(tam)
    
    print(f"Sua senha gerada foi: {senha}")
    while True:

     satisfeito = inteiro_min_max("1- Sim, 2- Não: ",1,2)
     if satisfeito == 1:
         print(f"Fico feliz que gostou!!! \nSenha escolhida: {senha}")
         break
     else:
         senha = gerar_senha(tam)
         print(f"Sua senha gerada foi: {senha}")


def gerar_senha(tamanho):
    senha = ''
    anterior = ''
    
    while len(senha) < tamanho:
       numero = str(random.randint(0,9))

       if anterior == '' or (numero != anterior and diferenca(numero,anterior) >1):
           anterior = numero
           senha += numero
           
    return senha


def diferenca(v1: str, v2: str) -> int:
  a = int(v1)
  b = int(v2)

  diff = a - b

  if a >= b:
    return diff
  else:
    return -1 * diff

main()