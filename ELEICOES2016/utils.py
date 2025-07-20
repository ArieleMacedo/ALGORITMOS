def obter_inteiro(label):
    while True:
     try:
        numero = int(input(label))
        return numero
     except ValueError:
         print("Digite um número inteiro.")


def obter_inteiro_positivo(label):
    while True:
        try:
         numero = int(input(label))
         if numero >0:
             return numero
         else:
          print("Digite um número inteiro positivo(>0).")
          continue
        except ValueError:
         print("Digite um número inteiro.")

   