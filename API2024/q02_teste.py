def main():
    
    while True:
        show_menu()
        opcao = int(input('Digite uma opção: '))
        if opcao == 4:
            print("Saindo do programa...")
            break 
        if opcao == 1:
         transport = 100 / 6
         escada = 100/ 8
        
        elif opcao == 2:
         transport = 100 / 5
         escada = 100/ 7
         
        else:
         print('opcao invalida')
         continue
        
        peso_atual = float(input('Qual seu peso atual '))
        kg_perder = float(input('Quantos kg quer perder? '))
        dias = int(input('Quantos dias por semana irá treinar? '))
        tempo_dia = int(input('Quantos minutos por dia? '))
        proporcao = int(input('Proporçao de tempo para o transport: '))
        
        minutos_transport = tempo_dia * (proporcao/100)
        minutos_escada = tempo_dia - minutos_transport
        
        cal_por_dia = (minutos_transport * transport)+( minutos_escada * escada)
        
        gasto_semana = cal_por_dia * dias
        calorias_objetivo = kg_perder * 7000
    
        semana = 0
        calorias_perdidas = 0
            
        while calorias_perdidas < calorias_objetivo:
          calorias_perdidas =+ gasto_semana     
          semana += 1
          
          
        print(f'SEU PESO ATUAL: {peso_atual} Kg QUILOS A PERDER : {kg_perder} >>> Em cal: {calorias_objetivo:.2f}OBJETIVO QUE VAI SER ATINGIDO EM {semana} SEMANA(S)COM UM GASTO POR DIA DE {cal_por_dia} CALORIAS PARA CADA DIA VC FARÁ {minutos_transport} MIN DE TRASNPORT E {minutos_escada} MIN DE ESCADA')
        
    
def show_menu():

 menu = '''
 ====CALCULATOR====
 1 - MULHER
 2- HOMEM
 '''
 print(menu)
 
 
main()