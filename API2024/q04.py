def main():
    
 origem = str(input('De: '))
 destino = str(input("Para: "))
 valor_rs = float(input("Valor em R$: "))
 valor_milhas= int(input('Valor em milhas: '))
 
 milhas_padrao= (valor_milhas / 1000) * 70
 milhas_baratas = (valor_milhas/1000) * 14.50
 percentual_padrao = (milhas_padrao / valor_rs) * 100
 percentual_barata = (milhas_baratas / valor_rs) * 100
 
 melhor_forma = calcular_melhor_forma(valor_rs,milhas_padrao,milhas_baratas)
 resultado = f'''
 RESUMO: COMPARATIVO
 ORIGEM: {origem}
 DESTINO: {destino}
 VALOR DA PASSAGEM R$: {valor_rs}
 VALOR PASSAGEM(MILHAS): {valor_milhas}
 ---------------------------------------
 VALOR MILHA PADRÃO (R$ 70/MIL): {milhas_padrao:.2f}
 \tDIFERENÇA : {percentual_padrao:.1f}%

 VALOR PASSAGEM(MILHAS)BARATAS (R$ 14.50/MIL): {milhas_baratas:.2f}
 \tDIFERENÇA : {percentual_barata:.1f}% 
 MELHOR FORMA DE COMPRA: {melhor_forma}
 '''
 print(resultado)


def calcular_melhor_forma(valor_rs,milhas_padrao,milhas_baratas):
  if valor_rs < milhas_padrao and valor_rs < milhas_baratas:
      return 'Comprar em Reais'
  elif milhas_padrao < valor_rs and milhas_padrao < milhas_baratas:
      return 'Comprar com milhas padrão'
  else:
      return'Comprar com milhas baratas'
main()