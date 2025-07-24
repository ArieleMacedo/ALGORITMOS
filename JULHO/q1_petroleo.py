from utils import *
def main():
    qtd_bombas = int_positivo('Quantidade de Bombas: ')
    barris_bomba = int_positivo("Quantidade barris por Bomba: ")
    valor_reducao = int_min_max("Percentual de Redução: ", 1,100)
    limite_minimo = int_positivo("Limite minimo de barris: ")
    percentual = valor_reducao/100
    
    contador_de_ciclos = 0 
    barris_retirado = 0
    
    while barris_bomba >= limite_minimo:

        barris_retirado += barris_bomba 
        barris_bomba -= barris_bomba*percentual
        
        contador_de_ciclos += 1

    total_ciclos = contador_de_ciclos *qtd_bombas   
    total_barris_retirado = barris_retirado * qtd_bombas
    print(f"Ciclos Realizados: {total_ciclos} \nQuantidade de Barris Extraído: {total_barris_retirado:.0f}")
        
        
main()