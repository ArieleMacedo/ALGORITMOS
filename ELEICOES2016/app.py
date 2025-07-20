import os
from function import *
from utils import *
def main():
    
 limpar_tela()
 inicializar()
 limpar_tela()
 
 while True:
    coligacoes = carregar_partidos_e_coligacoes('partidos_coligacoes.txt')
    candidatos = carregar_partidos_e_votos('candidatos_votos.txt')
    show_menu()
 
    opcao = obter_inteiro_positivo("\nEscolha uma opção>>>")
    limpar_tela()
    qtd_vagas = 29
    somatorio_votos = soma(candidatos)
    qe = quociente_eleitoral(somatorio_votos,qtd_vagas)
    if opcao == 9:
     break
    elif opcao == 1:
     imprimir_titulo("LISTAR CANDIDATOS")
     listar_candidatos(candidatos)
     
    elif opcao == 2:
      imprimir_titulo("TOTAL DE VOTOS VÁLIDOS")
      print(f"O total de votos válidos é: {somatorio_votos}\n")
      
    elif opcao == 3:
      imprimir_titulo("QUOCIENTE ELEITORAL")
      print(f"Quociente Eleitoral é: {qe}\n")
      
    elif opcao == 4:
        imprimir_titulo("TOTAL DE VOTOS POR COLIGAÇÃO")
        mostrar_votos_por_coligacao(coligacoes,candidatos)
        
    elif opcao == 5:
        imprimir_titulo("DISTRIBUIÇÃO DE VAGAS PELO QUOCIENTE PARTIDÁRIO")
        mostrar_quociente_partidario(coligacoes,candidatos,qe,qtd_vagas)
        
    elif opcao == 6:
        imprimir_titulo("DISTRIBUIÇÃO DE VAGAS DE SOBRA POR MÉDIA")
        mostrar_vagas_distribuidas_por_media(coligacoes,candidatos,qe,qtd_vagas)
    
    elif opcao == 7:
        imprimir_titulo("CANDIDATOS ELEITOS NO SISTEMA PROPORCIONAL")
        mostrar_candidatos_eleitos(coligacoes,candidatos,qe,qtd_vagas)
    
    elif opcao == 8:
        imprimir_titulo("CANDIDATOS ELEITOS NO SISTEMA MAJORITÁRIO")
        eleitos_no_sistema_majoritario(candidatos,qtd_vagas)
        
    input("Enter para continuar....")
    limpar_tela()

def show_menu():

 menu='''
                  MENU DE CONSULTA

1- Listar Candidatos

2- Calcular Total de Votos

3- Calcular Quociente Eleitoral

4- Calcular Total de Votos por Coligação

5- Distribuir Vagas por Quociente Partidário

6- Distribuir Vagas de Sobra por Média

7- Candidatos Eleitos No Sistema Proporcional

8- Candidatos Eleitos No Sistema Majoritário

9- Sair do Sistema
    '''
 print(menu)
 print("-" * 100)

def imprimir_titulo(titulo):
    limpar_tela()
    print("=" * 45)
    print(f"{titulo}")
    print("=" * 45)
    print()
 

def inicializar():
    print("\n" * 5)
    print("=" * 80)
    print("ELEIÇÕES TERESINA 2012".center(80))
    print("=" * 80)
    print("\n" * 5)
    input("Pressione Enter para continuar...")
    print("-" * 80)


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
main()