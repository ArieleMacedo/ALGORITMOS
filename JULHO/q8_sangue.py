from utils import *

def main():
 idade = int_positivo("Idade: ")
 peso = float_positivo("Peso: ")

 classificar = eh_apto(idade,peso)
 print(classificar)
 
 
def eh_apto(idade,peso):
    
    if 18 <= idade <=60 and peso >=50:
          return "Apto para doar sangue"
    else:
        return "Não é Apto para doar sangue"
    
    
main()