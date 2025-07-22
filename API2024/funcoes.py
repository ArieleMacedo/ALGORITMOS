
def n_int(label: str):
    entrada = input(label)
    try:
        num = int(entrada)
        return num
    except ValueError:
        print("Digite um número inteiro válido")
    return n_int(label)


def inteiro_min_max(label: str, min: int, max: int):
    while True:
        try:
            numero = int(input(label))
            if numero < min or numero > max:
                print(f"O número deve estar entre {min} e {max}")
            else:
                return numero
        except ValueError:
            print("Digite um número válido que seja inteiro")


def inteiro_positivo(label: str):
    while True:
        try:
            numero = int(input(label))
            if numero < 0:
                print(f"O número deve ser maior que 0")
            else:
                return numero
        except ValueError:
            print("Digite um número válido que seja inteiro")


def inteiro_min(label: str, min: int):
    while True:
        try:
            numero = int(input(label))
            if numero < min:
                print(f"O numero deve ser no minimo {min}")
            else:
                return numero
        except ValueError:
            print("Digite um número válido que seja inteiro")


def float_min_max(label: str, min: float, max: float):
    while True:
        try:
            numero = float(input(label))
            if numero < min or numero > max:
                print(f"O número deve estar entre {min} e {max}")
            else:
                return numero
        except ValueError:
            print("Digite um número válido que seja float")


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


def n_float(label: str):
    while True:
        try:
            numero = float(input(label))
            return numero
        except ValueError:
            print("Digite um número válido que seja float")
            
def inteiro_max(label: str, max: int):
    while True:
        try:
            numero = int(input(label))
            if numero > max:
                print(f"O numero deve ser no máximo {max}")
            else:
                return numero
        except ValueError:
            print("Digite um número válido que seja inteiro")
