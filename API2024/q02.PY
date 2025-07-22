from funcoes import *
def main():
    while True:
        show_menu()
        opcao = n_int('Digite sua opção (1-Homem / 2-Mulher / 0-Sair): ')

        if opcao == 0:
            print("Saindo do programa...")
            break

        if opcao == 1:
            calorias_transport = 100 / 5  
            calorias_escada = 100 / 7     
        elif opcao == 2:
            calorias_transport = 100 / 6   
            calorias_escada = 100 / 8      
        else:
            print("Opção inválida. Tente novamente.")
            break

        peso_atual = float_positivo('Qual seu peso atual (kg)? ')
        perder_peso = float_positivo('Quantos kg deseja perder? ')
        dias_por_semana = inteiro_positivo('Quantos dias por semana você treina? ')
        tempo_por_dia = inteiro_positivo('Quanto tempo por dia (em minutos)? ')

        while True:
            proporcao_transport = n_float('Qual a proporção (%) do tempo para Transport (0 a 100)? ')
            if 0 <= proporcao_transport <= 100:
                break
            print("Proporção inválida. Digite um valor entre 0 e 100.")

        tempo_transport = tempo_por_dia * (proporcao_transport / 100)
        tempo_escada = tempo_por_dia - tempo_transport

        calorias_dia = (tempo_transport * calorias_transport) + (tempo_escada * calorias_escada)

        calorias_semana = calorias_dia * dias_por_semana

        calorias_objetivo = perder_peso * 7000
        
        semanas = 0
        calorias_perdidas = 0

        while calorias_perdidas < calorias_objetivo:
         calorias_perdidas += calorias_semana
         semanas += 1
         
        resultado = f''' ===== RESULTADO =====
        Você precisa perder {perder_peso} kg, o que equivale a {calorias_objetivo:.0f} calorias.
        Gasto semanal estimado: {calorias_semana:.1f} calorias.
        Você alcançará seu objetivo em aproximadamente {semanas:.1f} semanas.
        Plano de treino diário ({dias_por_semana} dias/semana)
        - {tempo_transport:.1f} minutos de Transport
        - {tempo_escada:.1f} minutos de Escada
        '''
        print(resultado)


def show_menu():
    menu = '''
======= FIT_CALCULATOR =======
1 - Homem
2 - Mulher
0 - Sair
'''
    print(menu)


main()
