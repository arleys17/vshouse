print('encerrando o programa...')
print('tabuada de multiplicação')
#pede o numero de ser multiplicado
num=int(input('digite um numero para ver sua tabuada:'))
print('tabuada do {num}:\n')
 # mostrar a tabuada de 1 a 10 
for i in range (1 , 11) : 
    resultado = num * i
    print(f'{num} x {i} = {resultado} ' )
print('\n fim da tabuada ')