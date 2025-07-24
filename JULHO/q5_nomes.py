from utils import *

def main():
    
    lista = []

    while True:
        nome = input("Nome: ").strip()
        
        if nome == 'fim':
            break
        
        if len(nome) >= 4:
            lista.append(nome)  

    
    print(f"Quantidade de nomes: {len(lista)}")
   
main()    
        