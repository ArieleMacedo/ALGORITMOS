from utils import *

def main():
    avaliacao = obter_avaliacoes()
    total_pontos = 0
    qtd_pesos = 0
    somatorio_nota = 0
    
    for i in range(avaliacao):
        nota = float_min_max(f"Nota da {i+1} Avaliação: ",0,10)
        peso = int_min_max(f"Peso da {i+1} Avaliação: ",1,3)
        
        
        qtd_pesos += (peso)
        total_pontos += (nota * peso)
        somatorio_nota += nota

    media_ponderada = calcular_media_ponderada(total_pontos,qtd_pesos)
    print(f"\nMédia Ponderada: {media_ponderada:.2f}")
    
    if media_ponderada >= 8:
        print('Parabéns Pela Nota')
        
    media_normal = somatorio_nota/avaliacao
    print(f"Se a sua média fosse aritmética: {media_normal:.2f} ")
        
def obter_avaliacoes():
    qtd_avaliacoes = int_min_max("Quantidade de avaliações feitas: ",2,6)
    return qtd_avaliacoes



def calcular_media_ponderada(avaliacoes,pesos):
    return avaliacoes / pesos


    
     
main()