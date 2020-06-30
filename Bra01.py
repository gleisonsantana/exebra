# fazer um projeto em python 3, que funcione via linha de comando, ele irá receber um parametro que é um nome,
# e outro que vai ser o tipo de adjetivo, bom ou mau. Os adjetivos fica a sua escolha,
# e tem que ser escolhido randomicamente

import random
bom = ['Lindo', 'fofo', 'maravilhoso']
mal = ['Feio', 'bobao', 'trouxao']
nome = str(input('Digite seu nome : '))
pergunta = str(input('Você se considera uma pessoa boa ou ma? '))
if pergunta == 'boa':
    print (f' \n Parabens {nome} ', end='')
    print (random.choice(bom))
else:
    print (f'\n Você {nome} é ', end='')
    print (random.choice(mal))




