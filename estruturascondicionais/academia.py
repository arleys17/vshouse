#colocar a contagem na catraca
frequencia = 0

while True:
    entrada = input("O aluno passou na catraca? (s/n): ")

    if entrada.lower() == 's':
        frequencia += 1
        print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO!")
        
        if frequencia == 21:
            print("UHUU! AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ!")
            break  # encerra o programa após atingir 21 dias
    else:
        print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
        frequencia = 0  
# zera a contagem se o aluno faltar
    print(f"Frequência atual: {frequencia}/21\n")