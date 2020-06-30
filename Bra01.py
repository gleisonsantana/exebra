# fazer um projeto em python 3, que funcione via linha de comando, ele irá receber um parametro que é um nome,
# e outro que vai ser o tipo de adjetivo, bom ou mau. Os adjetivos fica a sua escolha,
# e tem que ser escolhido randomicamente

nome = str(input('Digite seu nome : '))
pergunta = str(input('Você se considera uma pessoa boa ou ma? '))
if pergunta == 'boa':
    print ('Parabens {}, seu lindo(a), continue assim.'.format(nome))
else:
    print ('Você é feio(a) {} e precisa melhorar.'.format(nome))




