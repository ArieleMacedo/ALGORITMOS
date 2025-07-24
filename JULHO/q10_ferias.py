import random


def main():
 nome = input("Nome: ").strip().title()
 
 lista_de_mensagens = [
 f"Olá {nome}, aproveite suas férias", f"{nome}, tenha execelentes férias!!"
 f"Boas Férias, {nome}",f"{nome}, Até próximo Périodo!!", 
 f'{nome},Feliz férias', f'Até breve {nome}, boas férias', 
 f'{nome}, que bom que está de férias!', f'Finalmente férias hein {nome}?',
 f'Descanse e viaje muito nessas férias, {nome}', f'Ah, merecidas férias, parabéns, {nome}.']
 
 sortear = random.randint(1,10)
 print(lista_de_mensagens[sortear])

    
main()