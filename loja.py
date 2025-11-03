
#solicitar o valor da compra
valor_compra = float(input('digite o valor da compra: R$ '))

#calcular o valor da compra com desconto 
if valor_compra <250:
    print(f'infelismente vc nao pode ter desconto, mas falta pouco para conseguir seu desconto de 10%')
elif valor_compra >=250 and valor_compra <500:
    desconto = valor_compra * 0.10
    valor_final = (valor_compra - desconto)
    print('parabens vc ganhou um desconto de 10%, no valor final da sua compra')
    print(f'o valor final da sua compra sera de R$ {valor_final:.2f}')
else:
    desconto = valor_compra * 0.30
    valor_final = (valor_compra - desconto)
    print(f'parabens vc ganhou um desconto de 30% , no valor final de R$ {valor_final:.2f}')

