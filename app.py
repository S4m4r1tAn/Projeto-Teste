from datetime import date
from time import sleep

#Calcular idade:
nome = input('Qual eh o seu nome: ')
nascimento = int(input('Em que ano voce nasceu: '))
data_de_hoje = date.today().year
idade = data_de_hoje - nascimento
print(f'Meu nome eh {nome} e eu tenho {idade} anos.')
sleep(3)
print('...........................MUITO PRAZER!')
