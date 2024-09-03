nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em CAPSLOCK fica:{}'.format(nome.upper()))
print('Seu nome em sem CAPSLOCK fica:{}.'.format(nome.lower()))
print('Seu nome tem {} letras!.'.format(len(nome)- nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))



# .strip() usado pra corrigir erros de digitaçao utilizando a barra de espaço no começo e no fim do nome 
# - nome.count(' ') pra eleminar o espaço entre o nome e contar apenas as letras 
# na ultima barra de codigo usamos o comando (nome.find(' ')) pra contar quantas letras tem no primeiro nome 