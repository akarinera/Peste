# Crie um programa para determinar se um número inteiro dado é divisível por 2, 3 ou nenhum deles. Utilize uma única linha de código dentro de cada bloco 'if', 'elif' e 'else' para imprimir 
# "divisível por 2", "divisível por 3" ou "não é divisível por 2 ou 3" respectivamente."

numero = int(input('Digite um número: '))

if numero %2 == 0:
    print('É divisível por 2')
elif numero %3 == 0:
    print('É divisível por 3')
else:
    print('Não é divisível por 2 e 3')