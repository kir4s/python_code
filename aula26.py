frase = str(input('Digite uma frasa: ')).lower().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print ('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))


#usando lower() na str pra confirmar as letras maiusculas e minusculas  
# na parte do codigo frase.find('a')+1 é pra ignorar a posiçao 0 na lista 
#na ultma linha o Rfind é pra procurar apartir do lado direito