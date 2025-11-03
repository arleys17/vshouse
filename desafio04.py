import math
#idade do pet
idade_humana=int(input('digite a idade humana do seu cachorro em anos:'))
idade_pet=idade_humana *7

print(f'A idade do seu cachoerro em anos caninos e {idade_pet} anos.')

#opcoes do porte do cachorro
print('\n escolha o porte dos eu cachorro:')
print('1- grande porte (banho:75 | custo :20)')
print('2- medio porte (banho:60 | custo :15)')
print('3- pequeno porte (banho:50 |custo:5)')
 #marcar a oçao correto
opçao=int(input('digite o numero do porte:'))
#os valores
if opçao ==1:
  banho=75
  custo=20
  porte='grande'

elif opçao==2:
 banho=60
 custo=15
 porte='medio'
 
else:
 banho=50
 custo=5
 porte='pequeno'

#calculo dos banhos
banho=int(input('\n quantos banhos seu cachorro tomou em 12 meses?'))
lucro= banho-custo*banho
print('o cachorro de porte {porte} deu um lucro de R${lucro} reais em 12 meses!')