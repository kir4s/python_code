# Recebe a entrada do usuário como uma string
n = input('Digite um número: ')

# Converte a string para um número inteiro
n = int(n)

# Calcula o antecessor e o sucessor
a = n - 1
s = n + 1

# Exibe o resultado
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))
