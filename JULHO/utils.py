
def numero_int(label: str):
    while True:
        try:
            numero = int(input(label))
            return numero
        except ValueError:
            print("Digite um número válido que seja int")


def int_positivo(label: str):
    while True:
        try:
            numero = int(input(label))
            if numero < 0:
                print(f"O número deve ser maior que 0")
            else:
                return numero
        except ValueError:
            print("Digite um número válido que seja int")


def numero_int_negativo(label):
    while True:
        try:
            numero = int(input(label))
            if numero > 0:
                print(f"O número deve ser menor que 0")
            else:
                return numero
        except ValueError:
            print("Digite um número válido que seja int")
 
    
def int_min(label: str, min:int):
    while True:
        try:
            numero = int(input(label))
            if numero < min:
                print(f"O número deve ser no minimo: {min}")
            else:
                return numero
        except ValueError:
            print("Digite um número válido que seja int")


def int_max(label: str, max:int):
    while True:
        try:
            numero = int(input(label))
            if numero < max:
                print(f"O número deve ser no maximo: {max}")
            else:
                return numero
        except ValueError:
            print("Digite um número válido que seja int")


def int_min_max(label: str, min:int, max:int):
    while True:
        try:
            numero =int(input(label))
            if numero < min or numero > max:
                print(f"O número deve estar entre {min} e {max}")
            else:
                return numero
        except ValueError:
            print("Digite um número válido que seja int")
    

def float_positivo(label: str):
    while True:
        try:
            numero = float(input(label))
            if numero < 0:
                print(f"O número deve ser maior que 0")
            else:
                return numero
        except ValueError:
            print("Digite um número válido que seja float")
            

def float_min_max(label: str, min:float, max:float):
    while True:
        try:
            numero =float(input(label))
            if numero < min or numero > max:
                print(f"O número deve estar entre {min} e {max}")
            else:
                return numero
        except ValueError:
            print("Digite um número válido que seja int")
            
                        
def filtrar (colecao,criterio):
    nova_colecao = []
    
    for item in colecao:
        if criterio(item):
            nova_colecao.append(item)
    
    return nova_colecao


def obter_texto(label):
  while True:
        try:
            texto = str(input(label))
            return texto
        except ValueError:
            print("Digite um número válido que seja string")