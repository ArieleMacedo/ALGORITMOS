from utils import *

def main():
    qtd_maxima_de_caixas = int_positivo("Quantidade maxima de caixas: ")
    
    peso_maximo = float_positivo("Peso maximo suportado(Tonelada): ")*1000
    
    qtd_caixas = 0
    total_kg_frango = 0
    
    while qtd_caixas < qtd_maxima_de_caixas and total_kg_frango < peso_maximo:
        
        peso_da_caixa = float_positivo("\nPeso da caixa: ")
        
        if (total_kg_frango + peso_da_caixa) > peso_maximo:
            print("Peso excedido!")
            print(f"Quantidade de caixas: {qtd_caixas} \nPeso Total da carga: {total_kg_frango/1000:.2f}")
            return 
         
        qtd_caixas += 1
        total_kg_frango += peso_da_caixa

    
    print(f"Quantidade de caixas: {qtd_caixas} \nPeso Total da carga: {total_kg_frango/1000:.2f}")
        
            
        
    
    
 
main()