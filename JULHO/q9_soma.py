from utils import *

def main():
   
   numero = int_min_max("Digite um número: ",1,99)
   somatorio = numero
   
   while True:
       novo_num = int_min_max("Digite outro número: ",1,99)
       somatorio+= novo_num
       
       if novo_num == numero:
           break
       
   print(f"Somatorio: {somatorio}")
main()